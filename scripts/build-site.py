#!/usr/bin/env python3
"""Builds the Voltaria website from site/: one page per language, plus what search engines and AI
crawlers read. pages.yml publishes the result on GitHub Pages.

- site/index.html is the template and site/strings.json the text, with the same keys in "pt" and
  "en". An element with data-i="key" gets the string as its content (it may hold HTML); a key in
  double braces gets it escaped, for attributes and <head>. Keys starting with "page." come from
  this script. A missing key, a key only one language has or a key no page uses fails the build.
- Portuguese goes to /, English to /en/, with the text already in the HTML.
- The list of topics and llms.txt come from skills/ and knowledge/, so they can't go stale.
- The Portuguese text follows glossario.md: a term from its "Evitar" column fails the build, as it
  does in the skills (scripts/check-skills.py).
- site/static/ is copied as is: fonts, icons, the images for link previews.

Usage: scripts/build-site.py [--out DIR]   (default _site/; run from the repo root; stdlib only)
       scripts/build-site.py --check       (build into a temporary folder and report; checks.yml)
"""
import argparse
import html
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SITE_URL = "https://voltaria.ocarroeletrico.com"
REPO_URL = "https://github.com/CarregaErvilhas/voltaria"
OHMIGO_MCP = "https://ohmigo.ocarroeletrico.com/mcp"
LANGS = {
    # path: where the page lives; root: how that page reaches the site's root (relative, so the
    # build also works opened from disk or under another domain).
    "pt": {"path": "", "root": "./", "lang": "pt-PT", "locale": "pt_PT"},
    "en": {"path": "en/", "root": "../", "lang": "en", "locale": "en_GB"},
}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
ELEMENT_RE = re.compile(r'<(\w+)([^>]*?)\sdata-i="([^"]+)"([^>]*)>\s*</\1>')
BRACES_RE = re.compile(r"\{\{([\w.-]+)\}\}")
TOPICS_MARK = "<!--topics-->"
TAGS_RE = re.compile(r"<code>.*?</code>|<[^>]+>", re.S)
LOCAL_RE = re.compile(r'(?:href|src)="(\.\.?/[^"#?]*)"')


def load_check_skills():
    """scripts/check-skills.py, for its glossary and frontmatter parsers (one source for both)."""
    spec = importlib.util.spec_from_file_location("check_skills", Path("scripts/check-skills.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def skills(check):
    """(name, description) of every skill, sorted by name."""
    out = []
    for f in sorted(Path("skills").glob("*/SKILL.md")):
        name = f.parent.name
        if not NAME_RE.match(name):
            continue
        fields, _ = check.frontmatter(f.read_text(encoding="utf-8"))
        out.append((name, (fields or {}).get("description", "")))
    return out


def json_ld(lang, strings):
    """schema.org data for search engines: what the site is, in which language, and its translation."""
    conf = LANGS[lang]
    data = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": f"{SITE_URL}/{conf['path']}#website",
        "name": "Voltaria",
        "url": f"{SITE_URL}/{conf['path']}",
        "inLanguage": conf["lang"],
        "description": strings[lang]["meta.desc"],
        "image": f"{SITE_URL}/og-{lang}.png",
        "isAccessibleForFree": True,
        "sameAs": [REPO_URL],
    }
    other = next(l for l in LANGS if l != lang)
    data["workTranslation" if lang == "pt" else "translationOfWork"] = {"@id": f"{SITE_URL}/{LANGS[other]['path']}#website"}
    # The payload sits inside <script>: escape "<" so no string can close it.
    return json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")


def page_values(lang, strings):
    """The page.* keys, which differ per language and are written as is (no escaping)."""
    conf = LANGS[lang]
    return {
        "page.jsonld": json_ld(lang, strings),
        "page.lang": conf["lang"],
        "page.root": conf["root"],
        "page.url": f"{SITE_URL}/{conf['path']}",
        "page.url.pt": f"{SITE_URL}/",
        "page.url.en": f"{SITE_URL}/en/",
        "page.og.locale": conf["locale"],
        "page.og.image": f"{SITE_URL}/og-{lang}.png",
        "page.current.pt": 'aria-current="page"' if lang == "pt" else "",
        "page.current.en": 'aria-current="page"' if lang == "en" else "",
    }


def render(template, strings, lang, topics_html):
    T = strings[lang]
    P = page_values(lang, strings)
    used, missing = set(), set()

    def element(m):
        key = m.group(3)
        used.add(key)
        if key not in T:
            missing.add(key)
            return m.group(0)
        return f"<{m.group(1)}{m.group(2)}{m.group(4)}>{T[key]}</{m.group(1)}>"

    def braces(m):
        key = m.group(1)
        if key in P:
            return P[key]
        used.add(key)
        if key not in T:
            missing.add(key)
            return m.group(0)
        return html.escape(T[key], quote=True)

    out = ELEMENT_RE.sub(element, template)
    out = BRACES_RE.sub(braces, out)
    out = out.replace(TOPICS_MARK, topics_html)
    leftover = re.findall(r'data-i="[^"]*"', out)
    return out, used, missing, leftover


def llms_txt(skill_list, facts):
    lines = [
        "# Voltaria",
        "",
        "> Agent Skills in European Portuguese about electric mobility in Portugal: charging at home and",
        "> in public, condominiums, the electrical installation, grants and tax, batteries and range, and",
        "> the law (DL 93/2025, AFIR). Written for AI assistants, not for people. Answer in the user's",
        "> language.",
        "",
        f"Read it through the ohmigo MCP server ({OHMIGO_MCP}, Streamable HTTP, no auth),",
        "tool `ev_rules_portugal`: no arguments lists the topics, `topic` returns that skill, and",
        "`topic` + `query` returns dated facts with their source. Without MCP, each release has one zip",
        f"per skill: {REPO_URL}/releases",
        "",
        "Content is CC-BY-4.0. Credit it with:",
        f'"Conteúdo do Voltaria ({REPO_URL}), CC-BY-4.0".',
        "",
        "## Skills",
        "",
    ]
    for name, desc in skill_list:
        lines.append(f"- [{name}]({REPO_URL}/blob/main/skills/{name}/SKILL.md): {desc}")
    lines += ["", "## Facts", ""]
    for name in facts:
        lines.append(f"- [{name}]({REPO_URL}/blob/main/knowledge/{name}.json): `topic` \"{name}\" + `query`")
    return "\n".join(lines) + "\n"


def last_change():
    """The date of the last commit, for the sitemap's lastmod (pages.yml deploys only on changes)."""
    try:
        return subprocess.run(["git", "log", "-1", "--format=%cs"], capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def sitemap():
    lastmod = last_change()
    lastmod = f"\n    <lastmod>{lastmod}</lastmod>" if lastmod else ""
    alternates = "".join(
        f'\n    <xhtml:link rel="alternate" hreflang="{LANGS[l]["lang"]}" href="{SITE_URL}/{LANGS[l]["path"]}"/>'
        for l in LANGS) + f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE_URL}/"/>'
    urls = "".join(f"\n  <url>\n    <loc>{SITE_URL}/{LANGS[l]['path']}</loc>{lastmod}{alternates}\n  </url>" for l in LANGS)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'
            f"{urls}\n</urlset>\n")


