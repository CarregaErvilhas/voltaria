#!/usr/bin/env python3
"""Checks every skills/*/SKILL.md. Fails on the first run with any problem.

- frontmatter: starts the file, has `name` and a quoted `description`, nothing unquoted with ": ";
- `name` equals the folder name and uses only lowercase letters, digits and hyphens;
- `description` is at most 1024 characters;
- no prices (euros or cents) in the skill text: prices live in tools and in knowledge/;
- no term from the "Evitar" column of glossario.md, outside URLs, `code` and the "## Fontes" section.

Usage: scripts/check-skills.py   (run from the repo root; stdlib only)
"""
import glob
import os
import re
import sys

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
PRICE_RE = re.compile(r"\d[\d  .,]*\s?(€|EUR\b|cêntimos)|€\s?\d", re.I)
STRIP_RE = re.compile(r"`[^`]*`|https?://\S+|\]\([^)]*\)")


def glossary_terms(path="glossario.md"):
    terms = []
    for line in open(path, encoding="utf-8"):
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| Termo"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        for t in cells[1].split(";"):
            t = t.strip()
            if t and t not in ("-", "—"):
                terms.append((cells[0], t, re.compile(r"(?<![\w-])" + re.escape(t) + r"(?![\w-])", re.I)))
    return terms


def frontmatter(text):
    if not text.startswith("---\n"):
        return None, ["frontmatter must start on line 1 with '---'"]
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, ["frontmatter has no closing '---'"]
    fields, errors = {}, []
    for n, line in enumerate(text[4:end].split("\n"), start=2):
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep:
            errors.append(f"line {n}: not a 'key: value' line")
            continue
        value = value.strip()
        if value.startswith('"'):
            if not value.endswith('"') or len(value) < 2:
                errors.append(f"line {n}: unterminated quoted value")
                continue
            inner = value[1:-1]
            if re.search(r'(?<!\\)"', inner):
                errors.append(f'line {n}: unescaped " inside a quoted value')
            value = inner.replace('\\"', '"')
        elif ": " in value or value.startswith(("[", "{", "&", "*", "!", "|", ">")):
            errors.append(f"line {n}: '{key}' must be quoted (YAML would misread it)")
        fields[key.strip()] = value
    return fields, errors


def main():
    terms = glossary_terms()
    bad = 0
    files = sorted(glob.glob("skills/*/SKILL.md"))
    if not files:
        print("no skills/*/SKILL.md found (run from the repo root)")
        return 1
    for f in files:
        problems = []
        text = open(f, encoding="utf-8").read()
        fields, errors = frontmatter(text)
        problems += errors
        folder = os.path.basename(os.path.dirname(f))
        if fields is not None:
            name, desc = fields.get("name", ""), fields.get("description", "")
            if name != folder:
                problems.append(f"name '{name}' differs from folder '{folder}'")
            if not NAME_RE.match(name):
                problems.append(f"name '{name}' must be lowercase letters, digits and hyphens")
            if not desc:
                problems.append("missing description")
            elif len(desc) > 1024:
                problems.append(f"description has {len(desc)} characters (max 1024)")
            raw = text[: text.find("\n---\n", 4)]
            if desc and 'description: "' not in raw and not any("'description'" in e for e in errors):
                problems.append("description must be quoted")

        body = text.split("\n## Fontes", 1)[0]
        for n, line in enumerate(body.split("\n"), start=1):
            clean = STRIP_RE.sub(" ", line)
            if PRICE_RE.search(clean):
                problems.append(f"line {n}: price in skill text: {line.strip()[:100]}")
            for use, avoid, rx in terms:
                if rx.search(clean):
                    problems.append(f"line {n}: '{avoid}' (glossary: use '{use}'): {line.strip()[:100]}")
        for p in problems:
            print(f"{f}: {p}")
        bad |= bool(problems)
    if bad:
        return 1
    print(f"Skills: {len(files)} skills with valid frontmatter, no prices, glossary terms respected")
    return 0


if __name__ == "__main__":
    sys.exit(main())
