# Step 3: Attach request id to error responses

Wire the shared error path so every 4xx/5xx JSON body includes `request_id` equal to `request.state.request_id` (the same value echoed on `X-Request-ID`). Do not duplicate access logging inside handlers.

## Scope

- **Caller:** Existing FastAPI exception handlers / `inference-api/app/errors.py` helpers used when validation fails or `POST /v1/infer` raises.
- **Slice:** Attach `request_id` on error responses for (1) request validation errors, (2) handler-raised HTTP errors, (3) unhandled exceptions mapped to 500.
- **Out of scope:** Changing success payload shape; new error taxonomy; client SDK changes; metrics/tracing.

## Files

### Inspect

- `inference-api/app/errors.py` — how error dicts and handlers are built today
- `inference-api/app/main.py` — where handlers are registered
- `inference-api/app/middleware/request_id.py` — confirms `request.state.request_id` is set before handlers run
- `inference-api/app/routes/infer.py` — how failures are raised (HTTPException vs domain errors)
- `inference-api/tests/test_infer_api.py` — existing failure cases to extend

### Allowed to change

- `inference-api/app/errors.py` — add `request_id` into the error payload builder; read id from the current request
- `inference-api/app/main.py` — only if handler registration must pass request-aware callables
- `inference-api/tests/test_infer_api.py` — assert `request_id` on error bodies
- `inference-api/tests/test_request_context.py` — cross-check header id == body `request_id`

### Forbidden to change

- `inference-api/app/routes/infer.py` except if a one-line re-raise is required to use the shared helper (prefer fixing handlers globally so routes stay untouched)
- Success response models / OpenAPI success schemas
- Logging middleware behavior from Step 2 (no second access-log implementation)
- Vendor APM/metrics packages

## Behavior requirements

1. Error JSON includes `"request_id": "<resolved id>"` alongside existing fields.
2. Value matches the `X-Request-ID` response header for that same response.
3. If somehow state is missing (should not happen if middleware is outermost), generate a UUID4 for the body **and** still set the response header consistently—or fail the test suite if middleware order is wrong; prefer fixing order over silent divergence.
4. Validation errors (e.g. malformed JSON or missing required field on `/v1/infer`) include `request_id`.
5. Domain/HTTP errors from the infer handler include `request_id`.
6. Unhandled exceptions that become 500 include `request_id`.
7. Do not add `request_id` to **2xx** JSON bodies.

## Implement-from-spec phases

### Phase 0

Caller = exception handlers registered on the app (entry from `errors.py` / `main.py`). Slice = build_error_body(request, ...) → JSONResponse.

### Phase 1 — Scaffold

Add a typed helper signature, e.g. `error_body(request, *, status_code, **existing_fields) -> dict`, stubbed if needed; wire handlers to call it.

### Phase 2 — Contracts

Error payload = existing keys + required `request_id: str`. No other new required keys.

### Phase 3 — Test design

1. **Given** invalid infer body **when** `POST /v1/infer` **then** status 4xx; body has `request_id`; header `X-Request-ID` equals body `request_id`; end access log `status_code` matches.
2. **Given** a forced handler error (use existing failure fixture or a test-only dependency override) **when** infer fails **then** error body and header share the client-supplied valid id.
3. **Given** unhandled exception path (if the app has a catch-all handler) **when** triggered **then** 500 body includes `request_id`.
4. **Given** successful infer **when** 200 **then** body does **not** contain `request_id`.

### Phase 4 — Flesh UoWs

1. Central `error_body` / helper reads `request.state.request_id`.
2. Validation exception handler.
3. HTTPException / domain handler.
4. Unhandled exception handler (if present).

### Phase 5

All error-path tests green; success tests still assert no body `request_id`.

## Pass / fail

### Must pass

- [ ] `pytest inference-api/tests/test_infer_api.py inference-api/tests/test_request_context.py -q` green.
- [ ] Every tested 4xx/5xx JSON response from the API includes `request_id` matching the response header.
- [ ] Access end logs from Step 2 still fire once per non-health request (no duplicate start/end pairs from error handling).

### Must fail / must not happen

- [ ] Success responses gaining `request_id` in JSON.
- [ ] Different ids in header vs error body for the same response.
- [ ] Per-route copy-pasted logging for correlation.

## Commands

```bash
cd inference-api
pytest tests/test_infer_api.py tests/test_request_context.py -q
```

Expected: all pass.

```bash
curl -sD - -X POST localhost:8000/v1/infer \
  -H 'Content-Type: application/json' \
  -H 'X-Request-ID: err-demo-1' \
  -d '{}'
```

Expected: 4xx response; header `X-Request-ID: err-demo-1`; body JSON contains `"request_id":"err-demo-1"`.

## Done when

All error responses from the shared handlers carry the middleware’s request id; success bodies unchanged. Ready for Step 4 end-to-end verification checklist.
