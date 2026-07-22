# Data gate (Layer 1)

Read when the PR is a **data** change: pipelines, ETL/ELT, warehouse/lake transforms, dataset schemas, batch/stream jobs, feature stores, or other work whose core story is how data moves.

## Fires when

Diff touches data movement in a meaningful way — e.g. `pipelines/`, `etl/`, `dbt/`, warehouse models, Spark/Prefect/Airflow jobs, dataset builders, schema migrations that change what flows where — not a one-line config typo with no path change.

## Required under Details

1. **Data flow (narrative)** — Short numbered steps: source → transforms → sinks. Name real stores, topics, tables, and jobs from the diff.
2. **How data moves** — Mermaid of the data path after this PR.
   - If an existing data path changed: **Before** and **After** diagrams.
   - If this PR introduces a new data path: **After** only.

Optional one-line notes on volume, freshness, or idempotency only when they matter to review.

## Mermaid guidance

- Prefer `flowchart LR` or `flowchart TD`.
- Nodes = sources, jobs, tables/topics, sinks — not abstract buzzwords.
- Label edges with format or trigger when useful (`Parquet`, `daily`, `CDC`).

## Example shape

```markdown
### Data flow

1. Raw events land in `s3://…/raw/events/`.
2. `etl/events_clean.py` normalizes and writes `events_clean`.
3. dbt model `marts.user_daily` aggregates to the warehouse mart.

### Before
(mermaid of prior path — if existing)

### After
(mermaid of proposed path)
```

## Checklist

- [ ] Narrative covers source → transform → sink
- [ ] After (and Before if existing path changed) mermaid present
- [ ] Nodes match real artifacts in the diff
- [ ] Terse; no plan dump
