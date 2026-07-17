# Caller-First Scoping

Apply in Phase 0. Goal: name **one** main caller and **one** unit-of-work slice before scaffolding.

## What is the main caller?

How this change will be used by whatever calls or uses it. Typically:

- A single function plugged into a flow
- A class constructed and used from `main.py` / `__main__`
- A route handler, job entrypoint, CLI command, or workflow step

Ask: *“If we only finish one path, which entrypoint proves the design works?”*

## How to pick the unit of work

1. State the happy path through the caller in plain English (e.g. load → transform → write).
2. List the functions/methods that path needs.
3. The **session slice** is that path (or one plan packet that owns it)—not every edge case in the design doc.
4. Defer alternate entrypoints, admin tools, and unrelated modules to out-of-scope.

## Dependency order (for Phase 4)

Flesh units along the **caller path’s dependency order**, not “easiest file first”:

1. Leaves the caller needs first (e.g. repository `get`)
2. Then siblings the path needs (e.g. `write`, then `transform`)
3. Close the caller last (e.g. `run`) once dependencies behave

See [../examples/pipeline-memory-repo.md](../examples/pipeline-memory-repo.md).

## Output of Phase 0

Produce a short scope block:

```markdown
## Scope
- **Caller:** `pipeline/main.py` → `run(repo, record_id)`
- **Slice:** load → transform → write via MemoryRepository
- **Files:** models.py, repository.py, transform.py, main.py, tests/test_pipeline.py
- **Out of scope:** real DB, CLI flags, batch mode
```

## Anti-patterns

- Starting with “shared utils” with no caller
- Scaffolding five services before naming who invokes them
- Treating the whole design doc as one undivided implementation session
