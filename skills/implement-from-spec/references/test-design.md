# Test Design

Apply in Phase 3. Tests are the executable spec for the slice. **Design before implementing.**

## Required order

1. **Pseudocode** — given / when / then scenarios covering the caller happy path and key failures from the design.
2. **Real tests** — each scenario becomes a named test; leave them failing until Phase 4.
3. **Do not** implement production code in this phase to make tests pass.

## Pseudocode shape

```markdown
given a repo with Record(id="1", value=10, label=None)
when run(repo, "1")
then get returns that record
and transform sets label to "doubled" and value to 20
and write persists TransformedRecord(...)
and run returns that written record

when get("missing")
then raise KeyError
```

## Real tests

- One test (or focused group) per scenario.
- Prefer asserting on **public APIs** the caller uses.
- Failures should be assertion / NotImplemented—not missing imports (fix scaffold first).

## Test seams

- Prefer a public seed/fixture/factory when the real boundary is not a private dict.
- Seeding private fields (e.g. `repo._store[...]`) is acceptable only for throwaway demos; **note the exception** in the test or a comment.
- Do not bake private-field access into production patterns without calling it out.

## Coverage minimum for the slice

- [ ] Caller happy path
- [ ] Each critical dependency behavior the path relies on (as separate tests when useful)
- [ ] At least one negative case if the design specifies failure behavior

## Anti-patterns

- Implementing first, then writing tests that mirror the code
- Accidental greens from `return None` stubs
- Only testing private helpers the caller never touches
- Skipping pseudocode and jumping to a sparse happy-path test
