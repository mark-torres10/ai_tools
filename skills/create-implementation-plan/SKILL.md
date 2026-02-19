---
name: create-implementation-plan
description: Creates implementation plans following PLANNING_RULES. Use when the user asks to create a plan, write an implementation plan, or plan out work. Ensures Overview, Happy Flow, Manual Verification, and other structure from planning rules.
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

## Workflow

1. Resolve ai_tools root and read `PLANNING_RULES.md` if available.
2. Create or refine the plan using the required structure.
3. Ensure the Remember block is at the top.
4. Verify no anti-patterns are present.

## Constraints

- Do not skip the Manual Verification section—it is required.
- Every task should have clear, verifiable outcomes.
- Prefer specificity over brevity for critical steps.
