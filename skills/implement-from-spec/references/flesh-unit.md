# Flesh One Unit of Work

Apply in Phase 4. Loop until the caller path for this slice is complete.

## Iteration template

For each unit of work:

1. **Choose** exactly one function or path segment (dependency order of the caller path).
2. **Implement** only that unit.
3. **Run** targeted tests (the ones that should newly pass, plus any quick regression you need).
4. **Report:**
   - Newly green tests
   - Still red (expected)
5. **Stop** the iteration; do not start the next UoW in the same undifferentiated dump of changes if the user wants step review—otherwise continue the loop cleanly labeled.

## Dependency order

Implement what the caller needs deepest-first. Example from the canonical walkthrough:

1. `MemoryRepository.get`
2. `MemoryRepository.write`
3. `transform_record`
4. `run` (close the caller)

See [../examples/pipeline-memory-repo.md](../examples/pipeline-memory-repo.md).

## Done for one iteration

- Diff is centered on one module/unit
- At least one previously designed test is now green because of this unit
- No unrelated cleanup, renames, or features

## Done for Phase 4 (exit loop)

- Every designed test for this slice is green **or** remaining reds are explicitly out-of-scope (should not happen if Phase 3 matched the slice)
- Caller path runs end-to-end for the slice

## Anti-patterns

- Multi-unit “big bang” implementation
- Refactoring neighbors while fleshing a unit
- Changing contracts in Phase 4 without returning to Phase 2 approval
- Marking the slice done while the caller is still a stub
