# Step 2: Implement retry policy and eligibility

## Scope

- **Caller:** Pure functions / small module consumed later by `src/exports/retry_worker.py` (Step 3). This step’s immediate caller for TDD is unit tests.
- **Slice:** Compute backoff delay from attempt count; decide whether a failed job is eligible to requeue or must go dead letter.
- **Out of scope:** Claiming rows, publishing queue messages, process main loop, changing CSV worker.

## Files to inspect

- `src/exports/config.py` — how `EXPORT_BUCKET`, `EXPORT_TTL_HOURS`, `EXPORT_QUEUE_URL` are loaded
- `src/exports/models.py` — job fields from Step 1
- `src/exports/job_store.py` — how failed jobs are listed today (if any list helper exists)
- `tests/` — pytest time-freezing patterns already used (e.g. `freezegun` / fake clock)

## Files allowed to change

- `src/exports/config.py` — add retry settings with defaults
- `src/exports/retry_policy.py` — **new**
- `src/exports/job_store.py` — add `list_retry_eligible(now)` only (query filter; no requeue side effects)
- `tests/test_retry_policy.py` — **new**
- `tests/test_job_store.py` — eligibility list cases

## Files forbidden to change

- `src/exports/worker.py`
- `src/exports/api.py` (beyond what Step 1 already did)
- `src/exports/retry_worker.py` (does not exist until Step 3)
- `docker-compose.yml` (process wiring is Step 3)
- S3 / CSV generation modules

## Defaults (must match plan decisions)

| Setting | Default | Env name |
| --- | --- | --- |
| Max attempts | `5` | `EXPORT_RETRY_MAX_ATTEMPTS` |
| Backoff base | `30` seconds | `EXPORT_RETRY_BASE_SECONDS` |
| Backoff cap | `900` seconds (15m) | `EXPORT_RETRY_CAP_SECONDS` |

Delay for the next wait after a failure that leaves `attempt_count == k` (k starting at 1 after first failure):

`min(base * 2^(k - 1), cap)` seconds.

Eligibility for requeue (all must hold):

1. `status == failed`
2. `attempt_count < max_attempts`
3. `next_retry_at` is not null and `next_retry_at <= now`
4. Status is not `completed`, `running`, `pending`, or `dead_letter`

Exhaustion rule (for Step 3 to apply): if `status == failed` and `attempt_count >= max_attempts`, job must be marked `dead_letter` (not requeued)—policy helper may expose `should_dead_letter(job) -> bool`.

## Work

1. Load the three config values with the defaults above; document them next to existing export env docs if a README section exists (`README.md` export section only—do not invent a new doc site).
2. Implement `backoff_seconds(attempt_count) -> int` and `compute_next_retry_at(failed_at, attempt_count) -> datetime` (timezone-aware UTC).
3. Implement eligibility predicate + `job_store.list_retry_eligible(now)`.
4. Unit-test table cases for delays: attempt 1 → 30s; 2 → 60s; 3 → 120s; … until cap 900s.

## Must pass

```bash
pytest tests/test_retry_policy.py tests/test_job_store.py -q
```

Expected: all green. Coverage includes:

- Delay series and cap.
- Eligible failed job with `next_retry_at` in the past is returned.
- Failed job with `next_retry_at` in the future is not returned.
- `attempt_count >= max_attempts` is not eligible (and `should_dead_letter` is true).
- `completed` / `running` / `pending` / `dead_letter` never eligible.

## Must fail (until this step is done)

- Tests that expect requeue or status transitions (those belong in Steps 3–4).
- Eligibility returning jobs with future `next_retry_at`.

## Done when

Policy + eligibility are pure/testable and job store can list due failures; nothing publishes to the export queue yet.
