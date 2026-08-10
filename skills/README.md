# Skills

Cursor and Codex skills. Source of truth: `skills/` in this repo.

## Sync to Cursor and Codex

- **Cursor (global):** Copy each skill to `~/.cursor/skills/`
- **Codex (global):** Copy each skill to `~/.codex/skills/`

| Skill | Description |
|-------|-------------|
| **review-persona** | Review current work using a persona from `agents/personas/`. Slash-only. |
| **review-rules** | Review current work against `agents/task_instructions/rules/`. Slash-only. |
| **review-for-simplicity** | Review plans, proposals, and diffs for unnecessary complexity, premature abstraction, and unverified assumptions. Slash-only. |
| **explain-as-python** | Explain non-Python code (e.g. TypeScript) through a Python lens—concepts first, then translation. Agent can auto-apply. |
| **create-implementation-plan** | Draft-then-confirm implementation plans (`plan.md` router + `steps/`), then expand step details via `implement-from-spec`. Examples under `skills/create-implementation-plan/examples/`. Agent can auto-apply. |
| **suggest-rules-additions** | At end of conversation, infers preferences from the exchange and suggests additions to `docs/RULES.md`. Slash-only. |
| **review-security** | Instructs the agent to apply code-security (Semgrep) and security-best-practices (OpenAI). Requires both installed. Slash-only. |
| **write-pr-description** | Type-specific PR bodies for experiments, features, bugs, or default (guide/template/examples under `types/`). Slash-only. Single source of truth for PR descriptions. |
| **write-docstring** | Writes Python function, class, or module docstrings (numpy-style) via routed guides. Slash-only. |
| **write-changelog** | Writes terse CHANGELOG entries for shipped PRs. Slash-only. |
| **implement-plan-and-open-pr** | Execute a plan end-to-end, verify, apply `write-docstring` for docstrings, open a PR using `write-pr-description`, update CHANGELOG via `write-changelog`, return the URL. Slash-only. |
| **interactive-implementation** | Run a plan step-by-step via `implement-plan-and-open-pr`, then at each step run `write-docstring` and `review-for-simplicity` and await approval before committing. Slash-only. |
| **refactor-service** | Diagnose a microservice or pipeline, then plan a behavior-preserving refactor (modularity, tests, ruff/pyright, runbooks, READMEs). Planning only. Slash-only. |
| **fix-ci** | Find or use a PR, triage failing checks, reproduce locally, fix, commit, push, and summarize. Slash-only. |
| **setup-new-repo** | Bootstrap a new repo: uv/pyproject, copy global Cursor skills, npx skills add (railway/shadcn/fastapi/langgraph/vercel), pre-commit+CI, gitignore, GitHub via gh. Slash-only. |
| **handoff** | End-of-session handoff generator that writes `handoff.md` with PR link, done summary, remaining to-dos, and last left off. |
| **create-advisory-brief** | Distills repo context into a copy-paste markdown prompt for an external AI (no codebase access) to evaluate options and recommend a path. Slash-only. |
| **implement-from-spec** | Implements a scoped unit of work from an approved design/plan: caller-first scaffold, contract freeze, test design, then one-function-at-a-time. References under `skills/implement-from-spec/`. Agent can auto-apply. |
