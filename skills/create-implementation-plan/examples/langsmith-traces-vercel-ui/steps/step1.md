# Step 1: Scaffold the Next.js app and LangSmith config

## Goal

Stand up a minimal Next.js App Router app at `apps/langsmith-trace-viewer/` with server-only LangSmith env wiring and a local health page that proves the app boots.

## Main caller

Local `npm run dev` → `apps/langsmith-trace-viewer/src/app/page.tsx` renders a static health string. No LangSmith calls in this step.

## Files to inspect

- Repo root package/workspace config (whatever already declares `apps/*`), e.g. `package.json`, `pnpm-workspace.yaml`, or `turbo.json` if present
- Existing Next.js apps under `apps/` for version and layout conventions (copy the nearest App Router app's Next major version)

## Files allowed to change

- `apps/langsmith-trace-viewer/package.json`
- `apps/langsmith-trace-viewer/tsconfig.json`
- `apps/langsmith-trace-viewer/next.config.ts`
- `apps/langsmith-trace-viewer/.env.example`
- `apps/langsmith-trace-viewer/.gitignore`
- `apps/langsmith-trace-viewer/src/app/layout.tsx`
- `apps/langsmith-trace-viewer/src/app/page.tsx`
- `apps/langsmith-trace-viewer/src/lib/env.ts` (read-only accessors for required env; throw if missing—no network)

## Files forbidden to change

- Any existing production service under `apps/` other than `langsmith-trace-viewer/`
- LangSmith SDK / HTTP client modules (do not add yet)
- Auth, middleware, or Deployment Protection config (Step 5)

## Work

1. Create `apps/langsmith-trace-viewer/` with Next.js App Router (TypeScript), matching the monorepo's package manager.
2. Add `.env.example` documenting three server-only values: LangSmith API key, LangSmith API base URL (default LangSmith cloud), and project name (default `helix-staging-agents`).
3. Add `src/lib/env.ts` that reads those values and fails fast if the API key or project name is empty. Do not prefix them for public Next.js exposure.
4. Make `src/app/page.tsx` render a single line confirming the app is up (no secrets printed).
5. Commit the scaffold.

## Commands (exact)

From `apps/langsmith-trace-viewer/`:

```bash
cp .env.example .env.local
# Edit .env.local: set LANGSMITH_API_KEY to a non-empty placeholder for local boot.
npm install
npm run dev
```

Expected: process listens on `http://localhost:3000` without crash.

```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/
```

Expected output: `200`

```bash
curl -s http://localhost:3000/ | head
```

Expected: HTML or text that includes a clear "up" / health indicator; must not include the API key string.

## Pass / fail

| Check | Pass | Fail |
| --- | --- | --- |
| App directory exists | `apps/langsmith-trace-viewer/src/app/page.tsx` present | Missing app or wrong path |
| Local boot | `curl` returns `200` | Non-200 or process exits |
| Secrets not leaked | Health response body does not contain the API key | Key appears in HTML |
| Env contract | Missing API key or project name causes a clear server error when env helpers are invoked in a one-off script or later step | Silent empty defaults |
| Scope | No LangSmith HTTP calls yet | Fetcher or UI list/detail added early |

## Out of scope

- Trace list/detail UI
- LangSmith list/get client
- Vercel project creation (Step 5)
