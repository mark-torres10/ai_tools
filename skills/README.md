# Skills

Cursor skills. Add to global Cursor with the same folder under `~/.cursor/skills/`.

| Skill | Description |
|-------|-------------|
| **review-persona** | Review current work using a persona from `agents/personas/`. Slash-only. |
| **review-rules** | Review current work against `agents/task_instructions/rules/`. Slash-only. |
| **explain-as-python** | Explain non-Python code (e.g. TypeScript) through a Python lens—concepts first, then translation. Agent can auto-apply. |
| **create-implementation-plan** | Create implementation plans following `PLANNING_RULES` (Overview, Happy Flow, Manual Verification). Agent can auto-apply. |
| **suggest-rules-additions** | At end of conversation, infers preferences from the exchange and suggests additions to `docs/RULES.md`. Slash-only. |
| **review-security** | Instructs the agent to apply code-security (Semgrep) and security-best-practices (OpenAI). Requires both installed. Slash-only. |
