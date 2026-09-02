---
name: implement-from-spec
description: >-
  Implements a scoped unit of work from an approved design doc or plan using
  caller-first scaffolding, contracts agreed upon, test-first design, then
  one-function-at-a-time completion. Use when implementing from a spec,
  scaffolding after a design, or executing a plan slice—not when still planning
  or comparing options.
disable-model-invocation: false
metadata:
  owner: mark
  scope: global
  category: implementation
---

# Implement from Spec

Execute a unit of work from an approved design doc or plan. Caller-first, contracts-before-behavior, tests-as-spec, one unit of work at a time.

Do not skip reference reads. Do not declare the slice done until Phase 6 passes. Each step is a separate Git commit.

## When to Use

- User asks to implement from a design, spec, or approved plan.
- User asks to scaffold, then implement a slice.
- A plan packet / design section is ready and the user wants code.

## Do Not Use

- Still comparing options → `create-advisory-brief`.
- Still writing the plan → `create-implementation-plan`.
- Unscoped “build everything in the design” with no caller/slice.

## Inputs

Before Phase 1, identify:

- Design doc, spec, or plan path (or paste in conversation).
- Optional: which unit of work / plan packet if already scoped.

If a plan has parallel task packets: one packet = one run. Honor contracts agreed upon in the plan.

## Philosophy (summary)

1. Find the main caller (how this change is used).
2. Scaffold files and imports — wiring only.
3. Confirm models / interfaces / boundaries — approve before behavior.
4. Design tests (pseudocode → real failing tests).
5. Flesh one unit of work until green; repeat until the caller path is complete.

Example walkthrough: [examples/pipeline-memory-repo.md](examples/pipeline-memory-repo.md).

## Phased Workflow (mandatory)

Complete each phase in order. Pass the phase gate before continuing. Read the linked reference before executing that phase. Commit once per step (each phase that changes the repo, and each unit of work in the Phase 5 loop).

| Phase | Read | Gate (summary) |
|-------|------|----------------|
| 1 — Scope | [references/caller-first.md](references/caller-first.md) | Caller named; file tree; unit of work + out-of-scope |
| 2 — Scaffold | [references/phase-gates.md](references/phase-gates.md) (Phase 2) | Imports resolve; stub bodies only; commit |
| 3 — Contracts | [references/contracts.md](references/contracts.md) | Signatures match design; stop for approval unless user said full auto; commit |
| 4 — Test design | [references/test-design.md](references/test-design.md) | Pseudocode → failing tests; happy + key failures; commit |
| 5 — Flesh units of work (loop) | [references/flesh-unit.md](references/flesh-unit.md) | One unit of work per iteration; one commit per unit of work; dependency order |
| 6 — Done | [checklist.md](checklist.md) | All applicable boxes checked |

Per-phase pass/fail criteria: [references/phase-gates.md](references/phase-gates.md).

### Phase 1 — Scope the unit of work

Identify main caller, proposed file tree, and the single happy-path slice for this session.

Gate: Caller named; file tree proposed; out-of-scope listed.

### Phase 2 — Scaffold and wiring

Create empty modules, imports, and a thin caller stub. No real logic. Commit this step.

Gate: Tree exists; imports resolve; caller shows the end-to-end shape (e.g. load → transform → write) with stubbed bodies.

### Phase 3 — Contracts only

Models, interfaces, method signatures. Caller may be typed but still thin. Commit this step.

Gate: Contracts match the design; bodies are stubs (`...` / `raise NotImplementedError`). Default: stop for user approval before Phase 4 unless the user said to run unattended / full auto.

### Phase 4 — Test design

Write given/when/then pseudocode, then real failing tests. Do not implement to make them pass yet. Commit this step.

Gate: Tests cover happy path + key failures from the spec; they fail for the right reasons.

### Phase 5 — Flesh units of work (loop)

Implement along dependency order of the caller path (not “easiest file first”). One function/path per iteration; run targeted tests; report newly green vs still red. Commit each unit of work before starting the next.

Gate per iteration: Exactly one unit of work advanced and committed; unrelated tests still failing is OK; no drive-by refactors.

### Phase 6 — Caller complete

All designed tests for this slice green; main path executable.

Gate: [checklist.md](checklist.md) passes. Only then declare the slice done.

## Hard Constraints

- Do not skip linked reference reads for the phase you are executing.
- Do not implement business logic during scaffold or contract phases.
- Do not write implementation before test design (Phase 4 before Phase 5).
- Do not expand into a sibling plan packet or out-of-scope files.
- Each step is a separate Git commit. Do not batch scaffold, contracts, tests, or multiple units of work into one commit.
- Prefer public test seams over poking private fields (see test-design); private seeding is OK only for throwaway demos and must be noted.

## Anti-Patterns

- Multiple entrypoints “in parallel” in one session
- Filling in methods “while scaffolding”
- Implementing several units of work in one shot
- Green tests from empty stubs that accidentally pass
- Shipping with “TODO: wire caller”
- Combining multiple steps into a single Git commit

## Additional Resources

- Phase criteria: [references/phase-gates.md](references/phase-gates.md)
- Final checklist: [checklist.md](checklist.md)
- Worked example: [examples/pipeline-memory-repo.md](examples/pipeline-memory-repo.md)
