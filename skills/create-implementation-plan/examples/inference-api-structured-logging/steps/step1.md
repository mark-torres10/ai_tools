# Step 1: Define request-id and JSON log contracts

Freeze contracts before behavior. Scaffold modules and write failing tests that encode the decisions in [../plan.md](../plan.md). Do not implement middleware or change error responses yet.

## Scope

- **Caller (for later steps):** ASGI middleware registered from `inference-api/app/main.py` that wraps every HTTP request.
- **This slice:** Types, constants, pure helpers (resolve id, serialize log events), and failing tests for those contracts.
- **Out of scope:** Middleware wiring, error-body attachment, changing `POST /v1/infer`, metrics/tracing vendors.

## Files

### Inspect

- `inference-api/app/main.py` — how the FastAPI app and existing middleware are created
- `inference-api/app/errors.py` — current error JSON shape
- `inference-api/app/logging_setup.py` — how the stdlib logger is configured today
- `inference-api/tests/conftest.py` — API client / app fixture patterns
- `inference-api/tests/test_infer_api.py` — existing inference route tests

### Allowed to change

- `inference-api/app/request_context.py` — **create** (constants, id resolution helper, log-event builders; stub bodies OK if signatures are frozen)
- `inference-api/app/logging_setup.py` — add JSON formatter / logger name for access events only if needed for imports to resolve; no runtime switch-over required yet
- `inference-api/tests/test_request_context.py` — **create** (contract tests; must fail until Step 2+)

### Forbidden to change

- `inference-api/app/routes/infer.py`
- `inference-api/app/routes/health.py`
- `inference-api/app/errors.py`
- `inference-api/app/main.py` (no middleware registration yet)
- Dependency manifests except if a stdlib-only approach needs no new packages (prefer stdlib `logging` + `json`; do not add OpenTelemetry, structlog, or Datadog SDKs)

## Contracts to freeze

### Request id

| Rule | Value |
| --- | --- |
| Incoming header | `X-Request-ID` |
| Response header | `X-Request-ID` (echo resolved id) |
| Valid incoming | non-empty, length ≤ 128, all chars in printable ASCII `0x20`–`0x7E` |
| Invalid or missing | generate UUID4 string (canonical `str(uuid.uuid4())`) |
| Context binding | store resolved id on `request.state.request_id` (Starlette/FastAPI request state) |

### Access log events (one JSON object per line on stdout)

**Start event**

| Field | Type | Notes |
| --- | --- | --- |
| `event` | string | literal `"request_start"` |
| `request_id` | string | resolved id |
| `method` | string | HTTP method |
| `path` | string | request path (no query string required) |

**End event**

| Field | Type | Notes |
| --- | --- | --- |
| `event` | string | literal `"request_end"` |
| `request_id` | string | same id as start |
| `method` | string | HTTP method |
| `path` | string | request path |
| `status_code` | int | final HTTP status |
| `latency_ms` | number | wall time from start to end, milliseconds (float OK) |

Health paths `/health` and `/ready` still get an id; access start/end events are **not** emitted for those paths (enforced in Step 2; document the skip set here as `ACCESS_LOG_SKIP_PATHS = {"/health", "/ready"}`).

### Error body field (consumed in Step 3)

Existing error JSON gains key `request_id` (string). Do not rename existing keys (`detail`, `error`, or whatever `errors.py` already uses).

## Implement-from-spec phases for this step

### Phase 0 — Scope

Confirm caller = middleware in `main.py` (wired in Step 2). File tree:

```text
inference-api/app/request_context.py
inference-api/tests/test_request_context.py
```

### Phase 1 — Scaffold

Create `request_context.py` with imports resolving from the test module. Stub:

- `HEADER_NAME`
- `ACCESS_LOG_SKIP_PATHS`
- `resolve_request_id(header_value: str | None) -> str`
- `build_request_start_event(...)` / `build_request_end_event(...)` returning `dict[str, object]`

Bodies may raise `NotImplementedError`.

### Phase 2 — Contracts

Lock signatures and constants to the tables above. Stop if anything contradicts plan decisions.

### Phase 3 — Test design (failing)

Pseudocode → real tests in `test_request_context.py`:

1. **Given** a valid `X-Request-ID` value **when** `resolve_request_id` **then** returns that value unchanged.
2. **Given** missing header **when** resolve **then** returns a UUID4-shaped string.
3. **Given** empty / too-long / non-printable header **when** resolve **then** returns a new UUID4 (not the invalid input).
4. **Given** start builder inputs **when** build start **then** dict has exact keys/literals for `event`, `request_id`, `method`, `path`.
5. **Given** end builder inputs **when** build end **then** dict has exact keys including `status_code` and `latency_ms`.

### Phase 4–5

Do **not** flesh middleware behavior in this step. Optional: implement the pure helpers so contract tests go green—allowed only for `resolve_request_id` and event builders. Middleware remains unwired.

## Pass / fail

### Must pass before leaving this step

- [ ] `request_context.py` exists with frozen constants and public helper signatures matching the tables.
- [ ] `pytest inference-api/tests/test_request_context.py -q` runs; contract tests for resolve + event shape either fail for `NotImplementedError` / wrong result **or** pass if pure helpers were implemented.
- [ ] No middleware registered in `main.py`.
- [ ] No new observability vendor packages in dependencies.

### Must fail / must not happen

- [ ] Changing infer or health route handlers.
- [ ] Emitting logs from helpers as a side effect (builders return dicts only).
- [ ] Altering success response JSON schemas.

## Commands

```bash
cd inference-api
pytest tests/test_request_context.py -q
```

Expected (helpers stubbed): failures citing `NotImplementedError` or assertion mismatches on event keys—not import errors.

Expected (helpers implemented): all tests in `test_request_context.py` green; existing `tests/test_infer_api.py` still green and unchanged in behavior.

## Done when

Contracts and tests encode header rules, log fields, skip paths, and the error-body key name. Ready for Step 2 to implement middleware against these seams.
