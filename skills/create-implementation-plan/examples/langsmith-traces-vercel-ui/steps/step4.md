# Step 4: Build the list and detail pages

## Goal

Replace the health-only home page with a plain list of recent traces and a detail page for one run id. Pages load data on the server (call the Step 2 fetcher or the Step 3 routes via server-side fetch—prefer direct fetcher calls from Server Components to avoid an extra hop). Capture before/after screenshots.

## Main caller

Engineer browser:

- `GET /` → list table
- `GET /traces/[id]` → detail summary

## Files to inspect

- `apps/langsmith-trace-viewer/src/app/page.tsx` (current health page)
- `apps/langsmith-trace-viewer/src/app/api/traces/route.ts`
- `apps/langsmith-trace-viewer/src/app/api/traces/[id]/route.ts`
- `apps/langsmith-trace-viewer/src/lib/langsmith/types.ts`
- `apps/langsmith-trace-viewer/src/app/layout.tsx`

## Files allowed to change

- `apps/langsmith-trace-viewer/src/app/page.tsx` (list)
- `apps/langsmith-trace-viewer/src/app/traces/[id]/page.tsx` (detail)
- `apps/langsmith-trace-viewer/src/app/error.tsx` (optional explicit error UI for failed loads)
- `apps/langsmith-trace-viewer/src/components/trace-list.tsx` (presentational list only, if split helps)
- `apps/langsmith-trace-viewer/src/components/trace-detail.tsx` (presentational detail only, if split helps)
- `apps/langsmith-trace-viewer/src/app/globals.css` (minimal typography/spacing only—no design-system expansion)
- Screenshot artifacts under this plan folder:
  - `skills/create-implementation-plan/examples/langsmith-traces-vercel-ui/images/before/`
  - `skills/create-implementation-plan/examples/langsmith-traces-vercel-ui/images/after/`

## Files forbidden to change

- `apps/langsmith-trace-viewer/src/lib/langsmith/fetch-traces.ts` contracts
- Client-side imports of the LangSmith API key or client module
- Charts, dashboards, filters, multi-project controls, realtime/WebSocket code

## Screenshots (required)

Before implementing UI changes, with the app on the health page (or empty shell):

1. Save `images/before/home.png` — viewport of `/`.

After list + detail work:

2. Save `images/after/list.png` — `/` showing the trace table (or the explicit error state if credentials are intentionally unset for the shot).
3. Save `images/after/detail.png` — `/traces/<id>` for a known run id showing summary fields.

Paths are relative to this example plan directory:
`skills/create-implementation-plan/examples/langsmith-traces-vercel-ui/`.

## Work

1. Capture before screenshot.
2. Implement `/` as a Server Component that loads recent traces and renders a table: name (link), status, latency, start time.
3. Implement `/traces/[id]` as a Server Component that loads one trace and renders status, timing, inputs, outputs, and error when present. Invalid id shows a clear not-found message.
4. On fetcher auth/config failure, show an explicit error message on the page (not an empty table that looks like “no traces”).
5. Capture after screenshots; commit code + images.

## Commands (exact)

```bash
cd apps/langsmith-trace-viewer && npm run dev
```

Expected: server up on `http://localhost:3000`.

```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/
curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/traces/sample-id
```

Expected with valid data for list: `200` on `/`. Expected for unknown id: `200` with not-found UI or `404` page—must not render another trace's data.

Manual: open `/`, click a name link, confirm detail fields match the API/detail fetcher for that id.

## Pass / fail

| Check | Pass | Fail |
| --- | --- | --- |
| List columns | Name, status, latency, start time only | Tags/type filters/charts |
| Detail | Shows inputs/outputs/error when present | Blank detail on success |
| Error state | Auth failure is visible copy | Silent empty list |
| Server-only secrets | No client LangSmith client | Browser network tab calls LangSmith |
| Screenshots | before home + after list/detail present | Missing image files |

## Out of scope

- Vercel production deploy (Step 5)
- Styling beyond readable default layout
