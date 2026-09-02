# Flesh One Unit of Work

Apply in Phase 5. Loop until the caller path for this slice is complete. Each unit of work is a separate Git commit.

## Iteration template

For each unit of work:

1. Choose exactly one function or path segment (dependency order of the caller path).
2. Implement only that unit.
3. Run targeted tests (the ones that should newly pass, plus any quick regression you need).
4. Report:
   - Newly green tests
   - Still red (expected)
5. Commit this unit of work as its own Git commit.
6. Stop the iteration; do not start the next unit of work in the same undifferentiated dump of changes if the user wants step review—otherwise continue the loop cleanly labeled, committing after each unit.

## Dependency order

Implement what the caller needs deepest-first. Example from the walkthrough:

1. `MemoryRepository.get`
2. `MemoryRepository.write`
3. `transform_record`
4. `run` (close the caller)

See [../examples/pipeline-memory-repo.md](../examples/pipeline-memory-repo.md).

## Done for one iteration

- Diff is centered on one module/unit
- At least one previously designed test is now green because of this unit
- No unrelated cleanup, renames, or features
- Changes for this unit are committed before the next unit starts

## Done for Phase 5 (exit loop)

- Every designed test for this slice is green or remaining reds are explicitly out-of-scope (should not happen if Phase 4 matched the slice)
- Caller path runs end-to-end for the slice

## Anti-patterns

- Multi-unit “big bang” implementation
- Refactoring neighbors while fleshing a unit
- Changing contracts in Phase 5 without returning to Phase 3 approval
- Marking the slice done while the caller is still a stub
- Combining several units of work into one commit
