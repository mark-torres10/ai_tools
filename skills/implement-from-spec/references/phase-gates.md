# Phase Gates

Pass/fail criteria for each phase. Use as a copy-paste checklist before advancing.

## Phase 1 — Scope

Pass

- [ ] Exactly one main caller named (function, class used from `main`, route, job handler, CLI entry).
- [ ] Proposed file tree listed (including tests).
- [ ] Unit of work / happy-path slice stated in one sentence.
- [ ] Out-of-scope listed (sibling packets, future paths, polish).

Fail / stop

- Multiple entrypoints treated as in-scope “in parallel”
- “Build the whole module / entire design” with no slice
- Caller unclear (“we’ll figure out who calls this later”)

---

## Phase 2 — Scaffold

Pass

- [ ] Every planned file exists (or explicitly deferred with reason).
- [ ] Imports from caller (and tests) resolve.
- [ ] Caller shows end-to-end shape with stub bodies (`...` / `pass` / `raise NotImplementedError`).
- [ ] No real business logic in any module.
- [ ] Scaffold is its own Git commit.

Fail / stop

- Implementing `get` / `write` / transform / handlers during scaffold
- Files that are never imported from caller or tests (orphans without reason)
- Skipping the caller stub
- Combining scaffold with contracts or implementation in one commit

---

## Phase 3 — Contracts

Pass

- [ ] Models / types match the design doc for this slice.
- [ ] Public functions/methods have signatures (and types where the project uses them).
- [ ] Bodies remain stubs except minimal lines needed to show how the caller uses a type.
- [ ] User approved contracts or user explicitly waived approval (full auto / unattended).
- [ ] Contracts are their own Git commit.

Fail / stop

- Filling in transform or persistence logic “while defining types”
- Contracts that contradict the design without calling out the change
- Proceeding to tests/implementation without approval when interactive
- Combining contracts with test design or implementation in one commit

---

## Phase 4 — Test design

Pass

- [ ] Pseudocode scenarios use given / when / then.
- [ ] Each scenario maps to a named real test.
- [ ] Happy path for the caller slice is covered.
- [ ] At least one negative / failure case from the spec (if the spec has any).
- [ ] Tests fail for the right reason (NotImplemented / wrong result), not import errors from missing scaffold.
- [ ] Test design is its own Git commit.

Fail / stop

- Writing tests only after implementation
- Accidental green from empty stubs
- Only testing private internals when a public API exists (unless demo exception noted)
- Combining test design with implementation in one commit

---

## Phase 5 — Flesh unit of work (each iteration)

Pass

- [ ] Exactly one unit of work chosen (one function or one path segment).
- [ ] Choice follows dependency order of the caller path (e.g. `get` → `write` → `transform` → `run`).
- [ ] Diff primarily touches that unit’s module.
- [ ] Targeted tests run; newly green vs still-red reported.
- [ ] No drive-by refactors or unrelated features.
- [ ] This unit of work is its own Git commit.

Fail / stop

- Implementing `get` + `write` + `transform` in one shot
- “Easiest file first” that skips a dependency of the happy path
- Expanding scope mid-iteration
- Combining multiple units of work into one commit

---

## Phase 6 — Done

Pass

- [ ] [checklist.md](../checklist.md) fully checked for applicable items.
- [ ] Designed tests for this slice all green.
- [ ] Main caller path executable for the slice.

Fail / stop

- Shipping with TODO to wire the caller
- Declaring done while designed tests for the slice still fail
