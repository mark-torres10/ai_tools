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
6. **Serial Coordination Spine** – The minimum set of tasks that must stay sequential because they define contracts, unblock dependencies, or integrate parallel work.
7. **Interface or Contract Freeze** – Exact shared interfaces, schemas, types, endpoints, props, DB contracts, or invariants that must be fixed before parallel work starts.
8. **Parallel Task Packets** – As many safely delegable tasks as possible, each specified so precisely that a small distilled coding agent could execute it without interpretation.
9. **Integration Order** – Exact order for merging or landing completed parallel tasks.
10. **Final Verification** – The end-to-end checks that prove the fully integrated change works.

## Parallel-First Delegation (mandatory)

Plans must be optimized for maximum safely delegable parallel execution.

This is a hard requirement:

- Minimize the serial coordination path.
- Maximize the amount of work split into safe parallel tasks.
- Do not delegate any task that could plausibly be misunderstood by a small, weak, distilled coding agent.
- If a task cannot be specified unambiguously enough to survive delegation without clarifying questions, it must remain in the serial coordination spine.

Prefer decomposition by stable ownership boundaries such as:

- schema or contract work
- backend handler or service work
- frontend rendering work
- tests or fixtures
- docs or migration follow-up

Do not split work across parallel tasks if they would share ownership of the same file unless the plan explicitly keeps that file in the serial coordinator track.

## Parallel Task Packet Format (mandatory)

Each delegated task must include all of the following:

- **Task ID**
- **One-sentence objective**
- **Why this task is parallelizable**
- **Exact files to inspect**
- **Exact files allowed to change**
- **Exact files forbidden to change**
- **Preconditions**
- **Dependency tasks**
- **Required contracts and invariants**
- **Step-by-step implementation instructions**
- **Exact verification commands**
- **Expected outputs from verification**
- **Done-when checklist**
- **Coordinator review checklist**

If any one of these fields is missing, the task is not safe to delegate and must not appear under Parallel Task Packets.

## Delegation Validity Test (mandatory)

Before finalizing the plan, apply this test to every delegated task:

1. Could a weak coding agent execute this task without asking a question?
2. Could another agent execute a sibling task in parallel without file ownership conflict?
3. Could the coordinator verify this task in isolation?
4. Would two different agents likely make the same change from this description?

If the answer to any question is "no", rewrite the task or move it out of parallel execution.

## Plan Asset Storage

Save all assets related to this workflow in:

```text
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
- Maximum safely delegable parallelism
- Delegated tasks must be impossible to misread
- UI changes: agent captures before/after screenshots itself (no README or instructions for the user)
```

## Anti-Patterns to Avoid

- Vague task descriptions
- Missing file paths
- Incomplete code snippets
- Implementation before tests
- No verification steps
- Assuming context
- Delegated tasks with ambiguous scope or ownership
- Shared ownership of the same file across parallel tasks
- "As needed", "etc.", or "follow the existing pattern" without naming the exact reference file or symbol
- Verification steps that rely on unfinished parallel work
- Any delegated step that requires hidden intent or unstated judgment
- Writing a README or instructions for the user to take before/after UI screenshots (the agent must take them)

## Workflow

1. Resolve ai_tools root and read `PLANNING_RULES.md` if available.
2. Create or refine the plan using the required structure.
3. Minimize the serial coordination spine, freeze shared contracts, and split the remaining work into the maximum safely delegable set of parallel task packets.
4. For each delegated task, include every field from the Parallel Task Packet Format. Do not omit any field.
5. Apply the Delegation Validity Test to every delegated task and rewrite or reclassify any task that fails.
6. Ensure the Remember block is at the top.
7. Use the plan asset path: `docs/plans/<YYYY-MM-DD>_<descriptor>_<6-digit hash>/`.
8. For UI work: the agent captures before screenshots (first to-do) and after screenshots (last to-do) using the browser. Save to `.../images/before/` and `.../images/after/`. Do not substitute with written instructions for the user.
9. Verify no anti-patterns are present.

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
- Plans are invalid if they do not maximize safely delegable parallel work.
- Delegated tasks are invalid if they omit exact file boundaries, dependencies, contracts, verification commands, or completion criteria.
