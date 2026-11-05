#!/bin/sh
# Fails if a skill has no sources, or has sources but no legislation and no standard.
# Usage:
#   scripts/check-sources.sh              structural check (fast, offline)
#   scripts/check-sources.sh --check-links  also requests every https link (best effort)
#
# Every skills/*/SKILL.md must have a "## Fontes" section with:
#   - at least one https link,
#   - at least one link to Portuguese or EU legislation,
#   - at least one link to a standards body (ISO, IEC, UNECE, OCA, EVRoaming, DATEX II).
set -eu

check_links=0
[ "${1:-}" = "--check-links" ] && check_links=1

legislation='data\.dre\.pt|diariodarepublica\.pt|eur-lex\.europa\.eu'
standards='iso\.org|webstore\.iec\.ch|unece\.org|openchargealliance\.org|evroaming\.org|datex2\.eu|genorma\.com'

bad=0
tmp=$(mktemp)
trap 'rm -f "$tmp"' EXIT

for f in skills/*/SKILL.md; do
  # Only the text after the last "## Fontes" heading counts.
  if ! grep -q '^## Fontes' "$f"; then
    echo "$f: missing '## Fontes' section"
    bad=1
    continue
  fi
  sed -n '/^## Fontes/,$p' "$f" > "$tmp"

  if ! grep -q 'https://' "$tmp"; then
    echo "$f: '## Fontes' has no https link"
    bad=1
  fi
  if ! grep -Eq "$legislation" "$tmp"; then
    echo "$f: '## Fontes' has no link to legislation (DRE, Diário da República or EUR-Lex)"
    bad=1
  fi
  if ! grep -Eq "$standards" "$tmp"; then
    echo "$f: '## Fontes' has no link to a standard (ISO, IEC, UNECE, OCA, EVRoaming, DATEX II)"
    bad=1
  fi
done

if [ "$check_links" = 1 ]; then
  for f in skills/*/SKILL.md; do
    sed -n '/^## Fontes/,$p' "$f" | grep -Eo 'https://[^ )>,"]+' | sed 's/[.;,`]$//' | sort -u > "$tmp"
    while read -r url; do
      code=$(curl -s -o /dev/null -w '%{http_code}' -L --max-time 30 "$url" || true)
      [ -n "$code" ] || code=000
      if [ "$code" = 000 ]; then
        # Slow or heavy endpoints (the MOBI.E NAP dumps) get one longer retry.
        code=$(curl -s -o /dev/null -w '%{http_code}' -L --max-time 90 "$url" || true)
        [ -n "$code" ] || code=000
      fi
      case "$code" in
        # 202/403/405: EUR-Lex, ISO and UNECE reject curl's user agent; the page exists.
        2*|3*|403|405) ;;
        *) echo "$f: $code $url"; bad=1 ;;
      esac
    done < "$tmp"
  done
fi

if [ "$bad" = 0 ]; then
  echo "Fontes: every skill has sources, legislation and standards links"
else
  exit 1
fi
