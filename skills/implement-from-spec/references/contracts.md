# Contracts Only

Apply in Phase 2. Freeze models, interfaces, and boundaries **without** behavior.

## What to define

- Data models / schemas (e.g. Pydantic `BaseModel`, dataclasses, types)
- Repository / port interfaces and concrete class **signatures**
- Function signatures the caller will invoke
- Error types the design specifies (as types or documented raises)—not full handlers yet

## What is allowed in bodies

- `...` / `pass` / `raise NotImplementedError`
- Trivial constructors that only hold empty state (e.g. `self._store: dict = {}`)
- Caller wiring that **calls** stubs in the correct order (typed shape), still without real logic inside callees

## What is forbidden

- Transform / business rules
- Persistence behavior beyond empty containers
- Validation logic beyond what the type system already enforces
- Helper functions with real implementations “for later”

## Alignment with the design

- Field names and types must match the design/spec for this slice.
- If you must diverge, state the divergence explicitly and get approval with the contracts.

## Approval gate

**Default:** stop after Phase 2 and present contracts (file list + key signatures) for user approval.

**Skip approval only if** the user said full auto, unattended, or explicitly waived the pause.

## Anti-patterns

- “While defining the repo, I’ll just implement `get`”
- Fat interfaces that include methods not needed by this caller slice
- Premature abstract base classes when one concrete type suffices for the slice
