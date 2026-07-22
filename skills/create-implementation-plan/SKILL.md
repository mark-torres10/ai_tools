---
name: create-implementation-plan
description: >-
  Creates Approach A implementation plans: complete static plan package with
  plan.md as Layer 0 router/exec summary and full detail in sibling artifacts
  (contracts, spine, packets, verification, gated runbooks/alternatives/images).
  Use when the user asks to create a plan, write an implementation plan, or plan
  out work with progressive-disclosure package layout.
disable-model-invocation: false
metadata:
  owner: mark
  scope: global
  category: planning
---

# Create Implementation Plan

Produce a **complete plan package up front**, consumed via **progressive disclosure**.

**`plan.md` = Layer 0 only** (router + executive summary). Full detail lives in sibling files under the plan asset directory. Planning still runs every applicable phase; completeness is Layer 0 + fired gates' leaves—not all 11 sections inlined in `plan.md`.

**Audience:** humans skim Layer 0; agents (or humans) open leaf files for depth.  
**Do not** dump full packet steps into `plan.md`. **Do not** create empty N/A files or filler sections.

## When to Use

- User asks to create a plan, write an implementation plan, or plan out work.
- User wants a plan package with `plan.md` as router and detail in sibling files.
- User enters plan mode and wants planning rules applied with progressive disclosure.

## Path Discovery

### ai_tools root (planning rules)

Planning rules live inside an `ai_tools` tree. Resolve **ai_tools root** in this order:

