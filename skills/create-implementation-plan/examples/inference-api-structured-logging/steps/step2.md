# Step 2: Add correlation middleware

Implement and register ASGI/HTTP middleware that resolves the request id, binds it on request state, emits JSON start/end access logs (except health), measures latency, and echoes `X-Request-ID` on the response. Handlers stay free of access-log code.

## Scope

- **Caller:** `inference-api/app/main.py` — app factory registers the middleware so every request (including `POST /v1/infer`) passes through it.
- **Slice:** resolve id → bind state → optional start log → call next → set response header → optional end log with status + latency.
- **Out of scope:** Changing error JSON bodies (Step 3); changing infer business logic; metrics/tracing exporters.

## Files

### Inspect

- `inference-api/app/request_context.py` — helpers and constants from Step 1
- `inference-api/app/main.py` — existing middleware order
- `inference-api/app/logging_setup.py` — how to obtain a logger that writes JSON lines to stdout
- `inference-api/app/routes/health.py` — confirm paths are exactly `/health` and `/ready`
- `inference-api/tests/conftest.py` — TestClient / ASGI transport fixture
- `inference-api/tests/test_request_context.py` — extend with middleware integration cases

### Allowed to change

- `inference-api/app/middleware/request_id.py` — **create** (middleware class or `BaseHTTPMiddleware` / pure ASGI callable)
- `inference-api/app/main.py` — register middleware only
- `inference-api/app/logging_setup.py` — ensure a named logger (e.g. access logger) emits one JSON object per log record to stdout
- `inference-api/app/request_context.py` — small helpers only if needed (e.g. `should_access_log(path)`)
- `inference-api/tests/test_request_context.py` — middleware tests
- `inference-api/tests/conftest.py` — only if a log-capture fixture is required

### Forbidden to change

- `inference-api/app/routes/infer.py`
- `inference-api/app/routes/health.py`
- `inference-api/app/errors.py` (error body `request_id` is Step 3)
- Model loading / scoring modules under `inference-api/app/` unrelated to HTTP edge
- Adding OpenTelemetry, Datadog, or other vendor SDKs

## Behavior requirements

1. On each request, read `X-Request-ID`; call `resolve_request_id`; set `request.state.request_id`.
2. If path ∉ `ACCESS_LOG_SKIP_PATHS`, log start event via JSON logger (`json.dumps` of `build_request_start_event(...)` as the log message, or structured `extra` that the JSON formatter serializes—pick one approach and use it consistently).
3. Call the downstream app; record start time with `time.perf_counter()`.
4. Set response header `X-Request-ID` to the resolved id (success and error statuses).
5. If path not skipped, log end event with `status_code` and `latency_ms` ≥ 0.
6. Downstream exceptions still produce an end log if a response status is available after exception handlers; if the middleware catches nothing, document that Step 3’s handlers run inside the stack so status is visible—register this middleware outermost (or outermost after only proxy middleware) so it sees final status codes.

## Implement-from-spec phases

### Phase 0

Caller = `create_app()` in `main.py` registering middleware. UoW = one request through middleware.

### Phase 1 — Scaffold

Add `middleware/request_id.py` with a stub `RequestIdMiddleware` imported and added in `main.py`. Stub `__call__` / `dispatch` raises `NotImplementedError` only if tests are not yet written; prefer thin stub that calls `call_next` without logging so the app still boots, then flesh in Phase 4.

### Phase 2 — Contracts

Public surface: middleware constructor takes the app (and optionally a logger). No new request/response body schemas.

### Phase 3 — Test design (failing then green)

Using TestClient + caplog or a custom logging handler that captures stdout/logger records:

1. **Given** no `X-Request-ID` on `POST /v1/infer` **when** request completes **then** response has `X-Request-ID` matching UUID4 shape; start and end log lines share that id; end has `status_code` and `latency_ms`.
2. **Given** valid `X-Request-ID: client-req-1` **when** request completes **then** response header equals `client-req-1`; both log events use `client-req-1`.
3. **Given** invalid header (empty or >128 chars) **when** request completes **then** response header is a generated UUID, not the invalid value.
4. **Given** `GET /health` **when** request completes **then** `X-Request-ID` is present; **no** `request_start` / `request_end` access events.
5. **Given** `GET /ready` **then** same as health (id present, no access events).

### Phase 4 — Flesh UoWs (order)

1. Resolve + bind + response header echo.
2. Start/end logging with latency for non-skip paths.
3. Skip-path behavior for health/ready.
4. Confirm registration order in `main.py`.

### Phase 5

All new middleware tests green; existing `test_infer_api.py` still green.

## Pass / fail

### Must pass

- [ ] `pytest inference-api/tests/test_request_context.py -q` green for middleware cases above.
- [ ] `pytest inference-api/tests/test_infer_api.py -q` green (behavior unchanged aside from new response header).
- [ ] Successful `POST /v1/infer` responses include `X-Request-ID` and do **not** gain a new JSON body field for the id.
- [ ] Access logs are single-line JSON with the frozen fields from Step 1.

### Must fail / must not happen

- [ ] Access logs for `/health` or `/ready`.
- [ ] Handler code in `routes/infer.py` manually logging request ids for this feature.
- [ ] Introduction of a metrics or tracing vendor dependency.

## Commands

```bash
cd inference-api
pytest tests/test_request_context.py tests/test_infer_api.py -q
```

Expected: all tests pass.

Manual smoke (optional):

```bash
cd inference-api
uvicorn app.main:app --port 8000
curl -sD - -o /tmp/infer_body.json -X POST localhost:8000/v1/infer \
  -H 'Content-Type: application/json' \
  -d '{"inputs": {"text": "hello"}}'
```

Expected headers: `X-Request-ID: <uuid-or-echoed>`. Expected stdout: two JSON lines with `"event":"request_start"` and `"event":"request_end"` sharing that id; end line includes `"status_code":200` (or the route’s success status) and `"latency_ms"`.

## Done when

Middleware is registered, ids propagate on headers, access logs emit for infer (not health), and Step 1 contract tests remain green. Error JSON still without `request_id` until Step 3.
