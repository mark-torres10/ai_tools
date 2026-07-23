# Step 2: Implement the server-side trace fetcher

## Goal

One server-side module lists recent root runs for the configured project in the last 24 hours and fetches a single run by id. Tests first against stubbed LangSmith HTTP responses; then implement until green.

## Main caller

Unit tests under `apps/langsmith-trace-viewer/src/lib/langsmith/__tests__/` call the fetcher. App routes and pages are not callers yet (Step 3–4).

## Files to inspect

- `apps/langsmith-trace-viewer/src/lib/env.ts` (from Step 1)
- LangSmith REST docs for listing runs and reading a run by id (official API reference for the SDK/HTTP version pinned in `package.json`)
- `apps/langsmith-trace-viewer/package.json` for test runner choice (prefer the repo's existing Vitest/Jest pattern if one exists)

## Files allowed to change

- `apps/langsmith-trace-viewer/package.json` (add LangSmith client dependency + test script only if missing)
- `apps/langsmith-trace-viewer/src/lib/langsmith/types.ts` (contracts only: list item + detail summary shapes)
- `apps/langsmith-trace-viewer/src/lib/langsmith/client.ts` (thin HTTP/SDK wrapper injectable for tests)
- `apps/langsmith-trace-viewer/src/lib/langsmith/fetch-traces.ts` (`listRecentTraces`, `getTraceById`)
- `apps/langsmith-trace-viewer/src/lib/langsmith/__tests__/fetch-traces.test.ts`
- `apps/langsmith-trace-viewer/src/lib/langsmith/__tests__/fixtures/` (recorded JSON stubs)

## Files forbidden to change

- `apps/langsmith-trace-viewer/src/app/**` (pages/routes stay health-only until Step 3–4)
- Vercel / CI deploy configs
- Any write/update/delete LangSmith APIs

## Contracts (freeze before behavior)

List item fields exposed to later UI: id, name, status, latency (ms), start time.

Detail fields: id, name, status, latency (ms), start time, end time if present, inputs summary, outputs summary, error text if present.

Fixed window: start = now − 24h, end = now. Project name always from env. No pagination UI; return at most one page of results (document the page size constant in the fetcher module—pick a single explicit limit such as 50).

## Work (implement-from-spec order)

1. **Scaffold:** empty `types.ts`, `client.ts`, `fetch-traces.ts` with stub bodies; test file imports the public functions.
2. **Contracts:** freeze the list/detail types and function signatures; stop if reviewing in a live run—this example assumes approval already given.
3. **Test design (write failing tests first):**
   - Happy list: stub returns two runs → mapped list items with name, status, latency, start time.
   - Happy detail: stub returns one run → mapped detail including inputs/outputs.
   - Detail error run: stub includes error → error text present on detail.
   - Upstream 401/403 → fetcher throws a distinct auth/config error (not an empty list).
   - Upstream 404 on get-by-id → distinct not-found error.
4. **Flesh:** implement client + mapper + list/get until those tests pass. No UI.

## Commands (exact)

From `apps/langsmith-trace-viewer/`:

```bash
npm test -- --run src/lib/langsmith/__tests__/fetch-traces.test.ts
```

Expected before implementation: failures on unimplemented stubs (not import errors).

Expected after implementation: all tests in that file pass (exit code `0`).

## Pass / fail

| Check | Pass | Fail |
| --- | --- | --- |
| Tests exist first | Failures are assertion/NotImplemented, then turn green | Implementation committed with no tests |
| List mapping | Only required list fields; 24h window passed into the API call | Wrong window or extra product scope (tags/filters UI) |
| Detail mapping | Inputs/outputs/error surfaced when present | Silent drop of error field |
| Auth failure | Throws; does not return `[]` | Empty list on 401 |
| No UI coupling | `src/app` unchanged | Pages call LangSmith directly |

## Out of scope

- App Router handlers (Step 3)
- Screenshots / UI (Step 4)
- Live calls to production LangSmith in CI (stubs only)
