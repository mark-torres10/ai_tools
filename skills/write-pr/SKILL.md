---
name: write-pr
description: Drafts or refines PR descriptions following HOW_TO_WRITE_PR rules. Use when creating a PR, writing a PR description, or when the user asks for help with a pull request.
disable-model-invocation: true
metadata:
  owner: mark
  scope: project
  category: planning
---

# Write PR

Draft or refine PR descriptions using the rules below.

## When to Use

- User asks to create a PR, write a PR description, or draft a pull request.
- User wants help refining an existing PR description.
- User asks how to structure a PR for this project.

## Workflow

1. Gather context: changed files, planning file (if any), related docs.
2. Draft or refine the PR description using the required sections below.
3. Ensure tone: terse, direct, present tense. No filler.

---

## Tone and conventions

**Tone:** Keep descriptions terse and direct. Use present tense. Avoid filler.

**When a planning file exists:** Copy Overview, Happy Flow, Data Flow, and Manual Verification directly from it. Fill in Problem, Solution, and Changes yourself.

---

## PR title

Use a verb + what. Be specific. Keep it short (under ~60 chars when possible).

- **Add** – New feature or capability
- **Update** – Change to existing behavior (including config/fixes)
- **Disable** / **Enable** – Toggle behavior
- **Migrate** – Refactor or move to new pattern
- **Connect** – Wire UI to backend, or integrate systems
- **Improve** – Better error handling, UX, or implementation

*Examples:*
- `Add OAuth with Supabase`
- `Add slowapi rate limiter on POST endpoints`
- `Disable auth during local dev`
- `Update docker remove nonroot user`
- `Migrate feed ranking algorithms to a registry pattern`
- `Add stronger feed algorithm typing and contracts`
- `Connect UI and backend so default config is fetched from the backend`
- `Improve fetch error handling and structured API errors`

---

## Required sections

### Overview

Copy from the corresponding planning file. One paragraph: what we're building and why.

*Example:*
> Add OAuth with Supabase Auth for the app. Enable Sign-In with Google and GitHub. We don't do user-level tracking yet—just gate unauthenticated access to the app itself.

---

### Problem / motivation

Why this change. For bugs or deploy fixes, include the actual error message.

*Example (bug/deploy):*
> Deploys in prod were failing:
> ```
> error: failed to create directory `/app/.venv`: Permission denied (os error 13)
> ```
> `appuser` couldn't create the virtualenv because `/app` wasn't writable.

*Example (feature):*
> After PR #96 (OAuth), every API call requires a JWT. Local dev and headless tests need OAuth + session setup, slowing iteration.

---

### Solution

One or two sentences summarizing what was done.

*Example:*
> Opt-in bypass via `DISABLE_AUTH=1` (backend) and `NEXT_PUBLIC_DISABLE_AUTH=true` (frontend). Local-only; never in production.

---

### Happy Flow

Copy from the planning file. Enumerated steps with file references.

*Example:*
> 1. **Run creation** – `RunRequest` accepts `feed_algorithm`; validation via `feeds.algorithms.validators.validate_feed_algorithm`.
> 2. **Feed generation** – `feeds/feed_generator.py` calls `registry.get_feed_generator(feed_algorithm)`, runs it on candidate posts, persists `GeneratedFeed`.
> 3. **API exposure** – `GET /v1/simulations/feed-algorithms` returns registered algorithms.

---

### Data Flow

Copy from the planning file when present. How data or logic moves end-to-end.

---

### Changes

Bulleted list of file-level changes. One line per file or logical group.

*Example:*
> - `simulation/api/dependencies/auth.py`: when `DISABLE_AUTH=1`, return mock payload instead of validating JWT
> - `ui/contexts/AuthContext.tsx`: when `NEXT_PUBLIC_DISABLE_AUTH=true`, treat as authenticated with mock user
> - `docs/runbooks/LOCAL_DEV_AUTH.md`: usage and session persistence

---

### Manual Verification

Copy from the planning file. Exact commands and expected outcomes.

*Example:*
> - `uv run pytest tests/feeds/test_feed_generator.py -v` — all pass
> - `curl -s http://localhost:8000/v1/simulations/feed-algorithms` — returns 200 with `[{"id":"chronological",...}]`
> - `POST /v1/simulations/run` with `{"feed_algorithm": "invalid"}` — returns 422

For deploy-related PRs, add live URLs:
> - Health: https://app.example.com/health → `{"status":"ok"}`

---

## UI changes: State (Before) / State (After)

Include before and after screenshots from `docs/plans/<folder>/images/before/` and `docs/plans/<folder>/images/after/`.

*Example:*
```markdown
## State (Before)

![Sign-in required](docs/plans/2026-02-20_auth_phase1_gate_app_382915/images/before/sign_in_prompt.png)

## State (After)

![Authenticated sidebar](docs/plans/2026-02-20_auth_phase1_gate_app_382915/images/after/sidebar_user.png)
```

Or reference the folder: `Screenshots: docs/plans/2026-02-20_auth_phase1_gate_app_382915/`

If you don't have these pictures, prompt the user for further instruction.

---

## Optional: Target structure

For refactors, show new layout in a code block.
```text
feeds/
├── algorithms/
│   ├── registry.py
│   └── implementations/chronological.py
└── feed_generator.py
```

---

## Reference PRs

Example PRs that follow these conventions:

| PR | Title | Notes |
|----|-------|-------|
| [96](https://github.com/METResearchGroup/social_agent_simulation_platform/pull/96) | Add OAuth with Supabase | Overview, verification screenshots |
| [98](https://github.com/METResearchGroup/social_agent_simulation_platform/pull/98) | Disable auth during local dev | Problem/Solution/Changes, screenshots path |
| [92](https://github.com/METResearchGroup/social_agent_simulation_platform/pull/92) | Migrate feed ranking algorithms to a registry pattern | Happy Flow, Target Structure, Manual Verification |
| [93](https://github.com/METResearchGroup/social_agent_simulation_platform/pull/93) | Add slowapi rate limiter on POST endpoints | Solution, implementation details |
| [95](https://github.com/METResearchGroup/social_agent_simulation_platform/pull/95) | Update docker remove nonroot user | Problem with error, Verification with live URLs |
| [97](https://github.com/METResearchGroup/social_agent_simulation_platform/pull/97) | Add stronger feed algorithm typing and contracts | Happy Flow, minimal |

---

## Constraints

- Do not skip required sections. Use placeholders or "N/A" only when truly inapplicable.
- When a planning file exists, copy Overview, Happy Flow, Data Flow, Manual Verification from it.
- If UI screenshots are missing, prompt the user for instruction.
