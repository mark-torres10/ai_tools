---
name: create-advisory-brief
description: >-
  Parses the repo and conversation to produce a self-contained markdown advisory
  brief for an external AI (no codebase access) to evaluate options, recommend a
  path, and return structured deliverables. Use when comparing architecture,
  vendors, stacks, or tradeoffs before implementation — e.g. "evaluate DB
  options", "compare auth providers", "should we use X or Y".
disable-model-invocation: true
metadata:
  owner: mark
  scope: global
  category: planning
---

# Create Advisory Brief

Produce a **copy-paste markdown prompt** for an external AI (ChatGPT, Claude web, etc.) that has **no access to this repository**. The external agent must be able to compare options, recommend a path, and produce structured deliverables without asking for code or file paths.

This skill **distills** repo knowledge into prose the external agent can reason from.

## When to Use

- User wants to evaluate options (architecture, vendors, patterns) via an external AI.
- User says: "give me a prompt I can paste into ChatGPT", "evaluate DB/auth/deploy options externally", "advisory brief".

## Do Not Use

- User already chose the path and wants an implementation plan → use `create-implementation-plan`.
- User wants a code review or security review → use review skills.
- User only wants a quick opinion in this session → answer directly; do not generate an external brief.

## Repo Discovery (mandatory before writing)

Mine the workspace for **decision-relevant** facts. Prefer behavior and contracts over file dumps.

### Discovery order

1. **Conversation** — what was built, discussed, or deferred in this session.
2. **Plans** — `docs/plans/`.
3. **Architecture docs** — README, `docs/architecture/`, ADRs, strategy docs.
4. **Implementation** — interfaces (ABCs, protocols), factories, enums, stubs, `NotImplementedError` branches.
5. **Config & ops** — env vars, deployment notes, CI constraints (e.g. no live DB in tests).
6. **Dependencies** — `pyproject.toml`, `package.json`, etc. for fixed vs open stack choices.

### What to extract (internal checklist)

Before writing the brief, you must be able to answer:

- [ ] What is the product / system and why does this decision matter?
- [ ] What is **shipped** vs **stub** vs **planned**?
- [ ] What is the current request/data flow (behavior, not file tree)?
- [ ] What **boundaries** must not be conflated? (e.g. product DB vs runtime state)
- [ ] What is **fixed** (language, framework) vs **on the table**?
- [ ] What engineering contracts apply? (testing, DI, migrations, observability)
- [ ] What options does the codebase already anticipate?
- [ ] What is must-have vs should-plan-for vs out-of-scope for this decision?

**Relevance filter:** Omit facts that do not change the recommendation. No README paste. No exhaustive file lists. File paths are not load-bearing for the external agent.

## Phased Workflow

### Phase 0 — Confirm the decision

- State the decision question in one sentence.
- If ambiguous, ask one clarifying question (not a questionnaire).
- Note what you will **not** cover.

**Gate:** Decision question is specific enough to compare options.

### Phase 1 — Extract context

- Run repo discovery (above).
- Identify critical distinctions and anti-conflation boundaries.
- List constraints from repo + user rules.
- Infer candidate options from code and docs.

**Gate:** Extraction checklist complete; no invented architecture.

### Phase 2 — Assemble brief structure

Fill every required section of the output template (below). Customize:

- **Comparison dimensions** — project-specific (not generic "scalability, cost" unless appropriate).
- **Options list** — grounded in repo reality + reasonable additions.
- **Deliverables** — match user request or use defaults.
- **Anti-patterns** — failure modes for *this* decision.

**Gate:** External agent could answer without requesting code.

### Phase 3 — Quality gate

Run the sufficiency checklist (below). Fix gaps before delivering.

**Gate:** All applicable sufficiency items pass.

### Phase 4 — Deliver

- Output **only** the advisory brief as a single fenced `markdown` code block (unrendered — user will copy).
- Do not wrap the brief in meta-commentary inside the fence.
- After the fence, optionally add 2–3 bullets: assumptions you made, what the user should decide after the external pass.

