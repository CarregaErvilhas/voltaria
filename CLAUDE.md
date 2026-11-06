# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Voltaria is a set of Agent Skills in pt-PT about electric mobility in Portugal, written **for agents,
never as pages for humans**. It is the single content source for two consumers, and it doesn't know
about either of them:

- the **ohmigo MCP** (`CarregaErvilhas/ohmigo-mcp`), which serves the skills through `get_guide` and the facts in `knowledge/` through `get_facts`;
- an **agent that rebuilds ocarroeletrico.com** from each Voltaria release. Its system prompt lives in the site's repo, not here.

Each consumer decides how to present the content and in which language. Decisions and their dates
are recorded in the plan, `docs/o-ohmigo-tem-sido-shiny-sloth.md`. Read it before changing
structure, licensing or how sources are handled.

**Semver:** updating facts is a patch, a new skill is a minor, and renaming a skill or changing the
fact format is a major, because skill names are the `get_guide` enum in ohmigo. A `vX.Y.Z` tag
triggers `release.yml`, which publishes one zip per skill with the LICENSE.

## Commands

Run from the repo root. The checks need only `sh` and `python3` (stdlib). CI runs the first three in
`checks.yml` on every PR and on `main`:

```sh
scripts/check-skills.py                  # frontmatter, name = folder, no prices, glossary "Evitar" terms
scripts/check-knowledge.py               # knowledge/incentives.json structure and dates
scripts/check-sources.sh                 # every skill's "## Fontes" has legislation + a standard
scripts/check-sources.sh --check-links   # also requests every URL (slow, network)
scripts/check-dco.sh origin/main..HEAD   # every commit signed off by its author (DCO, as in dco.yml)
```

`check-knowledge.py --today YYYY-MM-DD --max-age DAYS` changes the reference date and the staleness
window (default 180 days; stale entries only warn).

Evals (`evals/README.md` has the detail; anything except `check` costs money):

```sh
python3 evals/run.py check                           # validate questions.json against skills/, free
python3 evals/run.py run --smoke --dry-run           # cost estimate only
python3 evals/run.py run --skill sub-cpe             # one skill's questions, without vs with skill
python3 evals/run.py run --ids sub-01,sub-04         # specific questions
python3 evals/run.py ablate --skill sub-cpe --cited-only
python3 evals/run.py run --backend mock --smoke      # pipeline test, no model calls
```

The default backend `cli` runs a nested `claude -p` (no tools, no MCP, no CLAUDE.md) in an empty
folder, and needs `claude auth login`. Results are cached in `evals/.cache/`, so re-runs are free.
Each command refuses to start above `budget_usd` in `evals/config.json` unless you pass `--budget`.

## How the pieces constrain each other

- **`glossario.md` is enforced.** `check-skills.py` parses its table, and any term in the "Evitar"
  column (split by `;`) fails every skill that uses it. URLs, `code` spans and the `## Fontes`
  section are exempt. Adding an "Evitar" term can break skills that already exist: run the check.
- **Section titles are an API.** Each eval question's `source` is `skill#Exact section title`, and
  ablation uses it. Renaming a `##`/`###` heading breaks `evals/run.py check` until
  `evals/questions.json` is updated.
- **Prices live outside the skills.** `check-skills.py` rejects € amounts in skill text. Prices come
  from ohmigo's tools; dated amounts (incentives, tax limits) go in `knowledge/incentives.json`.
  The evals inject those facts into `incentivos` and `empresas-e-frotas` (`facts_for_skills` in
  `evals/config.json`).

## Skill format

`skills/<name>/SKILL.md`, where `name` uses lowercase letters, digits and hyphens and equals the
folder name. The frontmatter `description` must be double-quoted and at most 1024 characters (an
unquoted `: ` breaks YAML). The existing skills share this shape:

- Opening line addressed to the assistant ("Escrito para ti, o assistente. Responde na língua do
  utilizador…"), then `## Regras` at the top.
- Topic sections, often ending with `## Confusões a corrigir`.
- `## Fontes` last, split into `### Legislação`, `### Normas e standards` and `### Outras fontes`.
  `check-sources.sh` requires a DRE/Diário da República or EUR-Lex link, and a link to a standards
  body (ISO, IEC, UNECE, OCA, EVRoaming, DATEX II, Genorma). For DR links use the ELI codes
  `dec-lei` and `port`. The long forms redirect to an error page that returns 200.
- When something is covered better elsewhere, point to the other skill by name instead of
  duplicating it.
- No prices and no counts (stations, market shares, sales). Cite the article of the law, not a
  summary of it.

## Sources and content rules

- **Third-party text is a source, not text.** Rewrite in our own words. Copying requires written
  permission from the author, recorded in `docs/fontes/<author>.md` with what came from each page and
  where it went. The UVE has given permission, but we still rewrite, because it doesn't cover
  relicensing its text under CC-BY-4.0. The UVE manual is CC BY 4.0 and can be adapted, with credit.
- **Mark who is speaking.** A point taken from a third party carries an inline marker such as
  `[UVE, manual]`, `[DGEG, FAQ …]` or `[MOBI.E, …]`, so the agent presents it as that body's position
  rather than as law. Ministers' statements reported in the press are `[imprensa]` and are never a rule.
- **Incentives are official sources only** (Fundo Ambiental, AT, Diário da República). The only
  exception is `kind: "municipal"` entries: their `source` is the UVE parking list, and the town
  hall's link goes in `official`.
- **`knowledge/incentives.json`** (`schema: 2`). Every entry has `id`, `kind`
  (`apoio`/`fiscal`/`municipal`/`mercado`), `text.pt` + `text.en`, an https `source{url,name}`,
  `checkedAt`, and `validFrom`/`validTo`.
  - Fundo Ambiental entries also need `series` + `edition`.
  - Closed entries stay as history and are never presented as open.
  - `status: "anunciado"` marks a support the government announced that has no notice yet. It doesn't
    count as in force, and any `validFrom` it has must be in the future.
  - Bump `checkedAt` only when the source was actually re-read.

## Workflow

- Licence: content (skills, `knowledge/`, `glossario.md`, other text) is CC-BY-4.0; code (`scripts/`,
  `evals/`, `.github/`) is MIT.
- Every commit needs `git commit -s`. `dco.yml` rejects PRs with commits that aren't signed off.
- Everything goes in by PR, reviewed by CODEOWNERS. Only squash and rebase merges are allowed.
- Several sessions often work on this repo in parallel. Rebase on `main` before pushing, and expect
  conflicts in the shared files (`glossario.md`, the plan, `evals/questions.json`).
