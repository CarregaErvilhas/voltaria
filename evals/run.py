#!/usr/bin/env python3
"""Eval harness for the Voltaria skills: does a skill (or one section of it) change the answer?

Subcommands (run from the repo root):
  check                    validate questions.json against skills/ (no model calls)
  sections --skill S       list the ##/### sections of a skill, as ablation sees them
  run [--smoke|--ids|--skill|--category] [--reps N]
                           answer each question without and with its skills, grade, report
  ablate --skill S [--depth 2|3] [--reps N]
                           remove one section at a time and re-run that skill's questions
  report RUN_DIR           re-render report.md from a run's results.json

Every command that calls a model prints an estimate first and refuses to start when it exceeds
--budget (default: config.json budget_usd). --dry-run stops after the estimate.

Backends: "cli" (claude -p, headless, no tools, no MCP, no CLAUDE.md) or "api" (Anthropic SDK,
reads ANTHROPIC_API_KEY from the environment) or "mock" (no calls, for testing the plumbing).
Stdlib only, except the "api" backend, which needs `pip install anthropic`.
"""
import argparse
import concurrent.futures as cf
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVALS = ROOT / "evals"
CACHE = EVALS / ".cache"
RUNS = EVALS / "runs"
CATS = ("a", "b", "c", "d", "e")

# ---------------------------------------------------------------- loading


def load_config():
    return json.loads((EVALS / "config.json").read_text(encoding="utf-8"))


def load_questions():
    return json.loads((EVALS / "questions.json").read_text(encoding="utf-8"))["questions"]


