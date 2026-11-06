#!/usr/bin/env python3
"""Checks knowledge/incentives.json.

Fails when an entry has no id, a repeated id, no pt+en text, no https source.url or source.name,
no checkedAt, a bad date, validTo before validFrom, a checkedAt in the future, a Fundo Ambiental
entry without series/edition, or a municipal entry without municipality, benefit and official.url.

Warns (does not fail) about entries still in force whose checkedAt is older than --max-age days:
those are the ones a consumer marks as stale.

Usage: scripts/check-knowledge.py [--max-age DAYS] [--today YYYY-MM-DD]
"""
import argparse
import datetime as dt
import json
import sys

KINDS = {"apoio", "fiscal", "municipal"}
BENEFITS = {"isenção", "desconto"}


def date(value):
    return dt.date.fromisoformat(value) if value else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default="knowledge/incentives.json")
    ap.add_argument("--max-age", type=int, default=180)
    ap.add_argument("--today", default=dt.date.today().isoformat())
    args = ap.parse_args()
    today = date(args.today)

    data = json.load(open(args.file, encoding="utf-8"))
    entries = data.get("entries")
    if not isinstance(entries, list) or not entries:
        print(f"{args.file}: 'entries' must be a non-empty list")
        return 1

    errors, warnings, seen = [], [], set()
    for i, e in enumerate(entries):
        eid = e.get("id") or f"#{i}"
        err = lambda msg: errors.append(f"{eid}: {msg}")
        if not e.get("id"):
            err("missing id")
        elif eid in seen:
            err("repeated id")
        seen.add(eid)
        kind = e.get("kind")
        if kind not in KINDS:
            err(f"kind '{kind}' not in {sorted(KINDS)}")
        text = e.get("text") or {}
        if not (isinstance(text, dict) and text.get("pt") and text.get("en")):
            err("text needs pt and en")
        src = e.get("source") or {}
        if not str(src.get("url", "")).startswith("https://"):
            err("source.url missing or not https")
        if not src.get("name"):
            err("source.name missing")
        try:
            checked = date(e.get("checkedAt"))
            vfrom, vto = date(e.get("validFrom")), date(e.get("validTo"))
        except (TypeError, ValueError) as ex:
            err(f"bad date: {ex}")
            continue
        if not checked:
            err("checkedAt missing")
            continue
        if checked > today:
            err(f"checkedAt {checked} is in the future")
        if vfrom and vto and vto < vfrom:
            err(f"validTo {vto} before validFrom {vfrom}")
        if str(e.get("series", "")).startswith("fundo-ambiental") or eid.startswith("fa-"):
            if not e.get("series") or not e.get("edition"):
                err("Fundo Ambiental entry needs series and edition")
        if kind == "municipal":
            if not e.get("municipality"):
                err("municipal entry needs municipality")
            if e.get("benefit") not in BENEFITS:
                err(f"benefit must be one of {sorted(BENEFITS)}")
            if not str((e.get("official") or {}).get("url", "")).startswith("https://"):
                err("municipal entry needs an https official.url")
        in_force = not vto or vto >= today
        if in_force and (today - checked).days > args.max_age:
            warnings.append(f"{eid}: in force, checkedAt {checked} older than {args.max_age} days")

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"{args.file}: {e}")
    if errors:
        return 1
    closed = sum(1 for e in entries if e.get("validTo") and date(e["validTo"]) < today)
    print(f"Knowledge: {len(entries)} entries valid ({closed} closed, {len(entries) - closed} in force)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