def build(out):
    problems = []
    check = load_check_skills()
    strings = json.loads(Path("site/strings.json").read_text(encoding="utf-8"))
    template = Path("site/index.html").read_text(encoding="utf-8")

    if set(strings) != set(LANGS):
        problems.append(f"site/strings.json must have exactly the languages {sorted(LANGS)}")
    keys = {lang: set(strings.get(lang, {})) for lang in LANGS}
    for a in LANGS:
        for b in LANGS:
            for k in sorted(keys[a] - keys[b]):
                problems.append(f'string "{k}" is in "{a}" but not in "{b}"')
    for lang in LANGS:
        for k, v in strings.get(lang, {}).items():
            if not isinstance(v, str) or not v.strip():
                problems.append(f'string "{k}" in "{lang}" is empty')
            elif "</script" in v.lower():
                problems.append(f'string "{k}" in "{lang}" closes a <script>')

    for _, term, rx in check.glossary_terms():
        for k, v in strings.get("pt", {}).items():
            if rx.search(TAGS_RE.sub(" ", v)):
                problems.append(f'string "{k}" uses "{term}" (glossario.md: avoid)')

    skill_list = skills(check)
    if not skill_list:
        problems.append("no skills/*/SKILL.md found (run from the repo root)")
    topics_html = "\n".join(f"            <li><code>{html.escape(n)}</code></li>" for n, _ in skill_list)
    facts = sorted(p.stem for p in Path("knowledge").glob("*.json") if NAME_RE.match(p.stem))

    out.mkdir(parents=True, exist_ok=True)
    used_all = set()
    for lang, conf in LANGS.items():
        page, used, missing, leftover = render(template, strings, lang, topics_html)
        used_all |= used
        problems += [f'template uses "{k}", missing in "{lang}"' for k in sorted(missing)]
        problems += [f"template still has {x}: its element must be empty, and its string must exist" for x in leftover]
        dest = out / conf["path"] / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page, encoding="utf-8")
    for k in sorted(keys.get("pt", set()) - used_all):
        problems.append(f'string "{k}" is not used by the template')

    shutil.copytree("site/static", out, dirs_exist_ok=True)
    (out / "CNAME").write_text(SITE_URL.split("//", 1)[1] + "\n", encoding="utf-8")
    (out / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    (out / "sitemap.xml").write_text(sitemap(), encoding="utf-8")
    (out / "llms.txt").write_text(llms_txt(skill_list, facts), encoding="utf-8")

    # Every local link and file the pages and the manifest point to must be in the build.
    for conf in LANGS.values():
        page_dir = out / conf["path"]
        for ref in LOCAL_RE.findall((page_dir / "index.html").read_text(encoding="utf-8")):
            target = (page_dir / ref).resolve()
            if not (target / "index.html" if ref.endswith("/") else target).is_file():
                problems.append(f"/{conf['path']}index.html points to {ref}, which isn't in the build")
    manifest = json.loads((out / "site.webmanifest").read_text(encoding="utf-8"))
    for i in manifest.get("icons", []):
        if not (out / i["src"].lstrip("/")).is_file():
            problems.append(f"site.webmanifest points to {i['src']}, which isn't in the build")
    return problems, len(skill_list)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", default="_site", help="output folder (default: _site)")
    ap.add_argument("--check", action="store_true", help="build into a temporary folder and only report problems")
    args = ap.parse_args()
    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            problems, n = build(Path(tmp))
    else:
        out = Path(args.out)
        here = Path.cwd().resolve()
        if out.resolve() == here or out.resolve() in here.parents or (out / ".git").exists():
            print(f"site: refusing to replace {args.out}: pick an output folder of its own")
            return 1
        if out.exists():
            shutil.rmtree(out)
        problems, n = build(out)
    for p in problems:
        print(f"site: {p}")
    if problems:
        return 1
    print(f"site: built {len(LANGS)} pages with {n} topics" + ("" if args.check else f" into {args.out}/"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
