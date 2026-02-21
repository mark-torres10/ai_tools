Review the repo for newly discovered workflows, commands, personas, skills, and conventions that are not yet documented in agents/README.md (or AGENTS.md if present).

## What to discover

- **New personas** in `agents/personas/` that aren't listed in agents/README.md
- **New task instructions** in `agents/task_instructions/` that should be in the workflow docs
- **Skills** in `skills/` that aren't documented
- **Automations** in `codex/automations/` not reflected in docs
- **Recurring commands or workflows** implied by scripts, Makefiles, or CI config

## Output

Propose updates to `agents/README.md` (or create/update root `AGENTS.md`). Changes should:

- Add new personas to the relevant domain sections
- Add new task instructions to the workflow process
- Add skills and automations to a "Tools & Automations" section if missing
- Preserve existing structure and tone
- Be minimal: only add what is missing; do not rewrite existing content

## Grounding rules

- Use ONLY concrete repo evidence (file paths, headings, content).
- Do NOT invent personas, skills, or workflows.
- Match the existing style of agents/README.md (sections, formatting, tone).

## PR setup

When opening a PR with the updates:

- **PR Title:** `[YYYY-MM-DD] Codex repo automation - Update agents docs`
- **PR Description:** Sync agents/README.md (or AGENTS.md) with newly discovered workflows, personas, and skills. From Codex automation.
