---
name: implement-from-spec
description: >-
  Implements a scoped unit of work from an approved design doc or plan.
  Scaffold from the caller and agree on contracts. Finish one function at
  a time. Write the smallest change, and write tests only for production
  logic with real behavior. Use when implementing from a spec or an approved
  plan. Do not use it while still planning or comparing options.
disable-model-invocation: false
metadata:
  owner: mark
  scope: global
  category: implementation
---

# Implement from Spec

Execute a unit of work from an approved design doc or plan. Start from the caller, and agree on contracts before behavior. Finish one unit of work at a time. Design tests before implementation only when the testing policy below says tests belong.

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
4. Design tests when they belong (pseudocode, then real failing tests). Skip test design when they do not.
5. Implement one unit of work at a time until the caller path is complete.

Example walkthrough: [examples/pipeline-memory-repo.md](examples/pipeline-memory-repo.md).

## Write the smallest change

Write the smallest change that satisfies the spec.

Prefer fewer files, fewer functions, and fewer lines. Reuse a utility that already exists, and delete code when deletion satisfies the spec.

Do not add any of the following unless the spec asks for it:

- a speculative abstraction, such as a base class or an interface with one implementation
- extra config
- a module that only forwards calls to another module
- a defensive check for a case that cannot happen
- a feature the spec does not name

Do not add a comment or docstring that only restates the code. A docstring may state an outcome the function name does not already show. `write-docstring` still applies when a later skill runs it.

Before you finish, read the diff and ask what you can remove. Remove it when the spec still holds.

## When to write tests

Write a test for production logic that has real behavior. A function that decides whether a failed job is eligible to retry is production logic, so it gets a test.

Do not write a unit test for any of the following:

- Code that is clearly experimental, such as a script, a notebook, a one-off analysis, a prototype, or exploratory code, including a file under `experiments/` and a one-off script in any other folder. A notebook that plots a sample does not get a unit test.
- A constant, a config value, or other static data. `MAX_RETRIES = 3` does not get a unit test, and a change that only edits configuration does not get a unit test either.
- Code that does not run production logic, such as a type alias, a re-export, or a stub that only wires calls and has no behavior of its own.

When the task does not need tests, skip Phase 4. Implement the behavior in Phase 5, and do not add a test file to fill the phase list.

When the task needs tests, design them in Phase 4 before you implement in Phase 5.

## Phased Workflow (mandatory)

Complete each phase in order. Pass the phase gate before continuing. Read the linked reference before executing that phase. Commit once per step (each phase that changes the repo, and each unit of work in the Phase 5 loop).

| Phase | Read | Gate (summary) |
|-------|------|----------------|
| 1 — Scope | [references/caller-first.md](references/caller-first.md) | Caller named; file tree; unit of work + out-of-scope |
| 2 — Scaffold | [references/phase-gates.md](references/phase-gates.md) (Phase 2) | Imports resolve; stub bodies only; commit |
| 3 — Contracts | [references/contracts.md](references/contracts.md) | Signatures match design; stop for approval unless user said full auto; commit |
| 4 — Test design | [references/test-design.md](references/test-design.md) | Skip when tests do not belong. Otherwise pseudocode, then failing tests for the happy path and the failures the spec names; commit |
| 5 — Implement units of work (loop) | [references/implement-unit.md](references/implement-unit.md) | One unit of work per iteration; one commit per unit of work; dependency order |
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

Skip this phase when the testing policy above says the task does not need tests. Do not add a test file to complete the phase list.

When tests belong, write given/when/then pseudocode, then real failing tests. Do not implement production code in this phase to make those tests pass. Commit this step.

Gate: the tests cover the happy path and the failures the spec names, and they fail for the right reasons. If you skipped the phase, write a short note of why tests do not belong.

### Phase 5 — Implement units of work (loop)

Implement in the dependency order of the caller path, deepest call first. Take one function or path per iteration. When this task has tests, run the tests that should newly pass. Report which of those tests are newly green and which are still red. When this task has no tests, run the caller path for that unit. Commit each unit of work before you start the next.

Gate per iteration: advance and commit exactly one unit of work. Leave unrelated code alone. You can leave unrelated tests failing when this task has tests.

### Phase 6 — Caller complete

When this task has tests, every designed test is green. The main path runs.

Before you declare the task done, read the diff and ask what you can remove. Delete any file, function, comment, or branch the spec does not need.

Gate: [checklist.md](checklist.md) passes. Only then declare the task done.

## Hard Constraints

- Do not skip linked reference reads for the phase you are executing.
- Do not implement business logic during scaffold or contract phases.
- When this task needs tests, do not write implementation before test design (Phase 4 before Phase 5).
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
