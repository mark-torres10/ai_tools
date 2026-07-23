# Step 1: Extend job store for attempts and dead letter

## Scope

- **Caller:** Job-store read/write used by `src/exports/api.py` (`GET /exports/{export_id}`) and `src/exports/worker.py` (mark failed / completed). This step only extends persistence and models; no retry loop.
- **Slice:** Persist attempt count, next-retry time, last error, and `dead_letter` status; status poll returns the new status when set.
- **Out of scope:** Backoff math, eligibility queries, requeue, compose process for retry worker.

## Files to inspect

- `src/exports/models.py` — current job record / status enum (`pending` | `running` | `completed` | `failed`)
- `src/exports/job_store.py` — create, get, update status helpers
- `src/exports/api.py` — `GET /exports/{export_id}` response mapping
- `src/exports/worker.py` — how failure writes `error` and `failed`
- `migrations/` — latest export-jobs migration naming convention
- `tests/test_job_store.py`, `tests/test_exports_api.py` — existing fixtures

## Files allowed to change

- `src/exports/models.py`
- `src/exports/job_store.py`
- `src/exports/api.py` (status mapping only—accept `dead_letter` in response)
- `migrations/<next>_export_jobs_retry_fields.sql` (or equivalent Alembic revision under `migrations/`)
- `tests/test_job_store.py`
- `tests/test_exports_api.py` (status serialization only)

## Files forbidden to change

- `src/exports/worker.py` (CSV / S3 path unchanged this step)
- `src/exports/config.py` (retry env vars come in Step 2)
- Queue publishers/consumers beyond what job_store already uses
- Any new export format or `POST /exports` request body fields

## Work

1. Add job fields (names must match store + API):
   - `attempt_count` — integer, default `0` for new jobs; existing rows backfilled to `0`
   - `next_retry_at` — nullable timestamp; null when not scheduled
   - `error` — keep existing last-error string; required non-null when status is `dead_letter`
2. Extend status to include `dead_letter`.
3. Migration: add columns + check/constraint so `dead_letter` is a valid status; backfill `attempt_count = 0`.
4. Job store: get/update must round-trip the new fields; add or extend `mark_dead_letter(export_id, error)` and ensure `mark_failed` still sets `failed` + `error` without clearing attempt fields incorrectly.
5. API: `GET /exports/{export_id}` returns `status: "dead_letter"` and `error` when applicable. No new endpoints.

## Contracts to freeze before behavior (implement-from-spec Phase 2)

- Status union includes `dead_letter`.
- Job record includes `attempt_count`, `next_retry_at`, `error`.
- Poll response shape unchanged except status may be `dead_letter`.

## Must pass

```bash
pytest tests/test_job_store.py tests/test_exports_api.py -q
```

Expected: all green. New/updated tests prove:

- Creating a job yields `attempt_count == 0`, `next_retry_at is None`.
- Persisting `dead_letter` + `error` and reading back via store and `GET /exports/{id}` returns that status and error.
- Existing `pending` → `running` → `completed` / `failed` paths still round-trip.

```bash
# After migration applied in local compose/DB:
curl -s localhost:8000/exports/exp_fixture_dead | jq .status
```

Expected (fixture seeded as dead letter): `"dead_letter"`.

## Must fail (until this step is done)

- Any test that asserts status enum rejects `dead_letter`.
- Reading a migrated row without `attempt_count` default (migration incomplete).

## Done when

Job store and GET status support attempt fields and `dead_letter`; no retry scheduling code exists yet.
