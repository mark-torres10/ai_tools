---
name: create-implementation-plan
description: Creates implementation plans following PLANNING_RULES. Use when the user asks to create a plan, write an implementation plan, or plan out work. Ensures Overview, Happy Flow, Manual Verification, asset storage, and UI screenshots from planning rules.
disable-model-invocation: false
metadata:
  owner: mark
  scope: global
  category: planning
---

# Create Implementation Plan

Create implementation plans that follow the planning rules in `agents/task_instructions/rules/PLANNING_RULES.md`. Works alongside Cursor Plan Mode (or similar)—apply these rules to structure and enrich whatever plan mode produces.

## When to Use

- User asks to create a plan, write an implementation plan, or plan out work.
- User enters plan mode and wants planning rules applied.
- User asks for a structured breakdown with verification.

## Path Discovery

Planning rules live inside an `ai_tools` tree. Resolve the **ai_tools root** first.

**Resolve ai_tools root in this order:**

1. **Submodule in workspace**  
   Check for an `ai_tools` directory in the workspace root (e.g. `./ai_tools/`). If it exists and contains `agents/task_instructions/rules/PLANNING_RULES.md`, use it.
2. **Fallback canonical path**  
   If there is no such submodule, use: `/Users/mark/Documents/projects/ai_tools/`.

**Planning rules file:** `<ai_tools_root>/agents/task_instructions/rules/PLANNING_RULES.md`

If found, read `PLANNING_RULES.md` and apply it. If not found, apply the structure below (inline fallback).

## Required Plan Structure

In addition to the plan steps, include:

1. **Overview** – Brief 1-paragraph description of what we're building and why.
2. **Happy Flow** – How data/logic flows end-to-end in this unit of work. Enumerated plain English with file references.
3. **Manual Verification** – Checklist with step-by-step instructions:
   - Test commands (e.g. `uv run pytest ...`)
   - Server startup and checks
   - For UI: clicks, screens, components to review
4. **Alternative approaches** – Short note on options considered and why the chosen approach was selected.
5. **Specificity** – Exact commands, file paths, and component names. No vague steps like "Add auth" or "Fix the bug".

## Plan Asset Storage

Save all assets related to this workflow in:

```
docs/plans/<YYYY-MM-DD>_<descriptor of change>_<6-digit hash>/
```

Example: `docs/plans/2026-01-30_change_selector_panels_123456/`

## UI screenshots: agent responsibility (mandatory)

This must be run for ANY UI-related change (i.e., anything in `ui/`)

**The agent MUST capture before/after screenshots itself.** Do NOT:

- Write a README or instructions for the user to take screenshots.
- Add a to-do for "someone" to capture screenshots later.
- Delegate screenshot capture to the user.

**The agent MUST:** Use the browser (e.g. Cursor's browser tools or MCP) to:

1. Capture the current UI state **before** implementation and save to `.../images/before/`.
2. Capture the new UI state **after** implementation and save to `.../images/after/`.

If the plan involves UI changes, the plan is **not complete** until these screenshots exist in the plan asset folder. No exceptions.

## UI-Related Changes (screenshots)

For UI-related work, **the agent must capture before/after screenshots itself** using the browser. Do not write instructions or a README for the user to do this.

1. **Before implementation** – Use the browser to capture the current UI state (happy path). Save screenshots to:
   - `docs/plans/<YYYY-MM-DD>_<descriptor>_<hash>/images/before/`
2. **After implementation** – Use the browser to capture the new UI state (happy path). Save screenshots to:
   - `docs/plans/<YYYY-MM-DD>_<descriptor>_<hash>/images/after/`

**To-do ordering (MUST):** For UI changes, the first to-do is the agent taking before screenshots; the last to-do is the agent taking after screenshots. The agent performs these steps; it does not document them for the user.

## Remember (include at top of every plan)

```markdown
## Remember
- Exact file paths always
- Exact commands with expected output
- DRY, YAGNI, TDD, frequent commits
```

## Anti-Patterns to Avoid

- Vague task descriptions
- Missing file paths
- Incomplete code snippets
- Implementation before tests
- No verification steps
- Assuming context
- Writing a README or instructions for the user to take before/after UI screenshots (the agent must take them)

## Workflow

1. Resolve ai_tools root and read `PLANNING_RULES.md` if available.
2. Create or refine the plan using the required structure.
3. Ensure the Remember block is at the top.
4. Use the plan asset path: `docs/plans/<YYYY-MM-DD>_<descriptor>_<6-digit hash>/`.
5. For UI work: the agent captures before screenshots (first to-do) and after screenshots (last to-do) using the browser. Save to `.../images/before/` and `.../images/after/`. Do not substitute with written instructions for the user.
6. Verify no anti-patterns are present.

## Definition of done (UI work)

For plans that include UI changes, the plan is only complete when:
- [ ] Before screenshots exist in `.../images/before/` (captured by the agent).
- [ ] After screenshots exist in `.../images/after/` (captured by the agent).
- [ ] No README or instructions were added that ask the user to take screenshots.

If you have not yet captured these screenshots, do so now before considering the plan complete.

## Constraints

- Do not skip the Manual Verification section—it is required.
- For UI changes: first to-do = before screenshots, last to-do = after screenshots. Mandatory.
- Every task should have clear, verifiable outcomes.
- Prefer specificity over brevity for critical steps.
