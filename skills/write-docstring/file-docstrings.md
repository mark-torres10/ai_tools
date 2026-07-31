# File (Module) Docstrings

Answer **why this file exists**, not what Python statements it contains. Stay at the highest useful abstraction.

## Criteria

A good module docstring:

- States high-level **purpose** in one line (optionally one short paragraph)
- Clarifies **scope** / architectural role when helpful
- May name major exported APIs when that orients the reader
- May include a minimal **usage** snippet for CLI/script entrypoints
- Omits version tags, format numbers, provisioning, cron, and runbook detail
- Avoids hot-path vs cold-path essays and "see docs/" pointers that will rot

It should answer:

1. Why is this module in the tree?
2. What problem space does it own?
3. How do I invoke it (only if that is the module's job)?

## What to cover

| Cover | Skip |
|-------|------|
| Purpose and boundary | `format_version`, schema rev, migration notes |
| Role in the architecture (brief) | Dynamo/AWS/table provisioning detail |
| Key public entrypoints | Step-by-step of internal helpers |
| How to run (scripts/CLIs) | Cron install, HPC setup, "out of scope for this PR" |

## Good vs bad

### Abstraction level

Bad — embeds version and storage mechanics that will stale:

```python
"""On-disk Bluesky Jetstream cursor contract (format_version 1).

Disk is the hot-path source of truth. DynamoDB backups (see
``backup_jetstream_cursor``) are a cold disaster-recovery mirror only.
"""
```

Good — purpose only:

```python
"""On-disk Bluesky Jetstream cursor contract."""
```

### Purpose plus usage, without ops essay

Bad — implementation, guarantees, and out-of-scope infra:

```python
"""Daily DynamoDB disaster-recovery backup for the Bluesky Jetstream disk cursor.

Example / offline-capable entrypoint: reads the on-disk cursor contract, builds a
metadata-rich DynamoDB item, and writes it only after validation. Failed writes
do not delete or mutate a prior good backup (atomic put_item only).

Does not run on the ingestion hot path. Live AWS table provisioning and HPC cron
install are out of scope for the example PR — see the recovery runbook and cron
example under docs/.

Run from the repo root:

    PYTHONPATH=. uv run python data_platform/ingestion/backup_jetstream_cursor.py \\
        backup --cursor-path data_platform/data/bluesky/jetstream/cursor.json
"""
```

Good — purpose + how to run:

```python
"""Daily DynamoDB disaster-recovery backup for the Bluesky Jetstream disk cursor.

Run from the repo root:

    PYTHONPATH=. uv run python data_platform/ingestion/backup_jetstream_cursor.py \\
        backup --cursor-path data_platform/data/bluesky/jetstream/cursor.json
"""
```

## Anti-patterns

- Changelog or PR-scope language ("for this example PR", "not yet")
- Cross-references to runbooks, tickets, or sibling modules that duplicate README
- Narrating validation/atomicity internals better left to function docstrings
- Version or format identifiers in the opening line