def skill_text(name):
    return (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")


def all_skills():
    return sorted(p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md"))


def norm_rubric(q):
    """must_not items may be strings or {text, regex}; return lists of dicts."""
    mn = []
    for it in q.get("must_not", []):
        mn.append({"text": it, "regex": None} if isinstance(it, str) else {"text": it["text"], "regex": it.get("regex")})
    return [{"text": m} for m in q["must"]], mn


# ---------------------------------------------------------------- sections


def parse_sections(text):
    """Return the ablatable sections of a SKILL.md.

    Each section: {id, level, title, start, end} with line indices [start, end). A `##` section
    spans its `###` children. Skips the frontmatter, the `#` title, and `## Fontes` with its children.
    """
    lines = text.split("\n")
    heads, fence = [], False
    for i, line in enumerate(lines):
        if line.startswith("```"):
            fence = not fence
        if fence:
            continue
        m = re.match(r"^(##+)\s+(.*\S)\s*$", line)
        if m and len(m.group(1)) in (2, 3):
            heads.append((i, len(m.group(1)), m.group(2)))
    out, parent = [], None
    for k, (i, lvl, title) in enumerate(heads):
        end = len(lines)
        for j, l2, _ in heads[k + 1:]:
            if l2 <= lvl:
                end = j
                break
        if lvl == 2:
            parent = title
        if (lvl == 2 and title == "Fontes") or (lvl == 3 and parent == "Fontes"):
            continue
        sid = title if lvl == 2 else f"{parent} > {title}"
        out.append({"id": sid, "level": lvl, "title": title, "start": i, "end": end})
    return out


def remove_section(text, sec):
    lines = text.split("\n")
    return "\n".join(lines[: sec["start"]] + lines[sec["end"]:])


def source_matches(src, skill, sec):
    """Does a question's `source` entry ("skill#Heading") point at this section or inside it?"""
    s, _, head = src.partition("#")
    if s != skill:
        return False
    if head == sec["title"]:
        return True
    if sec["level"] == 3:
        return False
    # a ## section also covers sources naming one of its ### children
    child = sec.get("children", [])
    return head in child


# ---------------------------------------------------------------- prompts


def facts_block(skills, cfg):
    want = [s for s in skills if s in cfg.get("facts_for_skills", {})]
    if not want:
        return ""
    data = json.loads((ROOT / "knowledge" / "incentives.json").read_text(encoding="utf-8"))
    keep = []
    for e in data["entries"]:
        row = {k: e[k] for k in ("id", "kind", "status", "series", "edition", "municipality", "validFrom",
                                 "validTo", "checkedAt") if k in e and e[k] is not None}
        row["text"] = e["text"]["pt"]
        row["source"] = e.get("source", {}).get("url")
        if e.get("official"):
            row["official"] = e["official"]
        keep.append(row)
    body = "\n".join(json.dumps(r, ensure_ascii=False) for r in keep)
    return ("\n\n<factos origem=\"knowledge/incentives.json\" nota=\"o que ev_rules_portugal com topic incentives devolveria\">\n"
            + body + "\n</factos>")


def base_system(cfg):
    return (
        "És um assistente que responde a perguntas sobre mobilidade elétrica em Portugal, em português "
        f"de Portugal. A data de hoje é {cfg['today']}.\n"
        "Na aplicação real terias as ferramentas do ohmigo (find_chargers, lookup_charger, "
        "estimate_charging_cost, find_cheapest_charging, list_ceme_tariffs, ev_rules_portugal). Nesta conversa não as "
        "podes chamar: quando precisarias de uma, diz qual chamarias e com que argumentos, e responde com o "
        "que sabes."
    )


def skill_system(cfg, skills, overrides=None):
    overrides = overrides or {}
    parts = [base_system(cfg), "\n\nUsa as skills seguintes, que têm prioridade sobre o que sabes de memória."]
    for s in skills:
        parts.append(f"\n\n<skill name=\"{s}\">\n{overrides.get(s, skill_text(s))}\n</skill>")
    parts.append("\n\n<glossario>\n" + (ROOT / "glossario.md").read_text(encoding="utf-8") + "\n</glossario>")
    parts.append(facts_block(skills, cfg))
    return "".join(parts)


JUDGE_SYSTEM = """You grade answers from an assistant about electric mobility in Portugal against a rubric.
Today is {today}. The rubric is the ground truth, even where it disagrees with what you know.

For each `must` item: pass=true only if the answer clearly conveys it (paraphrase, other wording or
language is fine; vague, implicit or contradicted is a fail). An item with "ou"/"or" alternatives
passes if any alternative holds. Behaviour items ("não dá...", "indica que usaria a ferramenta...")
are judged on what the answer does.
For each `must_not` item: violated=true if the answer asserts it, even hedged. Mentioning a wrong
claim only to correct it is NOT a violation.
Do not reward or penalise anything outside the rubric. Evidence: a short quote (max ~20 words) or
"ausente". Answer only with the JSON object."""

JUDGE_SCHEMA = {
    "type": "object",
    "properties": {
        "must": {"type": "array", "items": {"type": "object", "properties": {
            "i": {"type": "integer"}, "pass": {"type": "boolean"}, "evidence": {"type": "string"}},
            "required": ["i", "pass", "evidence"], "additionalProperties": False}},
        "must_not": {"type": "array", "items": {"type": "object", "properties": {
            "i": {"type": "integer"}, "violated": {"type": "boolean"}, "evidence": {"type": "string"}},
            "required": ["i", "violated", "evidence"], "additionalProperties": False}},
    },
    "required": ["must", "must_not"],
    "additionalProperties": False,
}


def judge_user(q, answer):
    must, mn = norm_rubric(q)
    r = ["Pergunta:", q["question"], "", "must:"]
    r += [f"  {i}. {m['text']}" for i, m in enumerate(must)]
    r += ["must_not:"] + ([f"  {i}. {m['text']}" for i, m in enumerate(mn)] or ["  (nenhum)"])
    r += ["", "Resposta a avaliar:", "<<<", answer, ">>>"]
    return "\n".join(r)


# ---------------------------------------------------------------- backends


def _child_env():
    env = dict(os.environ)
    for k in list(env):
        if k == "CLAUDECODE" or k.startswith(("CLAUDE_CODE_", "CLAUDE_AGENT_SDK_")):
            env.pop(k)
    return env


class CliBackend:
    """`claude -p` with everything off: no tools, no MCP, no settings, no CLAUDE.md, empty cwd."""

    def __init__(self, cfg):
        self.cfg = cfg
        self.exe = shutil.which("claude")
        if not self.exe:
            sys.exit("claude CLI not found on PATH")
        CACHE.mkdir(parents=True, exist_ok=True)
        self.cwd = tempfile.mkdtemp(prefix="cwd-", dir=CACHE)

    def call(self, model, effort, system, user, schema=None):
        cmd = [self.exe, "-p", "--model", model, "--effort", effort, "--system-prompt", system,
               "--tools", "", "--strict-mcp-config", "--setting-sources", "", "--safe-mode",
               "--disable-slash-commands", "--no-session-persistence", "--output-format", "json"]
        if schema:
            cmd += ["--json-schema", json.dumps(schema)]
        cmd.append(user)
        p = subprocess.run(cmd, capture_output=True, text=True, cwd=self.cwd, env=_child_env(),
                           timeout=self.cfg.get("timeout_s", 300))
        try:
            d = json.loads(p.stdout)
        except json.JSONDecodeError:
            raise RuntimeError(f"claude -p: no JSON (exit {p.returncode}): {p.stderr.strip()[:300]}")
        if d.get("is_error"):
            raise RuntimeError(f"claude -p: {str(d.get('result'))[:300]}")
        u = d.get("usage", {})
        out = {"text": d.get("result", ""), "cost": d.get("total_cost_usd", 0.0),
               "in": u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0),
               "out": u.get("output_tokens", 0)}
        if schema:
            out["json"] = d.get("structured_output") or _extract_json(out["text"])
        return out


class ApiBackend:
    def __init__(self, cfg):
        try:
            import anthropic  # noqa: F401
        except ImportError:
            sys.exit("backend 'api' needs the Anthropic SDK: pip install anthropic")
        import anthropic
        self.cfg = cfg
        self.client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY (or an `ant auth login` profile)

    def call(self, model, effort, system, user, schema=None):
        oc = {"effort": effort}
        if schema:
            oc["format"] = {"type": "json_schema", "schema": schema}
        r = self.client.messages.create(
            model=model, max_tokens=16000,
            system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
            messages=[{"role": "user", "content": user}], output_config=oc)
        if r.stop_reason == "refusal":
            raise RuntimeError("refusal")
        text = "".join(b.text for b in r.content if b.type == "text")
        u = r.usage
        p = self.cfg["prices_usd_per_mtok"][model]
        cr, cw = u.cache_read_input_tokens or 0, u.cache_creation_input_tokens or 0
        cost = (u.input_tokens * p["input"] + cr * p["cache_read"] + cw * p["cache_write"]
                + u.output_tokens * p["output"]) / 1e6
        out = {"text": text, "cost": cost, "in": u.input_tokens + cr + cw, "out": u.output_tokens}
        if schema:
            out["json"] = json.loads(text)
        return out


class MockBackend:
    """No model calls. Answers echo which arm they came from; the judge passes items by hash."""

    def __init__(self, cfg):
        self.cfg = cfg

    def call(self, model, effort, system, user, schema=None):
        if not schema:
            arm = "skill" if "<skill name=" in system else "base"
            return {"text": f"[mock {arm} {hashlib.sha1(system.encode()).hexdigest()[:6]}] {user[:60]}",
                    "cost": 0.0, "in": len(system + user) // 4, "out": 50}
        n_must = len(re.findall(r"^  \d+\. ", user.split("must_not:")[0], re.M))
        n_mn = len(re.findall(r"^  \d+\. ", user.split("must_not:")[1], re.M))
        h = int(hashlib.sha1(user.encode()).hexdigest(), 16)
        boost = "[mock skill" in user
        res = {"must": [{"i": i, "pass": bool((h >> i) & 1) or boost, "evidence": "mock"} for i in range(n_must)],
               "must_not": [{"i": i, "violated": bool((h >> (i + 20)) & 1) and not boost, "evidence": "mock"} for i in range(n_mn)]}
        return {"text": json.dumps(res), "cost": 0.0, "in": len(user) // 4, "out": 80, "json": res}


def _extract_json(s):
    m = re.search(r"\{.*\}", s, re.S)
    if not m:
        raise RuntimeError("judge returned no JSON")
    return json.loads(m.group(0))


def make_backend(name, cfg):
    return {"cli": CliBackend, "api": ApiBackend, "mock": MockBackend}[name](cfg)


# ---------------------------------------------------------------- cache, budget


def h(*parts):
    return hashlib.sha256(json.dumps(parts, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:24]


class Store:
    """Answers and grades on disk, keyed by everything that changes them. Re-runs are free."""

    def __init__(self, backend_name):
        self.dir = CACHE / backend_name
        (self.dir / "answers").mkdir(parents=True, exist_ok=True)
        (self.dir / "grades").mkdir(parents=True, exist_ok=True)

    def get(self, kind, key):
        p = self.dir / kind / f"{key}.json"
        return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None

    def put(self, kind, key, val):
        (self.dir / kind / f"{key}.json").write_text(json.dumps(val, ensure_ascii=False, indent=1), encoding="utf-8")

    def avg_cost(self, kind, arm=None):
        costs = []
        for p in (self.dir / kind).glob("*.json"):
            d = json.loads(p.read_text(encoding="utf-8"))
            if arm is None or d.get("arm") == arm:
                costs.append(d.get("cost", 0.0))
        return statistics.mean(costs) if len(costs) >= 3 else None


class Budget:
    def __init__(self, limit):
        self.limit, self.spent, self.lock = limit, 0.0, threading.Lock()

    def add(self, c):
        with self.lock:
            self.spent += c or 0.0
            if self.spent > self.limit:
                raise BudgetExceeded(f"spent {self.spent:.2f} USD > budget {self.limit:.2f} USD")


class BudgetExceeded(RuntimeError):
    pass


# ---------------------------------------------------------------- core


class Harness:
    def __init__(self, cfg, backend_name, budget, workers):
        self.cfg, self.bname = cfg, backend_name
        self._backend = None
        self.store = Store(backend_name)
        self.budget = Budget(budget)
        self.workers = workers

    @property
    def backend(self):
        if self._backend is None:  # created on first call, so --dry-run needs no credentials
            self._backend = make_backend(self.bname, self.cfg)
        return self._backend

    # one task = (question, arm, system prompt, rep)
    def answer_key(self, system, q, rep):
        return h(self.cfg["answer_model"], self.cfg["answer_effort"], system, q["question"], rep)

    def grade_key(self, q, answer):
        must, mn = norm_rubric(q)
        return h(self.cfg["judge_model"], self.cfg["judge_effort"], JUDGE_SYSTEM, q["question"], must, mn, answer)

    def estimate(self, tasks):
        """USD for the tasks not in cache. Uses measured averages once the cache has some."""
        e, p = self.cfg["estimate"], self.cfg["prices_usd_per_mtok"]
        pa, pj = p[self.cfg["answer_model"]], p[self.cfg["judge_model"]]
        avg_j = self.store.avg_cost("grades")
        total, n_ans, n_grade = 0.0, 0, 0
        for t in tasks:
            akey = self.answer_key(t["system"], t["q"], t["rep"])
            cached = self.store.get("answers", akey)
            if cached is None:
                n_ans += 1
                avg = self.store.avg_cost("answers", t["arm"] if t["arm"] in ("base", "skill") else "skill")
                tok_in = len(t["system"] + t["q"]["question"]) / e["chars_per_token"]
                total += avg if avg is not None else (tok_in * pa["input"] + e["answer_output_tokens"] * pa["output"]) / 1e6
            if cached is None or self.store.get("grades", self.grade_key(t["q"], cached["text"])) is None:
                n_grade += 1
                tok_in = (len(JUDGE_SYSTEM) + 6000) / e["chars_per_token"]
                total += avg_j if avg_j is not None else (tok_in * pj["input"] + e["judge_output_tokens"] * pj["output"]) / 1e6
        return total, n_ans, n_grade

    def run_task(self, t):
        q = t["q"]
        akey = self.answer_key(t["system"], q, t["rep"])
        ans = self.store.get("answers", akey)
        if ans is None:
            r = self.backend.call(self.cfg["answer_model"], self.cfg["answer_effort"], t["system"], q["question"])
            self.budget.add(r["cost"])
            ans = {"qid": q["id"], "arm": t["arm"], "rep": t["rep"], "text": r["text"], "cost": r["cost"],
                   "in": r["in"], "out": r["out"], "model": self.cfg["answer_model"]}
            self.store.put("answers", akey, ans)
        gkey = self.grade_key(q, ans["text"])
        g = self.store.get("grades", gkey)
        if g is None:
            r = self.backend.call(self.cfg["judge_model"], self.cfg["judge_effort"],
                                  JUDGE_SYSTEM.format(today=self.cfg["today"]), judge_user(q, ans["text"]), JUDGE_SCHEMA)
            self.budget.add(r["cost"])
            g = {"judge": r["json"], "cost": r["cost"], "model": self.cfg["judge_model"]}
            self.store.put("grades", gkey, g)
        return {"qid": q["id"], "arm": t["arm"], "rep": t["rep"], "answer": ans["text"],
                **score(q, ans["text"], g["judge"])}

    def run_all(self, tasks, label):
        out, errors = [], []
        with cf.ThreadPoolExecutor(max_workers=self.workers) as ex:
            futs = {ex.submit(self.run_task, t): t for t in tasks}
            for n, f in enumerate(cf.as_completed(futs), 1):
                t = futs[f]
                try:
                    out.append(f.result())
                except BudgetExceeded as e:
                    for g in futs:
                        g.cancel()
                    print(f"\nstopped: {e}", file=sys.stderr)
                    break
                except Exception as e:  # keep going; report the failure
                    errors.append({"qid": t["q"]["id"], "arm": t["arm"], "error": str(e)[:300]})
                if sys.stderr.isatty():
                    print(f"\r{label}: {n}/{len(tasks)}  spent {self.budget.spent:.2f} USD", end="", file=sys.stderr)
                elif n % 20 == 0 or n == len(tasks):
                    print(f"{label}: {n}/{len(tasks)}  spent {self.budget.spent:.2f} USD", file=sys.stderr)
        if sys.stderr.isatty():
            print(file=sys.stderr)
        return out, errors


def score(q, answer, judge):
    must, mn = norm_rubric(q)
    passed = {m["i"]: m["pass"] for m in judge.get("must", [])}
    viol = {m["i"]: m["violated"] for m in judge.get("must_not", [])}
    ev_m = {m["i"]: m.get("evidence", "") for m in judge.get("must", [])}
    ev_n = {m["i"]: m.get("evidence", "") for m in judge.get("must_not", [])}
    must_res = [{"text": m["text"], "pass": bool(passed.get(i, False)), "evidence": ev_m.get(i, "")} for i, m in enumerate(must)]
    mn_res = []
    for i, m in enumerate(mn):
        det = bool(m["regex"] and re.search(m["regex"], answer, re.I))
        mn_res.append({"text": m["text"], "violated": bool(viol.get(i, False)) or det, "regex_hit": det,
                       "evidence": ev_n.get(i, "")})
    n = len(must_res) + len(mn_res)
    good = sum(r["pass"] for r in must_res) + sum(not r["violated"] for r in mn_res)
    return {"score": good / n if n else 0.0, "must": must_res, "must_not": mn_res}


# ---------------------------------------------------------------- selection


def select(questions, cfg, a):
    qs = questions
    if a.smoke:
        qs = [q for q in qs if q["id"] in cfg["smoke_ids"]]
    if a.ids:
        want = set(a.ids.split(","))
        qs = [q for q in qs if q["id"] in want]
    if a.skill:
        qs = [q for q in qs if a.skill in q["skills"]]
    if a.category:
        qs = [q for q in qs if q["category"] in a.category]
    if a.limit:
        qs = qs[: a.limit]
    return qs


def preflight(hs, tasks, a):
    est, n_ans, n_grade = hs.estimate(tasks)
    budget = hs.budget.limit
    print(f"{len(tasks)} tasks: {n_ans} answers and {n_grade} grades not cached. "
          f"Estimated cost: {est:.2f} USD (budget {budget:.2f} USD, backend {hs.bname}).")
    if hs.bname == "cli":
        print("  (claude -p on a subscription reports API-equivalent cost; it draws on plan usage, not billing)")
    sys.stdout.flush()
    if a.dry_run:
        sys.exit(0)
    if est > budget:
        sys.exit(f"Estimate above budget. Re-run with --budget {est * 1.3:.0f} to go ahead.")


def new_run_dir(kind):
    d = RUNS / f"{dt.datetime.now().strftime('%Y%m%d-%H%M%S')}-{kind}"
    d.mkdir(parents=True, exist_ok=True)
    return d


# ---------------------------------------------------------------- commands


def cmd_check(a):
    cfg, qs = load_config(), load_questions()
    skills, problems = all_skills(), []
    heads = {s: {sec["title"] for sec in parse_sections(skill_text(s))} for s in skills}
    ids = [q["id"] for q in qs]
    for d in {i for i in ids if ids.count(i) > 1}:
        problems.append(f"duplicate id {d}")
    for q in qs:
        for k in ("id", "skills", "category", "question", "must"):
            if k not in q:
                problems.append(f"{q.get('id')}: missing {k}")
        if q.get("category") not in CATS:
            problems.append(f"{q['id']}: bad category {q.get('category')}")
        for s in q.get("skills", []):
            if s not in skills:
                problems.append(f"{q['id']}: unknown skill {s}")
        if not q.get("must"):
            problems.append(f"{q['id']}: empty must")
        for src in q.get("source", []):
            s, _, head = src.partition("#")
            if s not in skills or head not in heads.get(s, ()):
                problems.append(f"{q['id']}: source '{src}' is not a heading of skills/{s}/SKILL.md")
        for it in q.get("must_not", []):
            if isinstance(it, dict) and it.get("regex"):
                try:
                    re.compile(it["regex"])
                except re.error as e:
                    problems.append(f"{q['id']}: bad regex: {e}")
    for i in cfg["smoke_ids"]:
        if i not in ids:
            problems.append(f"smoke id {i} not in questions.json")
    cover = {s: sum(s in q["skills"] for q in qs) for s in skills}
    for s, n in cover.items():
        if n == 0:
            problems.append(f"skill {s} has no questions")
    for p in problems:
        print(p)
    cats = {c: sum(q["category"] == c for q in qs) for c in CATS}
    print(f"{len(qs)} questions; per skill: " + ", ".join(f"{s} {n}" for s, n in cover.items()))
    print("per category: " + ", ".join(f"{c} {n}" for c, n in cats.items()))
    return 1 if problems else 0


def cmd_sections(a):
    secs = parse_sections(skill_text(a.skill))
    qs = [q for q in load_questions() if a.skill in q["skills"]]
    for sec in secs:
        _children(secs, sec)
        n = sum(any(source_matches(s, a.skill, sec) for s in q.get("source", [])) for q in qs)
        lines = sec["end"] - sec["start"]
        print(f"{'  ' if sec['level'] == 3 else ''}{sec['id']}  ({lines} lines, {n} questions cite it)")
    return 0


def _children(secs, sec):
    if sec["level"] == 2:
        sec["children"] = [s["title"] for s in secs if s["level"] == 3 and sec["start"] < s["start"] < sec["end"]]
    return sec


def cmd_run(a):
    cfg = load_config()
    qs = select(load_questions(), cfg, a)
    if not qs:
        sys.exit("no questions selected")
    hs = Harness(cfg, a.backend or cfg["backend"], a.budget or cfg["budget_usd"], a.workers or cfg["concurrency"])
    tasks = []
    for q in qs:
        for rep in range(a.reps):
            tasks.append({"q": q, "arm": "base", "rep": rep, "system": base_system(cfg)})
            tasks.append({"q": q, "arm": "skill", "rep": rep, "system": skill_system(cfg, q["skills"])})
    preflight(hs, tasks, a)
    results, errors = hs.run_all(tasks, "run")
    d = new_run_dir("smoke" if a.smoke else "run")
    meta = {"kind": "run", "cfg": cfg, "backend": hs.bname, "reps": a.reps, "spent_usd": hs.budget.spent,
            "questions": [q["id"] for q in qs], "errors": errors}
    (d / "results.json").write_text(json.dumps({"meta": meta, "results": results}, ensure_ascii=False, indent=1), encoding="utf-8")
    (d / "report.md").write_text(render_run(meta, results, load_questions()), encoding="utf-8")
    print(f"report: {d / 'report.md'}  (spent {hs.budget.spent:.2f} USD, {len(errors)} errors)")
    return 1 if errors else 0


def cmd_ablate(a):
    cfg = load_config()
    qs = [q for q in select(load_questions(), cfg, a) if a.skill in q["skills"]]
    if not qs:
        sys.exit(f"no questions for skill {a.skill}")
    hs = Harness(cfg, a.backend or cfg["backend"], a.budget or cfg["budget_usd"], a.workers or cfg["concurrency"])
    full = skill_text(a.skill)
    all_secs = parse_sections(full)
    secs = [_children(all_secs, s) for s in all_secs if s["level"] <= a.depth]
    tasks = []
    for q in qs:
        for rep in range(a.reps):
            tasks.append({"q": q, "arm": "skill", "variant": "__full__", "rep": rep, "system": skill_system(cfg, q["skills"])})
            for s in secs:
                if a.cited_only and not any(source_matches(x, a.skill, s) for x in q.get("source", [])):
                    continue
                sysp = skill_system(cfg, q["skills"], {a.skill: remove_section(full, s)})
                tasks.append({"q": q, "arm": "ablate", "variant": s["id"], "rep": rep, "system": sysp})
    preflight(hs, tasks, a)
    _, errors = hs.run_all(tasks, f"ablate {a.skill}")
    # read every task back from the cache, so each row keeps its variant
    rows = []
    for t in tasks:
        ans = hs.store.get("answers", hs.answer_key(t["system"], t["q"], t["rep"]))
        if not ans:
            continue
        g = hs.store.get("grades", hs.grade_key(t["q"], ans["text"]))
        if not g:
            continue
        rows.append({"qid": t["q"]["id"], "variant": t["variant"], "rep": t["rep"],
                     **score(t["q"], ans["text"], g["judge"])})
    d = new_run_dir(f"ablate-{a.skill}")
    meta = {"kind": "ablate", "skill": a.skill, "depth": a.depth, "cited_only": a.cited_only, "cfg": cfg, "backend": hs.bname, "reps": a.reps,
            "spent_usd": hs.budget.spent, "questions": [q["id"] for q in qs], "errors": errors,
            "sections": [{"id": s["id"], "title": s["title"], "level": s["level"], "lines": s["end"] - s["start"],
                          "children": s.get("children", [])} for s in secs]}
    (d / "results.json").write_text(json.dumps({"meta": meta, "results": rows}, ensure_ascii=False, indent=1), encoding="utf-8")
    (d / "report.md").write_text(render_ablate(meta, rows, load_questions()), encoding="utf-8")
    print(f"report: {d / 'report.md'}  (spent {hs.budget.spent:.2f} USD, {len(errors)} errors)")
    return 1 if errors else 0


def cmd_report(a):
    d = Path(a.run_dir)
    data = json.loads((d / "results.json").read_text(encoding="utf-8"))
    meta, rows = data["meta"], data["results"]
    md = render_ablate(meta, rows, load_questions()) if meta["kind"] == "ablate" else render_run(meta, rows, load_questions())
    (d / "report.md").write_text(md, encoding="utf-8")
    print(d / "report.md")
    return 0


# ---------------------------------------------------------------- reports


def mean(xs):
    return statistics.mean(xs) if xs else float("nan")


def f2(x):
    return "—" if x != x else f"{x:.2f}"


def sgn(x):
    return "—" if x != x else f"{x:+.2f}"


def render_run(meta, results, questions):
    cfg, th = meta["cfg"], meta["cfg"]["thresholds"]
    qmap = {q["id"]: q for q in questions}
    per = {}
    for r in results:
        per.setdefault(r["qid"], {"base": [], "skill": []})[r["arm"]].append(r)
    rows = []
    for qid in meta["questions"]:
        if qid not in per:
            continue
        b = mean([r["score"] for r in per[qid]["base"]])
        s = mean([r["score"] for r in per[qid]["skill"]])
        rows.append({"q": qmap[qid], "base": b, "skill": s, "delta": s - b, "runs": per[qid]})
    L = [f"# Voltaria evals: com e sem skill", "",
         f"- Respostas: `{cfg['answer_model']}` (effort {cfg['answer_effort']}); juiz: `{cfg['judge_model']}`; "
         f"backend `{meta['backend']}`; {meta['reps']} repetição(ões).",
         f"- {len(rows)} perguntas; custo desta execução: {meta['spent_usd']:.2f} USD (respostas e notas em cache não contam).",
         f"- Nota por pergunta: fração de itens cumpridos (`must` cumpridos + `must_not` evitados). Δ = com − sem."]
    if meta.get("errors"):
        L.append(f"- **{len(meta['errors'])} erros**: " + "; ".join(f"{e['qid']}/{e['arm']}: {e['error'][:80]}" for e in meta["errors"][:5]))
    L += ["", "## Por categoria", "", "| Categoria | n | sem | com | Δ |", "|---|---|---|---|---|"]
    cats = json.loads((EVALS / "questions.json").read_text(encoding="utf-8"))["categories"]
    for c in CATS:
        rs = [r for r in rows if r["q"]["category"] == c]
        if rs:
            L.append(f"| {c}: {cats[c][:60]} | {len(rs)} | {f2(mean([r['base'] for r in rs]))} | "
                     f"{f2(mean([r['skill'] for r in rs]))} | {sgn(mean([r['delta'] for r in rs]))} |")
    L += ["", "## Por skill", "", "Uma pergunta com duas skills conta nas duas.", "",
          "| Skill | n | sem | com | Δ | melhora | igual | piora |", "|---|---|---|---|---|---|---|---|"]
    for s in sorted({s for r in rows for s in r["q"]["skills"]}):
        rs = [r for r in rows if s in r["q"]["skills"]]
        up = sum(r["delta"] >= th["improve"] for r in rs)
        dn = sum(r["delta"] <= th["regress"] for r in rs)
        L.append(f"| {s} | {len(rs)} | {f2(mean([r['base'] for r in rs]))} | {f2(mean([r['skill'] for r in rs]))} | "
                 f"{sgn(mean([r['delta'] for r in rs]))} | {up} | {len(rs) - up - dn} | {dn} |")

    def table(title, rs, note):
        out = ["", f"## {title}", "", note, "", "| Pergunta | Cat. | Skills | sem | com | Δ |", "|---|---|---|---|---|---|"]
        for r in rs:
            out.append(f"| `{r['q']['id']}` {r['q']['question'][:70]} | {r['q']['category']} | "
                       f"{', '.join(r['q']['skills'])} | {f2(r['base'])} | {f2(r['skill'])} | {sgn(r['delta'])} |")
        return out if rs else out[:4] + ["(nenhuma)"]

    up = sorted([r for r in rows if r["delta"] >= th["improve"]], key=lambda r: -r["delta"])
    same = sorted([r for r in rows if th["regress"] < r["delta"] < th["improve"]], key=lambda r: -r["base"])
    down = sorted([r for r in rows if r["delta"] <= th["regress"]], key=lambda r: r["delta"])
    L += table("Melhoram com a skill", up, f"Δ ≥ {th['improve']}. É aqui que a skill ganha o lugar.")
    L += table("Sem diferença", same, f"|Δ| < {th['improve']}. Com nota alta nos dois braços, o modelo já sabe: "
               "o texto que a pergunta usa é candidato a corte. Com nota baixa nos dois, a skill não está a chegar à resposta.")
    L += table("Pioram com a skill", down, f"Δ ≤ {th['regress']}. Ver o que a skill diz.")
    L += ["", "## Itens que falham com a skill", "",
          "O que a resposta com skill ainda não diz (primeira repetição). Serve para corrigir a skill ou a rubrica.", ""]
    for r in rows:
        sk = r["runs"]["skill"][0] if r["runs"]["skill"] else None
        if not sk:
            continue
        miss = [m["text"] for m in sk["must"] if not m["pass"]] + \
               [f"VIOLA: {m['text']}" + (" (regex)" if m["regex_hit"] else "") for m in sk["must_not"] if m["violated"]]
        if miss:
            L.append(f"- `{r['q']['id']}`: " + "; ".join(miss))
    return "\n".join(L) + "\n"


def render_ablate(meta, rows, questions):
    th, skill = meta["cfg"]["thresholds"], meta["skill"]
    qmap = {q["id"]: q for q in questions}
    full = {}
    for r in rows:
        if r["variant"] == "__full__":
            full.setdefault(r["qid"], []).append(r["score"])
    fullm = {q: mean(v) for q, v in full.items()}
    noise = [statistics.pstdev(v) for v in full.values() if len(v) > 1]
    L = [f"# Ablação: {skill}", "",
         f"- Respostas: `{meta['cfg']['answer_model']}`; juiz: `{meta['cfg']['judge_model']}`; {meta['reps']} repetição(ões); "
         f"profundidade {'## e ###' if meta['depth'] == 3 else '##'}"
         + ("; só as perguntas que citam cada secção (Δ todas = Δ citam)." if meta.get("cited_only") else "."),
         f"- {len(meta['questions'])} perguntas da skill; custo desta execução: {meta['spent_usd']:.2f} USD.",
         f"- Nota média com a skill inteira: {f2(mean(list(fullm.values())))}."
         + (f" Ruído (desvio entre repetições): {f2(mean(noise))}." if noise else
            " Com 1 repetição não há medida de ruído: usar `--reps 3` antes de cortar."),
         "",
         "Δ = nota sem a secção − nota com a skill inteira. \"Citam\" = perguntas cuja `source` aponta para a secção.",
         f"Veredicto: **cortar?** se as perguntas que a citam não descem (Δ ≥ {th['ablation_mean']}) e nenhuma desce mais de "
         f"{-th['ablation_worst']}; **manter** se descem; **sem perguntas** se nenhuma a cita (não se sabe: escrever perguntas primeiro).",
         "", "| Secção | Linhas | Citam | Δ (citam) | Δ (todas) | Pior pergunta | Veredicto |", "|---|---|---|---|---|---|---|"]
    out = []
    for sec in meta["sections"]:
        sec_r = [r for r in rows if r["variant"] == sec["id"]]
        per_q = {}
        for r in sec_r:
            per_q.setdefault(r["qid"], []).append(r["score"])
        deltas = {q: mean(v) - fullm[q] for q, v in per_q.items() if q in fullm}
        cites = [q for q in deltas if any(source_matches(s, skill, sec) for s in qmap[q].get("source", []))]
        d_all = mean(list(deltas.values()))
        d_cit = mean([deltas[q] for q in cites])
        worst_q = min(deltas, key=deltas.get) if deltas else None
        worst = deltas[worst_q] if worst_q else float("nan")
        if not cites:
            verdict = "manter (efeito indireto)" if d_all < th["ablation_mean"] else "sem perguntas"
        elif d_cit >= th["ablation_mean"] and worst >= th["ablation_worst"]:
            verdict = "**cortar?**"
        elif d_cit < th["ablation_mean"]:
            verdict = "manter"
        else:
            verdict = "rever (uma pergunta desce)"
        order = {"**cortar?**": 0, "sem perguntas": 1, "rever (uma pergunta desce)": 2, "manter (efeito indireto)": 3, "manter": 4}[verdict]
        name = ("&nbsp;&nbsp;" if sec["level"] == 3 else "") + sec["id"]
        out.append((order, f"| {name} | {sec['lines']} | {len(cites)} | {sgn(d_cit)} | {sgn(d_all)} | "
                           f"{f'`{worst_q}` {sgn(worst)}' if worst_q else '—'} | {verdict} |"))
    L += [row for _, row in sorted(out, key=lambda x: x[0])]
    if meta.get("errors"):
        L += ["", f"**{len(meta['errors'])} erros** (essas tarefas ficaram de fora)."]
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------- main


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    p = sub.add_parser("sections")
    p.add_argument("--skill", required=True)

    def common(p):
        p.add_argument("--smoke", action="store_true", help="only config.json smoke_ids")
        p.add_argument("--ids", help="comma-separated question ids")
        p.add_argument("--category", help="one or more of abcde")
        p.add_argument("--limit", type=int)
        p.add_argument("--reps", type=int, default=1)
        p.add_argument("--backend", choices=["cli", "api", "mock"])
        p.add_argument("--budget", type=float, help="USD; default config.json budget_usd")
        p.add_argument("--workers", type=int)
        p.add_argument("--dry-run", action="store_true", help="print the estimate and stop")

    p = sub.add_parser("run")
    common(p)
    p.add_argument("--skill")
    p = sub.add_parser("ablate")
    common(p)
    p.add_argument("--skill", required=True)
    p.add_argument("--depth", type=int, choices=[2, 3], default=2, help="2: ## sections; 3: also each ###")
    p.add_argument("--cited-only", action="store_true",
                   help="per section, re-run only the questions whose source cites it (cheaper; misses indirect effects)")
    p = sub.add_parser("report")
    p.add_argument("run_dir")
    a = ap.parse_args()
    os.chdir(ROOT)
    return {"check": cmd_check, "sections": cmd_sections, "run": cmd_run, "ablate": cmd_ablate, "report": cmd_report}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
