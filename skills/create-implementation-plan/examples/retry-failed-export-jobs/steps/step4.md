# Step 4: Prove retry and dead-letter behavior with tests

## Scope

- **Caller:** End-to-end proof via pytest (and optional local curl) against job store + retry worker + existing export worker fakes—not a new production entrypoint.
- **Slice:** Lock the four behaviors from the plan: success after one failure; backoff gating; exhaustion → dead letter with last error; over-cap never requeued; poll returns `dead_letter`.
- **Out of scope:** Load/performance testing; multi-format exports; admin UI; changing defaults from Step 2.

## Files to inspect

- `tests/test_retry_worker.py`, `tests/test_retry_policy.py`, `tests/test_job_store.py`, `tests/test_exports_api.py`
- `src/exports/retry_worker.py`, `src/exports/worker.py` (failure hook)
- Existing fake queue / fake clock fixtures under `tests/conftest.py`

## Files allowed to change

- `tests/test_retry_integration.py` — **new** (or extend `tests/test_retry_worker.py` if integration fits there without bloating)
- `tests/conftest.py` — shared fixtures only (fake clock, in-memory store, recording queue)
- Tiny test-only helpers under `tests/support/` if the repo already uses that pattern

## Files forbidden to change

- Production CSV / S3 / query execution code except bugfixes discovered while testing retry accounting (if a double-increment bug appears, fix in `job_store` / worker failure hook and note it in the PR)
- `POST /exports` schema, allowed formats
- Unrelated services outside `src/exports/` and export tests

## Required scenarios

Write given/when/then tests first if any gap remains after Step 3; then flesh until green.

1. **Happy retry:** Job fails once (`attempt_count` under max, `next_retry_at` due) → `run_once` → `pending` + queue message → simulated export worker success → `completed` with download URL fields as today.
2. **Backoff gating:** Failed job with `next_retry_at` in the future → `run_once` publishes nothing and leaves status `failed`.
3. **Exhaustion:** After `EXPORT_RETRY_MAX_ATTEMPTS` failures, next retry pass marks `dead_letter` and retains the last `error` string from the final failure; queue publish count stays 0 for that pass.
4. **Over-cap never requeued:** Job already at `attempt_count >= max` and `failed` → never becomes `pending` again.
5. **Poll:** `GET /exports/{id}` after dead letter returns `"dead_letter"` and the same `error`.

Use a fake clock to advance time between failure and eligibility; do not sleep real backoff in CI.

## Must pass

```bash
pytest tests/test_retry_policy.py tests/test_retry_worker.py tests/test_retry_integration.py tests/test_job_store.py tests/test_exports_api.py -q
```

Expected: all green.

```bash
pytest tests/test_exports_worker.py -q
```

Expected: still green (CSV happy path regression).

Optional local smoke (compose up with fakes or localstack as the repo already documents for exports):

```bash
# Seed a failed job with next_retry_at in the past, then:
docker compose up -d api worker retry_worker
curl -s localhost:8000/exports/$EXPORT_ID | jq '{status,error,attempt_count}'
```

Expected eventually: either `completed` (if worker succeeds) or after forced repeated failures `dead_letter` with non-null `error`.

## Must fail (definition of incomplete)

- Missing any of the five scenarios above.
- Tests that pass only by sleeping wall-clock backoff.
- Assertions that require a new export format or new public API fields beyond status/`error`/attempt fields already introduced.

## Done when

All plan “done” criteria are evidenced by automated tests; retry + dead letter are regression-safe relative to the existing async CSV export path.