Optional: if the user asks to save, write to `docs/advisory-briefs/<YYYY-MM-DD>_<descriptor>.md` with the same content.

## Output Template (required sections)

The brief inside the code fence must include these sections (adapt headings slightly if the decision type warrants it):

```markdown
# Task: [Decision title]

You are advising on [domain]. You do **not** have access to the codebase. Use the context below to compare options, recommend a path, and call out tradeoffs explicitly.

---

## Product / system context

[What this is, who uses it, why this decision matters. 1–2 short paragraphs.]

---

## Current architecture (as shipped)

[Layers, request flow, key interfaces as behavioral description. What works today.]

### [Optional: Request flow or data flow]

[Numbered steps or short diagram in prose.]

---

## Critical distinctions

[Named boundaries the evaluator must not conflate. Each: name, purpose, current state, why decoupling matters.]

---

## Technical constraints & preferences

[Bullets: stack fixed vs open, testing, CI, DI patterns, migrations, observability, deployment, team preferences from repo/rules.]

---

## Near-term requirements

### Must support
### Should plan for
### Out of scope for this evaluation

---

## Options to evaluate

### [Category A — e.g. App DB candidates]
### [Category B — e.g. Runtime / checkpointer]
### [Category C — e.g. Access layer]
### [Architecture patterns]

[List concrete options + dimensions to compare. Add categories only if relevant.]

---

## Deliverables

Produce a structured recommendation with:

1. **Executive summary** — recommended stack per environment
2. **Comparison matrix** — scored on project-specific dimensions
3. **[Domain-specific artifact]** — e.g. schema sketch, API contract, rollout phases
4. **Migration / rollout plan** — from current state to recommended state
5. **Breaking changes & blast radius**
6. **What to defer**
7. **Open questions** — assumptions + what the team must decide

[Customize list for the decision type.]

---

## Assumptions you may use unless stated otherwise

[Team size, scale, compliance, geography, etc.]

---

## Anti-patterns to avoid in your answer

[Decision-specific bad recommendations to reject explicitly.]
```

## Default deliverables (when user does not specify)

1. Executive summary (per environment if relevant)
2. Comparison matrix with project-specific dimensions
3. One concrete artifact (schema, contract, topology sketch — pick what fits)
4. Migration / rollout plan from current state
5. Breaking changes & blast radius
6. What to defer
7. Open questions and assumptions

## Sufficiency Checklist (Phase 3)

The brief is **invalid** until all applicable items pass:

- [ ] Opens with explicit **no codebase access** instruction.
- [ ] Describes **behavior and contracts**, not "read file X".
- [ ] Separates **shipped / stub / planned** clearly.
- [ ] Names at least one **critical distinction** or states none apply.
- [ ] Lists **fixed stack** vs **open choices**.
- [ ] Includes **engineering contracts** (testing, CI, ops) that constrain options.
- [ ] Options are **grounded in repo** (stubs, enums, docs) not generic textbook lists.
- [ ] Comparison **dimensions are project-specific** where possible.
- [ ] **Deliverables** are explicit and scannable.
- [ ] **Assumptions** and **anti-patterns** sections are present.
- [ ] External agent would not need to ask "can you share the repo?" to proceed.

## Stop and Ask

Stop and ask the user if:

- The decision question is too broad to compare options (help narrow to one decision).
- Multiple unrelated decisions are bundled (suggest separate briefs).
- Repo state is unclear and you cannot distinguish shipped vs stub without guessing.

Do **not** stop for missing optional inputs — use defaults and list assumptions in the brief.

## Anti-Patterns (this skill)

Never:

- Produce a handoff that says "read these files" as the primary context.
- Paste README or file tree as substitute for distilled architecture.
- Omit boundaries when two concepts are commonly conflated in this domain.
- List every vendor in the category ignoring what the repo already supports.
- Deliver without the sufficiency checklist passing.
- Put meta-commentary ("I looked at your repo…") inside the copy-paste fence.