1. **Submodule in workspace** — `./ai_tools/` containing `agents/task_instructions/rules/PLANNING_RULES.md`
2. **Local clone** — `/Users/mark/Documents/projects/ai_tools/`
3. **Global skill copy** — if loaded from `~/.cursor/skills/`, prefer steps 1–2 for `PLANNING_RULES.md`
4. **Remote fallback** — [https://github.com/mark-torres10/ai_tools](https://github.com/mark-torres10/ai_tools) → `agents/task_instructions/rules/PLANNING_RULES.md`

**Planning rules file:** `<ai_tools_root>/agents/task_instructions/rules/PLANNING_RULES.md`

If found locally, read it. If only GitHub fallback is available, read `PLANNING_RULES.md` from the repo before Phase 1.

### Skill references (this skill)

Resolve the directory containing this `SKILL.md`, then read files relative to it **only when the phase or gate needs them**:

| File | When |
|------|------|
| [references/plan-structure.md](references/plan-structure.md) | Phase 1 (Layer 0 + package layout) |
| [references/parallel-delegation.md](references/parallel-delegation.md) | Parallel / heavy-contracts gates |
| [references/runbooks-audit.md](references/runbooks-audit.md) | Ops / runbooks gate |
| [references/runbook-template.md](references/runbook-template.md) | Ops gate + proposing new runbooks |
| [references/ui-screenshots.md](references/ui-screenshots.md) | UI gate |
| [checklist.md](checklist.md) | Phase 4 (always) |

### Target workspace

**Plan assets:** `<workspace_root>/docs/plans/`  
**Runbooks:** `<workspace_root>/docs/runbooks/` (inventory only when ops gate fires)

## Package layout (generate this shape)

```text
docs/plans/<YYYY-MM-DD>_<descriptor>_<6-digit hash>/
  plan.md                 # router + exec summary ONLY (Layer 0)
  contracts.md            # Interface / Contract Freeze (full) — when parallel/contract gate fires
  spine.md                # Serial Coordination Spine (short, ordered)
  packets/
    T1_<slug>.md          # full parallel task packets (14 fields)
    T2_<slug>.md
  verification.md         # Manual + Final Verification (detailed) — always
  runbooks.md             # Update Runbooks audit — ONLY if ops gate fires
  alternatives.md         # short options — ONLY if non-trivial alternatives
  images/...              # UI before/after — ONLY if UI gate fires
```

Omit files whose gates did not fire. Never write empty N/A stubs.

## Depth gates

| Gate | When | Artifact(s) |
|------|------|-------------|
| Parallel / multi-agent | Work can safely split | `contracts.md`, `spine.md`, `packets/*.md`; Tasks (in order) in `plan.md` |
| Heavy contracts | Shared schemas/APIs must freeze (even if little parallel split) | `contracts.md` |
| Ops / runbooks | Operator/deploy/incident behavior changes | `runbooks.md` |
| UI | Frontend paths change | Screenshot todos in package + `images/` guidance ([ui-screenshots.md](references/ui-screenshots.md)) |
| Non-trivial alternatives | Real tradeoff worth recording | `alternatives.md` |

**Completeness** = Layer 0 (`plan.md` + always `verification.md`) + every fired gate's leaves exist.

## Phased Workflow (mandatory)

Complete phases in order. Pass each gate before continuing. **Read linked refs only when that phase/gate needs them.**

| Phase | Read | Gate |
|-------|------|------|
| 0 — Paths | — | `PLANNING_RULES.md` + paths resolved |
| 1 — Layer 0 core | [plan-structure.md](references/plan-structure.md) | Remember, Overview, Happy Flow, approach, asset path; verification drafted in leaf |
| 2 — Depth gates | Matching `references/*.md` only | Leaf files written only for fired gates; skip silent |
| 3 — Assemble `plan.md` | [plan-structure.md](references/plan-structure.md) (Layer 0 shape) | Router indexes leaves; ~150–250 lines skim target; no packet walls |
| 4 — Done | [checklist.md](checklist.md) | Layer 0 + fired leaves pass checklist |

### Phase 0 — Resolve paths

- Resolve ai_tools root and read `PLANNING_RULES.md` (local or GitHub fallback).
- Resolve this skill's reference directory.
- Note target workspace roots for `docs/plans/` and (if needed) `docs/runbooks/`.

**Gate:** Paths documented; planning rules loaded.

### Phase 1 — Layer 0 core + verification leaf

**Read:** [references/plan-structure.md](references/plan-structure.md)

- Choose plan asset path: `docs/plans/<YYYY-MM-DD>_<descriptor>_<6-digit hash>/`.
- Draft Remember, Overview, Happy Flow, chosen approach (1–3 sentences).
- Always write **`verification.md`** with full Manual Verification + Final Verification (exact commands, expected outcomes).
- Soft-draft gate signals (parallel? ops? UI? alternatives? contracts?).

**Gate:** Phase 1 checklist in `plan-structure.md` passes; `verification.md` exists with specific checks.

### Phase 2 — Depth gates (leaves only)

Evaluate each gate. **If a gate does not fire, do not create its file and do not add an N/A section.**

| Gate | Read | Write |
|------|------|-------|
| Parallel / multi-agent | [parallel-delegation.md](references/parallel-delegation.md) | `contracts.md`, `spine.md`, `packets/T*_*.md` |
| Heavy contracts (no/few packets) | [parallel-delegation.md](references/parallel-delegation.md) (freeze section) | `contracts.md` only |
| Ops / runbooks | [runbooks-audit.md](references/runbooks-audit.md) (+ template if new) | `runbooks.md` |
| UI | [ui-screenshots.md](references/ui-screenshots.md) | First/last screenshot todos; `images/before|after` paths |
| Non-trivial alternatives | — | `alternatives.md` (short) |

Packet leaves must include all **14 fields** per [parallel-delegation.md](references/parallel-delegation.md). Prefer specificity in leaves.

**Gate:** Every fired gate has its leaf artifact(s); unfired gates leave no files and no filler.

### Phase 3 — Assemble `plan.md` (Layer 0 router)

**Read:** Layer 0 shape in [plan-structure.md](references/plan-structure.md)

Write **only** the router/exec summary into `plan.md` (see Layer 0 contents below). Link out to leaves. Soft budget: skim-friendly **~150–250 lines**—not a wall of packet steps.

**Gate:** `plan.md` indexes every present leaf; Happy Flow stays enumerated with file refs; no inlined 14-field packets.

### Phase 4 — Checklist

**Read:** [checklist.md](checklist.md)

Fix gaps; re-run until applicable boxes pass.

**Gate:** Checklist passes. **Only then deliver the package.**

## What `plan.md` (Layer 0) contains

1. Short **Remember** block  
2. **Overview** (why)  
3. **Happy Flow** (enumerated, file refs — keep here)  
4. **Chosen approach** (1–3 sentences; link to `alternatives.md` if present)  
5. **Contracts pointer** — e.g. "See details in [contracts.md](contracts.md)" — omit if no `contracts.md` (no frozen-symbol lists)  
6. **Spine pointer** — e.g. "See details in [spine.md](spine.md)" — omit if no `spine.md` (no spine task lines)  
7. **Tasks (in order)** — markdown table with exactly three columns: **ID** | **Task description** | **File**; rows in execution/integration order (spine + packets); omit if no packets/spine  
8. **Verification pointer** — e.g. "See [verification.md](verification.md)" — always (no top-checks list)  
9. **Runbooks pointer** (touch/no-touch + link) — **only if** `runbooks.md` exists  
10. **UI notes** (screenshot paths) — only if UI gate fired  

Do **not** include: Contract freeze index details, Spine index details, Packet table (old multi-column form), Integration order, or Verification index lists.

## Output shape

**Simple plan (no depth gates):**

```text
docs/plans/2026-07-22_fix_timeout_a1b2c3/
  plan.md              # Remember, Overview, Happy Flow, approach, verification pointer
  verification.md      # full Manual + Final Verification
```

**Gated plan (parallel + ops + UI):**

```text
docs/plans/2026-07-22_split_ingest_d4e5f6/
  plan.md
  contracts.md
  spine.md
  packets/T1_schema.md
  packets/T2_worker.md
  packets/T3_ui.md
  verification.md
  runbooks.md
  images/before/       # populated at execution
  images/after/
```

`plan.md` stays an index; leaves hold rigor.

## Hard Constraints

- Prefer **specificity in leaves**; **brevity in `plan.md`**.
- `plan.md` is a router — never inline full parallel packet bodies.
- Always produce Layer 0 + `verification.md`.
- Never add empty sections, "N/A" placeholders, or unfired gate files.
- Do not skip linked reference reads for a gate you are executing.
- Delegated packets are invalid without all 14 fields and the validity test.
- Plans must still maximize safely delegable parallel work when the parallel gate applies.

## Anti-Patterns

- All 11 sections dumped into a single `plan.md`
- Creating `runbooks.md` / `alternatives.md` / `contracts.md` with "N/A"
- Packet / Tasks table in `plan.md` that duplicates step-by-step instructions from leaves
- Frozen-symbol lists, spine task lines, verification check lists, or a separate Integration order section in `plan.md`
- Delivering before Phase 4 checklist
- Asking the user to take UI screenshots (agent captures them)

## Additional resources

- Layer 0 + package: [references/plan-structure.md](references/plan-structure.md)
- Packets / freeze / spine: [references/parallel-delegation.md](references/parallel-delegation.md)
- Ops audit: [references/runbooks-audit.md](references/runbooks-audit.md)
- New runbook template: [references/runbook-template.md](references/runbook-template.md)
- UI screenshots: [references/ui-screenshots.md](references/ui-screenshots.md)
- Final checklist: [checklist.md](checklist.md)
