#!/usr/bin/env python3
"""Builds the Claude plugin folder from the repo, for the `plugin` branch that the directory follows.

The repo root can't be the plugin: the directory scans the whole plugin folder, and site/, scripts/
and evals/ (images the scripts render, an API key read from the environment) hold every version for
a reviewer. So the plugin is only what Claude reads:

- .claude-plugin/plugin.json: plugin/plugin.json with `version` set;
- .claude-plugin/icon.png: the Voltaria icon (the directory takes it only on the first submission);
- skills/, knowledge/, glossario.md (the skills point to it), LICENSE;
- README.md: plugin/README.md, which says what the plugin sends where (the security scan reads it).

Fails if the result holds anything the directory would hold for review: a file type other than
text, PNG, JSON or Markdown, or a non-image file over 256 KiB.

Usage: scripts/build-plugin.py VERSION OUT_DIR   (run from the repo root; stdlib only)
       VERSION is MAJOR.MINOR.PATCH, the release tag without the "v".
"""
import json
import os
import re
import shutil
import sys

MAX_TEXT = 256 * 1024
TEXT = (".md", ".json")


def main():
    if len(sys.argv) != 3 or not re.fullmatch(r"\d+\.\d+\.\d+", sys.argv[1]):
        sys.exit(__doc__.split("Usage: ")[1])
    version, out = sys.argv[1], sys.argv[2]
    if os.path.exists(out) and os.listdir(out):
        sys.exit(f"{out} is not empty")

    os.makedirs(os.path.join(out, ".claude-plugin"), exist_ok=True)
    with open("plugin/plugin.json", encoding="utf-8") as f:
        manifest = json.load(f)
    manifest = {"name": manifest.pop("name"), "version": version, **manifest}
    with open(os.path.join(out, ".claude-plugin", "plugin.json"), "w", encoding="utf-8") as f:
        f.write(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    shutil.copyfile("site/static/icon-512.png", os.path.join(out, ".claude-plugin", "icon.png"))

    for d in ("skills", "knowledge"):
        shutil.copytree(d, os.path.join(out, d))
    for src, dst in (("glossario.md", "glossario.md"), ("LICENSE", "LICENSE"), ("plugin/README.md", "README.md")):
        shutil.copyfile(src, os.path.join(out, dst))

    problems = []
    for root, _, files in os.walk(out):
        for name in files:
            path = os.path.join(root, name)
            rel = os.path.relpath(path, out)
            if rel == os.path.join(".claude-plugin", "icon.png"):
                continue
            if name != "LICENSE" and not name.endswith(TEXT):
                problems.append(f"{rel}: not text, the directory holds it for review")
            elif os.path.getsize(path) > MAX_TEXT:
                problems.append(f"{rel}: over 256 KiB, the directory holds it for review")
    if problems:
        sys.exit("\n".join(problems))
    print(f"plugin {version} in {out}")


if __name__ == "__main__":
    main()
