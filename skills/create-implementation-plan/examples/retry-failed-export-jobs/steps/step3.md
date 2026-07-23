# Step 3: Wire retry worker loop

## Scope

- **Caller:** `src/exports/retry_worker.py` → `run_once(now)` / `main()` process entry (compose service `retry_worker`).
- **Slice:** Claim eligible failures → either requeue as `pending` onto the existing export queue (increment attempt, clear/set timing fields) or mark `dead_letter` with last error when exhausted.
- **Out of scope:** Changing CSV generation, S3 upload, or export worker success path; new HTTP endpoints; new export formats.

## Files to inspect

- `src/exports/worker.py` — how messages are consumed and how `mark_failed` / `mark_completed` work; reuse the same queue client publish helper the API uses on create
- `src/exports/api.py` — queue message shape published on `POST /exports`
- `src/exports/job_store.py` — `list_retry_eligible`, update helpers from Steps 1–2
- `src/exports/retry_policy.py` — backoff + `should_dead_letter`
- `docker-compose.yml` — existing `api` / `worker` services
- `src/exports/__main__` or `scripts/run_worker.py` — how the export worker process is started

## Files allowed to change

- `src/exports/retry_worker.py` — **new**
- `src/exports/job_store.py` — claim/update helpers needed for atomic transition (`failed` → `pending` or `failed` → `dead_letter`)
- `docker-compose.yml` — add `retry_worker` service (same image as `worker`, different command)
- Process entry wiring mirroring the export worker (e.g. `scripts/run_retry_worker.py` or module `__main__`)
- `tests/test_retry_worker.py` — **new**

## Files forbidden to change

- CSV builders, S3 upload helpers, query runners under `src/exports/` (or `src/query/`) used only by the export worker body
- `POST /exports` request validation / format list
- Retry policy defaults (already fixed in Step 2)—only consume them here
- Frontend / non-export services

## Work

1. **Requeue path** (eligible job):
   - Atomically transition `failed` → `pending` only if still `failed` and still eligible (optimistic lock or conditional update).
   - Increment `attempt_count` by 1 as part of scheduling the retry (define clearly: attempt_count counts failures so far; requeue after failure N sets up attempt N+1—match Step 2’s formulas and document the invariant in the module docstring).
   - Set `next_retry_at` to null while pending/running.
   - Publish the **same** queue message shape as create (`export_id`, `query_id`, `format`, `requested_at`) to `EXPORT_QUEUE_URL`.
2. **Dead-letter path** (exhausted):
   - Transition `failed` → `dead_letter`.
   - Preserve existing `error` string (last failure reason); do not overwrite with a generic message unless `error` was null (then set a fixed `"retries exhausted"`).
3. **On export worker failure** (minimal hook—only if failure path today does not set retry fields):
   - When marking `failed`, set `next_retry_at = now + backoff_seconds(attempt_count + 1)` and increment `attempt_count`, **or** set `next_retry_at` from current `attempt_count` per the invariant documented above.
   - Prefer one clear place: either worker’s `mark_failed` wrapper or job_store `mark_failed`—do not double-increment.
4. **Loop:** `run_once` processes a batch (e.g. limit 100); `main` sleeps a short poll interval (e.g. 5s) between passes. No change to CSV worker loop.
5. Compose: `docker compose up api worker retry_worker` runs all three.

## Must pass

```bash
pytest tests/test_retry_worker.py -q
```

Expected: green for:

- One eligible failed job → status `pending`, message published once, not dead-lettered.
- Exhausted failed job → `dead_letter`, **no** queue publish.
- Conditional update: if job left `failed` (e.g. already completed), retry worker no-ops without publishing.

```bash
docker compose up api worker retry_worker
```

Expected: `retry_worker` process stays up; logs show poll cycles without crashing when the eligible set is empty.

## Must fail (until this step is done)

- Requeue without going through eligibility / backoff gating.
- Export worker tests that assert CSV/S3 behavior (must remain green and unchanged).

```bash
pytest tests/test_exports_worker.py -q
```

Expected: still green; no assertion changes required for happy CSV path.

## Done when

Retry worker can requeue or dead-letter using Steps 1–2 primitives; CSV/S3 code paths untouched.
