# Skills

Cursor and Codex skills. Source of truth: `skills/` in this repo.

## Sync to Cursor and Codex

- **Cursor (global):** Copy each skill to `~/.cursor/skills/`
- **Codex (global):** Copy each skill to `~/.codex/skills/`
- **Codex (repo):** `.agents/skills` → symlink to `skills/` (already configured)

| Skill | Description |
|-------|-------------|
| **review-persona** | Review current work using a persona from `agents/personas/`. Slash-only. |
| **review-rules** | Review current work against `agents/task_instructions/rules/`. Slash-only. |
| **explain-as-python** | Explain non-Python code (e.g. TypeScript) through a Python lens—concepts first, then translation. Agent can auto-apply. |
| **create-implementation-plan** | Create implementation plans following `PLANNING_RULES` (Overview, Happy Flow, Manual Verification). Agent can auto-apply. |
| **suggest-rules-additions** | At end of conversation, infers preferences from the exchange and suggests additions to `docs/RULES.md`. Slash-only. |
| **review-security** | Instructs the agent to apply code-security (Semgrep) and security-best-practices (OpenAI). Requires both installed. Slash-only. |
| **create-pr** | Drafts or refines PR descriptions following `HOW_TO_WRITE_PR` rules. Slash-only. |
