# Step 4: Verify end-to-end on the inference route

Prove the full happy and failure paths on `POST /v1/infer` against the plan’s “done” criteria. No new feature work unless a gap fails a check—then fix in the owning module from Steps 1–3 and re-run.

## Scope

- **Caller:** `POST /v1/infer` through middleware + routes + error handlers.
- **Slice:** Automated regression suite + short manual checklist; dependency audit for vendor APM/metrics.
- **Out of scope:** New log fields, sampling, trace export, dashboards, cross-service propagation.

## Files

### Inspect

- `inference-api/app/main.py`
- `inference-api/app/middleware/request_id.py`
- `inference-api/app/request_context.py`
- `inference-api/app/errors.py`
- `inference-api/app/routes/infer.py`
- `inference-api/app/logging_setup.py`
- `inference-api/pyproject.toml` or `inference-api/requirements.txt`
- `inference-api/tests/test_infer_api.py`
- `inference-api/tests/test_request_context.py`

### Allowed to change

- Test files only, to close coverage gaps for the checklist below
- Bugfixes strictly in files allowed in Steps 1–3 if verification finds a defect

### Forbidden to change

- Adding Datadog, OpenTelemetry, Sentry performance, Prometheus client, or similar dependencies
- Expanding log schema beyond Step 1 fields
- UI or non-API packages outside `inference-api/`

## Verification checklist (must all pass)

### Automated

1. Valid client `X-Request-ID` on successful infer → echoed on response header; start/end logs share id; success JSON **lacks** `request_id`.
2. Missing header on successful infer → generated UUID4 on header; start/end logs share that id.
3. Invalid header → generated UUID4; invalid value never appears in header or logs.
4. Validation failure on infer → 4xx; body `request_id` == header; end log `status_code` is that 4xx.
5. Handler failure on infer → error body and header match; end log status matches.
6. `GET /health` and `GET /ready` → header present; **no** access start/end events.
7. `latency_ms` on end events is a number ≥ 0.
8. Full suite green:

```bash
cd inference-api
pytest -q
```

Expected: all tests pass (exit code 0).

### Dependency audit

```bash
cd inference-api
rg -n "opentelemetry|datadog|ddtrace|prometheus_client|newrelic" pyproject.toml requirements.txt requirements*.txt app || true
```

Expected: no matches for vendor tracing/metrics SDKs introduced by this work.

### Manual smoke (optional but recommended once)

```bash
cd inference-api
uvicorn app.main:app --port 8000

curl -sD - -o /tmp/ok.json -X POST localhost:8000/v1/infer \
  -H 'Content-Type: application/json' \
  -H 'X-Request-ID: e2e-ok-1' \
  -d '{"inputs": {"text": "hello"}}'

curl -sD - -o /tmp/bad.json -X POST localhost:8000/v1/infer \
  -H 'Content-Type: application/json' \
  -H 'X-Request-ID: e2e-bad-1' \
  -d '{}'

curl -sD - localhost:8000/health
```

Expected:

- First call: `200`; header `X-Request-ID: e2e-ok-1`; stdout start+end JSON with that id; `/tmp/ok.json` has no `request_id` field.
- Second call: 4xx; header and body `request_id` both `e2e-bad-1`; end log status matches.
- Health: header present; no access log pair for `/health`.

## Pass / fail

### Must pass

- [ ] All checklist items above.
- [ ] Plan “What done looks like” items 1–5 satisfied.
- [ ] No open todos in middleware/error helpers for this feature.

### Must fail / must not happen

- [ ] Shipping with failing tests “fixed later.”
- [ ] Silent introduction of a metrics/tracing backend.
- [ ] Divergent ids across header, error body, and log lines for one request.

## Done when

`pytest -q` is green, dependency audit is clean, and the inference route demonstrates correlated JSON logs plus error-body ids with header-only success correlation—matching [../plan.md](../plan.md).
