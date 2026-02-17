---
name: review-rules
description: Reviews current work against task-instruction rules in agents/task_instructions/rules. Use when the user asks for rules-based compliance checks or policy-aligned review feedback.
disable-model-invocation: true
metadata:
  owner: mark
  scope: global
  category: review
---

# Review Rules

Run a structured compliance review against `agents/task_instructions/rules/`.

## When to Use

- User asks for a review based on project rules or standards.
- User wants a checklist-driven pass/fail/warn assessment.
- User asks whether current work follows rule files in the rules directory.

## Inputs

- Current workspace context (open files, changed files, task intent).
- Optional user-selected subset of rules.

## Path Discovery

Rules live inside an `ai_tools` tree. Resolve the **ai_tools root** first, then use `agents/task_instructions/rules/` under it.

**Resolve ai_tools root in this order:**

1. **Submodule in workspace**  
   Check for an `ai_tools` directory in the workspace root (e.g. `./ai_tools/`). If it exists and contains `agents/task_instructions/rules/`, use it. Paths are always relative to this ai_tools root (e.g. `./ai_tools/agents/task_instructions/rules/` from workspace).
2. **Fallback canonical path**  
   If there is no such submodule, use: `/Users/mark/Documents/projects/ai_tools/`.

**Rules directory:** `<ai_tools_root>/agents/task_instructions/rules/`

If neither location yields a valid `agents/task_instructions/rules/` directory, ask the user for the rules directory and stop.

## Rule Selection

1. If `router.md` exists, use it first to choose applicable rules.
2. If user specifies rule files, honor that filter.
3. If no router exists, infer from file names and frontmatter fields:
   - `when_to_use`
   - `scope`
   - `applies_to.task_types`
4. Prefer task-relevant rules over loading everything.

## Review Workflow

1. Identify task type from user request and changed files.
2. Read selected rule files fully.
3. Evaluate current work against each selected rule.
4. Record compliance as:
   - `pass`: clearly satisfied
   - `warn`: partially satisfied or unclear
   - `fail`: clearly violated
5. For each `warn`/`fail`, provide a concrete remediation step.

## Output Format

Return:

1. **Rule Set Used**
   - Rule file paths
   - Why selected
2. **Compliance Matrix**
   - Rule -> status (`pass`/`warn`/`fail`) -> rationale
3. **Top Violations (by impact)**
   - Violation
   - Risk
   - Exact fix recommendation
4. **Verification Plan**
   - Tests/checks/commands to validate remediations

If all selected rules pass, state that explicitly and still list residual risk or missing verification.

## Constraints

- Do not claim compliance without evidence from current work context.
- Do not force unrelated rules when router/task intent indicates a narrower set.
- Keep remediation actionable and minimally invasive.
