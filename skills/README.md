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
| **create-epic** | From a complete plan, file a GitHub parent issue plus one child sub-issue per step (each child = one future PR). Slash-only. |
| **implement-epic** | Implements an existing GitHub epic as a stacked PR (`gh stack`): one child issue per PR, manager spawns one orchestrator per child. Slash-only. |
| **suggest-rules-additions** | At end of conversation, infers preferences from the exchange and suggests additions to `docs/RULES.md`. Slash-only. |
| **review-security** | Instructs the agent to apply code-security (Semgrep) and security-best-practices (OpenAI). Requires both installed. Slash-only. |
| **write-pr-description** | Type-specific PR bodies for experiments, features, bugs, or default (guide/template/examples under `types/`). Slash-only. Single source of truth for PR descriptions. |
| **write-docstring** | Writes Python function, class, or module docstrings (numpy-style) via routed guides. Slash-only. |
| **write-changelog** | Writes terse CHANGELOG entries for shipped PRs. Slash-only. |
| **implement-plan-and-open-pr** | One plan as one PR. Uses `implement-from-spec` for coding, then verify, `write-docstring`, `write-pr-description`, `write-changelog`, post-PR review, return the URL. Slash-only. |
| **interactive-implementation** | Run a plan step-by-step via `implement-plan-and-open-pr`, then at each step run `write-docstring` and `review-for-simplicity` and await approval before committing. Slash-only. |
| **refactor-service** | Diagnose a microservice or pipeline, then plan a behavior-preserving refactor (modularity, tests, ruff/pyright, runbooks, READMEs). Planning only. Slash-only. |
| **fix-ci** | Find or use a PR, triage failing checks, reproduce locally, fix, commit, push, and summarize. Slash-only. |
| **setup-new-repo** | Bootstrap a new repo: uv/pyproject, copy global Cursor skills, npx skills add (railway/shadcn/fastapi/langgraph/vercel), pre-commit+CI, gitignore, GitHub via gh. Slash-only. |
| **handoff** | End-of-session handoff generator that writes `handoff.md` with PR link, done summary, remaining to-dos, and last left off. |
| **create-advisory-brief** | Distills repo context into a copy-paste markdown prompt for an external AI (no codebase access) to evaluate options and recommend a path. Slash-only. |
| **implement-from-spec** | Implements a scoped unit of work from an approved design/plan: caller-first scaffold, contracts agreed upon, test design, then one-function-at-a-time. References under `skills/implement-from-spec/`. Agent can auto-apply. |

## Some notes on how these fit together

The `implement-*` skills fit as part of a stack. We structure multi-PR builds as epics, managed by `implement-epic`. Each PR is then built using `implement-plan-and-open-pr`, which uses `impleent-from-spec` to actually write the code.

```
implement-epic                         # manager: stack, CI, children
  per child:
    create-implementation-plan          # one-PR plan against current stack base
    implement-plan-and-open-pr        # one plan → one PR (`gh stack` instead of `gh pr create`)
      implement-from-spec             # write code for one task; commits as it goes
      write-docstring
      verify
      write-pr-description
      write-changelog
      post-PR review                   # comprehensive-code-review, plain-writing, review-for-simplicity
```
