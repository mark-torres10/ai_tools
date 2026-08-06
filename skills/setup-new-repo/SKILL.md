---
name: setup-new-repo
description: >-
  Bootstraps a new repo. Use when starting a new repository, scaffolding a greenfield
  project, or the user asks to set up a new repo / project tooling.
disable-model-invocation: true
metadata:
  owner: mark
  scope: global
  category: project_setup
---

# Setup new repo

Bootstrap a greenfield (or nearly empty) project with the user's standard
tooling. Do the steps in order. Do not skip the GitHub question.

## When to use

- User asks to set up a new repo, scaffold a new project, or initialize tooling.
- Repo has little or no existing package/CI setup.

## Do not use

- Existing mature repos that already have uv, pre-commit, and CI — fix or extend
  those instead of replacing them.
- Pure planning with no intent to write files.

## Inputs to resolve first

Before writing files, confirm (ask if missing):

1. **Project root** — current workspace unless the user names another path.
2. **Project name** — for `pyproject.toml` `[project].name` (kebab-case).
3. **Stack** — Python-only vs Python + JS/TS (frontend). Default Python-only
   unless a `package.json` / `ui/` / frontend intent is clear.
4. **Python version** — default `>=3.10`, target `3.12` for tooling.

## Workflow checklist

```
Setup progress:
- [ ] 1. uv + pyproject.toml
- [ ] 2. Copy global Cursor skills → project .cursor/skills
- [ ] 3. Install required project skills via npx skills add
- [ ] 4. .gitignore (Python + JavaScript)
- [ ] 5. Pre-commit + CI (ruff, pyright, complexipy; eslint/oxlint if JS/TS)
- [ ] 6. GitHub remote (ask: connect existing vs create with gh)
- [ ] 7. Verify install hooks and summarize
```

## 1. uv and pyproject.toml

- Prefer `uv init` in the project root if there is no `pyproject.toml` yet.
  Otherwise create or edit `pyproject.toml` for a modern uv project.
- Use **uv only** for Python package management. Never introduce pip/poetry
  as the primary manager.
- Include a `test` (or `dev`) extra / dependency group with at least:
  `ruff`, `pyright`, `complexipy`, `pre-commit`, `pytest`.
- Configure `[tool.ruff]` and `[tool.pyright]` (line-length 88, Python 3.12
  target, basic pyright mode is fine).
- Run `uv sync --extra test` (or the equivalent dependency-group command) and
  commit `uv.lock` when the project is a git repo.

## 2. Copy Cursor skills into the project

Copy **all** skills from the global Cursor skills library into this project's
`.cursor/skills/`:

- **Source:** `~/.cursor/skills/` (each subdirectory that contains a `SKILL.md`)
- **Destination:** `<project>/.cursor/skills/<skill-name>/`

Rules:

- Prefer **copying** skill directories (not symlinks into `~/.cursor/skills`), so
  the project is self-contained for collaborators and other machines.
- If `.cursor/skills/` already has entries, merge: copy missing skills; do not
  overwrite a project skill that differs unless the user asks.
- Skip non-skill entries (e.g. a top-level `README.md` alone).
- After copy, the project should list skills under `.cursor/skills/*/SKILL.md`.

## 3. Install required project skills (`npx skills add`)

Always run these from the project root so the skills land in the project
directory (not only globally). Run each command:

```bash
npx skills add railwayapp/railway-skills@use-railway
npx skills add shadcn/ui@shadcn
npx skills add fastapi/fastapi@fastapi
npx skills add langchain-ai/langchain-skills --skill langgraph-persistence --skill langgraph-fundamentals --skill langgraph-human-in-the-loop --skill ecosystem-primer
npx skills add vercel-labs/agent-skills
```

- If a command prompts for confirmation or target path, choose the **project**
  skill location (e.g. `.agents/skills` / `.cursor/skills` as the CLI offers).
- If a skill is already installed in the project, skip or re-run only if the
  user wants a refresh.
- Do not skip this step for "Python-only" repos; install the full set unless
  the user explicitly opts out of specific packages.

## 4. Gitignore

Create or update `.gitignore` with standard **Python and JavaScript** ignores
(venv, `__pycache__`, `node_modules`, build/dist caches, `.env`, coverage,
editor junk). Preserve any existing project-specific entries.

## 5. Pre-commit and CI

Set up the lint/type/complexity stack the user prefers. Mirror patterns from
repos that use these tools (adjust paths; drop JS pieces if Python-only):

| Tool | Role |
|------|------|
| **ruff** | Lint + format (`ruff check`, `ruff format --check`) |
| **pyright** | Type check |
| **complexipy** | Cognitive complexity |
| **eslint** + **oxlint** | JS/TS lint gate when a frontend exists |

### Pre-commit

- Write `.pre-commit-config.yaml` with ruff (check + format), pyright, and
  complexipy. Hooks should **mirror CI** (same commands).
- Install: `uv run pre-commit install` (after deps are synced).
- For JS/TS: add a local hook that runs the frontend lint CI script (e.g.
  `npm run lint:ci` combining eslint + oxlint), scoped to the frontend tree.

### GitHub Actions CI

- Write `.github/workflows/ci.yml`.
- Minimum Python job: uv setup → sync → ruff check → ruff format --check →
  pyright → complexipy → pytest.
- If JS/TS exists: Node setup → `npm ci` → eslint + oxlint lint gate.
- Use `astral-sh/setup-uv`, cache on `pyproject.toml` / `uv.lock`.
- Keep commands runnable on a scaffold (empty tests ok if pytest exits 0).
  Do not weaken checks to pass.

If the user names a sibling project whose CI they like, prefer matching that
over inventing a new layout.

## 6. GitHub remote (required ask)

**Always ask** before creating or linking a remote:

1. Connect this local repo to an **existing** GitHub repo (user provides
   `owner/name` or URL)?
2. Or **create** a new GitHub repo with the GitHub CLI?

Then:

- Ensure git is initialized (`git init` if needed).
- **Existing:** `gh repo set-default` / `git remote add origin <url>` as
  appropriate; confirm with `gh repo view`.
- **Create:** `gh repo create` with the agreed visibility (ask private vs
  public if unclear), then set `origin` and push when the user wants an
  initial push.
- Do not force-push. Do not make the repo public unless the user said so.

## 7. Verify and summarize

1. `uv sync --extra test` (or equivalent) succeeds.
2. `uv run pre-commit run --all-files` — fix scaffold issues or note expected
   first-run noise.
3. Confirm `.cursor/skills/` has the copied global skills.
4. Confirm the `npx skills add` packages are present in the project.
5. Confirm remote: `git remote -v` / `gh repo view`.

Return a short summary: paths created, stack chosen, skills copied / added,
remote URL or “no remote yet”, and any follow-ups for the user.

## Constraints

- Do not invent product application code beyond minimal package scaffolding.
- Do not commit secrets. Do not push unless the user wants the initial push
  as part of GitHub setup.
