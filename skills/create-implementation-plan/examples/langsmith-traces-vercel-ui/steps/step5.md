# Step 5: Deploy to Vercel and verify the happy path

## Goal

Deploy `apps/langsmith-trace-viewer/` to Vercel, configure server env and Deployment Protection, and verify the production (or preview) URL lists real traces and opens detail for a known run id from `helix-staging-agents`.

## Main caller

Engineer browser against the deployed Vercel URL (not localhost).

## Files to inspect

- `apps/langsmith-trace-viewer/package.json` (build/start scripts)
- `apps/langsmith-trace-viewer/next.config.ts`
- `apps/langsmith-trace-viewer/.env.example`
- Repo root Vercel/monorepo settings if an existing `vercel.json` or Turborepo pipeline defines app roots

## Files allowed to change

- `apps/langsmith-trace-viewer/vercel.json` only if required to set the app root/build command for this package
- Root docs or deploy notes **only if** the repo already keeps per-app deploy docs in-tree (do not invent a new docs site)
- No application feature code unless a build break requires a one-line fix; any fix must be called out in the commit message

## Files forbidden to change

- Fetcher contracts and UI scope from Steps 2–4 (no new features while deploying)
- Adding custom password middleware or SSO providers
- Writing to LangSmith

## Work

1. Create or link a Vercel project whose root directory is `apps/langsmith-trace-viewer/` (or the monorepo equivalent that builds only this app).
2. Set server env on Vercel: LangSmith API key, API base URL, project name `helix-staging-agents`. Mark the API key as sensitive / non-public.
3. Enable **Vercel Deployment Protection** on the project (Standard Protection or the org default). Do not add an in-app password gate.
4. Deploy a production or long-lived preview URL.
5. Verify happy path with a real recent run id from the LangSmith project (copy id from LangSmith UI or from the deployed list).
6. Commit any necessary `vercel.json` / build config; leave secrets only in Vercel env, never in git.

## Commands (exact)

From repo root (adjust package manager if the monorepo uses pnpm/yarn):

```bash
cd apps/langsmith-trace-viewer
npm run build
```

Expected: Next.js build completes with exit code `0`.

```bash
npx vercel link --yes
npx vercel env pull .env.vercel.local
```

Expected: project linked; env pull succeeds only after env vars were set in the Vercel dashboard (do not commit `.env.vercel.local`).

```bash
npx vercel deploy --prod
```

Expected: CLI prints a production URL; deploy status ready.

Against the deployed URL (replace `DEPLOY_URL`; include Deployment Protection bypass/cookie headers if your org requires them for CLI curls):

```bash
curl -s -o /dev/null -w "%{http_code}" "https://DEPLOY_URL/"
```

Expected: `200` (or `401`/`403` from Deployment Protection when unauthenticated—then retry as an allowed user in the browser and confirm `200`).

Browser checks (required):

1. Open `https://DEPLOY_URL/` while authenticated via Deployment Protection → table shows recent traces for the last 24 hours.
2. Click one row → detail shows status, timing, inputs/outputs or error.
3. Confirm the page source / network panel shows calls only to the same Vercel origin (or RSC payloads), not to LangSmith from the browser.

## Pass / fail

| Check | Pass | Fail |
| --- | --- | --- |
| Build | `npm run build` exit `0` | Build errors |
| Env | API key + project set on Vercel; not in git | Key committed or missing |
| Protection | Deployment Protection enabled | Fully public with no protection when org requires it |
| Happy path | List + detail work on deploy URL | Empty silent list or client-side LangSmith calls |
| Scope | No SSO/password feature added | Custom auth app code shipped |

## Out of scope

- Multi-project support
- Custom domain DNS beyond what Vercel already provides for the project
- Alerting, metrics, or full observability platform features
