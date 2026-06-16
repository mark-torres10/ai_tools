---
name: create-implementation-plan
description: Creates implementation plans following PLANNING_RULES. Use when the user asks to create a plan, write an implementation plan, or plan out work. Ensures Overview, Happy Flow, Manual Verification, Update Runbooks (audit docs/runbooks/), parallel delegation, asset storage, and UI screenshots. Loads phase-specific reference files before each gate.
disable-model-invocation: false
metadata:
  owner: mark
  scope: global
  category: planning
---

# Create Implementation Plan

Orchestrate implementation plans using phased gates. **Do not skip reference reads.** **Do not deliver the plan until Phase 5 passes.**

## When to Use

- User asks to create a plan, write an implementation plan, or plan out work.
- User enters plan mode and wants planning rules applied.
- User asks for a structured breakdown with verification.

## Path Discovery

### ai_tools root (planning rules)

Planning rules live inside an `ai_tools` tree. Resolve **ai_tools root** in this order:

1. **Submodule in workspace** — `./ai_tools/` containing `agents/task_instructions/rules/PLANNING_RULES.md`
2. **Local clone** — `/Users/mark/Documents/projects/ai_tools/`
3. **Global skill copy** — if this skill is loaded from `~/.cursor/skills/create-implementation-plan/`, use sibling references in that directory; for `PLANNING_RULES.md`, prefer steps 1–2 first
4. **Remote fallback** — if none of the above exist, use the canonical repo: [https://github.com/mark-torres10/ai_tools](https://github.com/mark-torres10/ai_tools)
   - Fetch or browse `agents/task_instructions/rules/PLANNING_RULES.md` from that repo (raw GitHub URL or clone instructions for the user)
   - Apply the same rules; use this skill's `references/` and `checklist.md` for structure beyond what `PLANNING_RULES.md` covers

**Planning rules file:** `<ai_tools_root>/agents/task_instructions/rules/PLANNING_RULES.md`

If found locally, read it. If only the GitHub fallback is available, read `PLANNING_RULES.md` from the repo before Phase 1.

### Skill references (this skill)

Resolve the directory containing this `SKILL.md`, then read files relative to it:

| File | When |
|------|------|
| [references/plan-structure.md](references/plan-structure.md) | Phase 1 |
| [references/runbooks-audit.md](references/runbooks-audit.md) | Phase 2 (always) |
| [references/runbook-template.md](references/runbook-template.md) | Phase 2 (when proposing new runbooks) |
| [references/parallel-delegation.md](references/parallel-delegation.md) | Phase 3 |
| [references/ui-screenshots.md](references/ui-screenshots.md) | Phase 4 (UI changes only) |
| [checklist.md](checklist.md) | Phase 5 (always) |

### Target workspace runbooks

**Runbook root:** `<workspace_root>/docs/runbooks/` (the repo where the change lands—not ai_tools unless that is the target).

## Required Plan Structure (summary)

Every plan must include all 11 sections listed in [references/plan-structure.md](references/plan-structure.md). Do not omit **Update Runbooks** (use explicit no-impact when N/A).

## Phased Workflow (mandatory)

Complete each phase in order. Pass the phase gate before continuing.

### Phase 0 — Resolve paths

- Resolve ai_tools root and read `PLANNING_RULES.md` (local or [GitHub fallback](https://github.com/mark-torres10/ai_tools)).
- Resolve skill reference directory (this skill's folder).
- Note target workspace root for `docs/runbooks/` and `docs/plans/`.

**Gate:** Paths documented; `PLANNING_RULES.md` loaded or GitHub fallback applied.

### Phase 1 — Core plan

**Read:** [references/plan-structure.md](references/plan-structure.md)

Draft Overview, Happy Flow, Manual Verification, Alternative approaches, and choose plan asset path under `docs/plans/<YYYY-MM-DD>_<descriptor>_<6-digit hash>/`. Add Remember block at top.

**Gate:** Phase 1 checklist in `plan-structure.md` passes.

### Phase 2 — Update Runbooks (every plan)

**Read:** [references/runbooks-audit.md](references/runbooks-audit.md)

Inventory `docs/runbooks/` in the target workspace. Write **Update Runbooks** section.

**Also read** [references/runbook-template.md](references/runbook-template.md) when proposing new runbooks.

**Gate:** Phase 2 checklist in `runbooks-audit.md` passes.

### Phase 3 — Parallel delegation

**Read:** [references/parallel-delegation.md](references/parallel-delegation.md)

Add Serial Coordination Spine, Interface or Contract Freeze, Parallel Task Packets, Integration Order, Final Verification. Apply validity test to every delegated task.

**Gate:** Phase 3 checklist in `parallel-delegation.md` passes.

### Phase 4 — UI screenshots (conditional)

**Trigger:** Plan changes anything under `ui/` or equivalent frontend paths.

**Read:** [references/ui-screenshots.md](references/ui-screenshots.md)

Set first to-do = before screenshots, last to-do = after screenshots. Agent captures screenshots—not the user.

**Gate:** Phase 4 checklist in `ui-screenshots.md` passes, or phase skipped with documented reason.

### Phase 5 — Final gate

**Read:** [checklist.md](checklist.md)

Verify every applicable checkbox. Fix failures and re-run Phase 5.

**Gate:** All applicable items in `checklist.md` checked. **Only then deliver the plan.**

## Hard Constraints

- Do not skip Manual Verification or Update Runbooks.
- Plans are invalid if they do not maximize safely delegable parallel work.
- Delegated tasks are invalid without exact file boundaries, dependencies, contracts, verification commands, and completion criteria.
- Do not skip linked reference files for a phase you are executing.
- Prefer specificity over brevity for critical steps.

## Anti-Patterns (summary)

See reference files for full lists. Never:

- Deliver a plan before Phase 5 passes
- Skip runbook inventory when ops behavior changes
- Delegate ambiguous tasks or share file ownership across parallel tasks without serial coordination
- Ask the user to take UI screenshots
