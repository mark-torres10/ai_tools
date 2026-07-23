# Step 3: Expose list and detail behind App Router handlers

## Goal

Add server-only App Router handlers that call the Step 2 fetcher and return JSON for list and detail. Map auth, not-found, and upstream failures to clear HTTP status codes. Never put the LangSmith API key in responses or client bundles.

## Main caller

`GET` handlers:

- `apps/langsmith-trace-viewer/src/app/api/traces/route.ts` → `listRecentTraces`
- `apps/langsmith-trace-viewer/src/app/api/traces/[id]/route.ts` → `getTraceById`

## Files to inspect

- `apps/langsmith-trace-viewer/src/lib/langsmith/fetch-traces.ts`
- `apps/langsmith-trace-viewer/src/lib/langsmith/types.ts`
- `apps/langsmith-trace-viewer/src/lib/env.ts`
- `apps/langsmith-trace-viewer/src/app/layout.tsx` (confirm no client provider that could leak env)

## Files allowed to change

- `apps/langsmith-trace-viewer/src/app/api/traces/route.ts`
- `apps/langsmith-trace-viewer/src/app/api/traces/[id]/route.ts`
- `apps/langsmith-trace-viewer/src/lib/langsmith/errors.ts` (optional shared error → HTTP mapping)
- `apps/langsmith-trace-viewer/src/app/api/traces/__tests__/route.test.ts` (or colocated handler tests if that matches repo convention)

## Files forbidden to change

- `apps/langsmith-trace-viewer/src/lib/langsmith/fetch-traces.ts` behavior contracts from Step 2 (call only; do not broaden the fetcher API)
- Client components that import `env.ts` or the LangSmith client
- Middleware auth / SSO
- Public `NEXT_PUBLIC_*` copies of the API key

## Work

1. Implement `GET /api/traces`: call `listRecentTraces`; on success return `200` with a JSON array of list items; on auth/config failure return `502` or `503` with a short error message (no stack, no key).
2. Implement `GET /api/traces/[id]`: call `getTraceById`; `200` on success; `404` on not found; same upstream mapping as list for auth/config failures.
3. Confirm neither handler accepts a project name or time-window override from the query string (fixed env project + 24h).
4. Add handler tests with the fetcher mocked: success, not-found, auth failure.
5. Commit.

## Commands (exact)

From `apps/langsmith-trace-viewer/`:

```bash
npm test -- --run src/app/api/traces
```

Expected: exit code `0`.

With the app running and valid stubbed or real env (local only):

```bash
curl -s -o /tmp/traces.json -w "%{http_code}" http://localhost:3000/api/traces
```

Expected with valid credentials and upstream available: `200` and a JSON array.

```bash
curl -s http://localhost:3000/api/traces | head -c 200
```

Expected: JSON starting with `[`; body must not contain the literal API key.

```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/api/traces/does-not-exist-id
```

Expected with fetcher wired: `404` (or the status your not-found mapping defines—must not be `200` with an empty success object).

## Pass / fail

| Check | Pass | Fail |
| --- | --- | --- |
| List route | `200` + JSON array on success | HTML page or client-side LangSmith call |
| Detail route | `200` / `404` mapped correctly | Always `200` |
| Secret hygiene | Response and client bundle grep show no API key | Key in JSON or `NEXT_PUBLIC_` |
| No query overrides | Project/window ignored if passed | Caller can select another project |
| Fetcher reused | Handlers call Step 2 functions | Duplicated HTTP logic in routes |

## Out of scope

- HTML list/detail pages (Step 4)
- Vercel deploy (Step 5)
