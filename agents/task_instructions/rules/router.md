---
id: rules.router
title: Rules Router
description: Router for selecting and composing task-instruction rules based on user intent, task type, and file context.
when_to_use:
  - Choosing which rule files to load for a task.
  - Composing multiple rules for implementation, testing, or operations.
  - Resolving overlap or conflicts between candidate rules.
when_not_to_use:
  - Replacing the detailed content of individual rule files.
scope:
  - routing
  - context_selection
priority: 100
applies_to:
  task_types:
    - routing
    - context_engineering
  file_globs:
    - "agents/task_instructions/rules/*.md"
dependencies: []
conflicts_with: []
tools_preferred:
  - ReadFile
owner: ai_tools
last_updated: 2026-02-17
---

# Task Instruction Rules Router

This folder contains specialized task-instruction rule files used to guide agent behavior for coding, testing, repository conventions, server operations, and ticket quality.

Use this router to select the right rules for a task and combine them in a deterministic order.

## Rule Directory

### `RUN_SERVERS.md`
- **Rule ID**: `rules.run_servers`
- **Summary**: Start, validate, monitor, and troubleshoot local servers safely.
- **Use for**: server startup, runtime debugging, process and port checks.
- **Common triggers**:
  - "start the frontend/backend"
  - "port already in use"
  - "server crashes on launch"

### `CODING_RULES.md`
- **Rule ID**: `rules.coding_rules`
- **Summary**: Baseline engineering standards for architecture, reliability, performance, and debugging behavior.
- **Use for**: implementation, refactoring, bug fixes, code reviews.
- **Common triggers**:
  - "implement/fix/refactor this code"
  - "review code quality"
  - "improve performance/reliability"

### `CLEAN_CODE_PRINCIPLES.md`
- **Rule ID**: `rules.clean_code_principles`
- **Summary**: Readability and maintainability principles (naming, functions, structure, comments).
- **Use for**: readability-focused refactors and clean-code reviews.
- **Common triggers**:
  - "clean this up"
  - "make this easier to maintain"
  - "improve naming and structure"

### `CODING_REPO_CONVENTIONS.md`
- **Rule ID**: `rules.coding_repo_conventions`
- **Summary**: Repository-level conventions for formatting, lint/build checks, and package-management policy.
- **Use for**: commit preparation, tooling standards, and pre-commit expectations.
- **Common triggers**:
  - "prepare this for commit"
  - "set up pre-commit checks"
  - "which package manager should we use"

### `UNIT_TESTING_STANDARDS.md`
- **Rule ID**: `rules.unit_testing_standards`
- **Summary**: Testing standards covering structure, coverage, naming, mocking, and pytest execution.
- **Use for**: writing/updating tests and validating bug fixes with tests.
- **Common triggers**:
  - "add tests"
  - "fix failing tests"
  - "what testing standard should we follow"

### `UI_RULES.md`
- **Rule ID**: `rules.ui_rules`
- **Summary**: Guidance for writing high-quality project-management and engineering tickets.
- **Use for**: ticket generation and ticket-quality evaluation.
- **Common triggers**:
  - "write a project ticket"
  - "improve this ticket description"
  - "define acceptance criteria"

## Routing Decision Tree

1. **Is the user asking to run or debug services?**
   - Yes -> load `RUN_SERVERS.md` first.

2. **Is the primary task code implementation/refactor/review?**
   - Yes -> load `CODING_RULES.md`.
   - If readability/maintainability is emphasized -> also load `CLEAN_CODE_PRINCIPLES.md`.

3. **Is the task test-focused?**
   - Yes -> load `UNIT_TESTING_STANDARDS.md`.
   - If code changes are included -> also load `CODING_RULES.md`.

4. **Is the task commit/tooling/conventions focused?**
   - Yes -> load `CODING_REPO_CONVENTIONS.md`.

5. **Is the task ticket/planning artifact generation?**
   - Yes -> load `UI_RULES.md`.

6. **If multiple categories apply**
   - Compose all relevant rules using precedence in the next section.

## Rule Composition and Precedence

When multiple rules match, apply in this order:

1. `rules.router` (this file, for selection logic)
2. `rules.run_servers` (operational safety-critical)
3. `rules.unit_testing_standards` (quality gate)
4. `rules.coding_rules` (baseline implementation behavior)
5. `rules.coding_repo_conventions` (repo/tooling conventions)
6. `rules.clean_code_principles` (style and maintainability refinements)
7. `rules.ui_rules` (ticket/planning quality)

If guidance appears conflicting:
- Prefer the more task-specific rule over generalized guidance.
- Prefer explicit safety/verification steps over optional style guidance.
- Prefer repository policy when selecting tools or commands.

## Common Task Patterns

| Task Pattern | Recommended Rule Set |
| --- | --- |
| Start backend and frontend, then verify health | `RUN_SERVERS.md`, `CODING_REPO_CONVENTIONS.md` |
| Implement feature and add tests | `CODING_RULES.md`, `UNIT_TESTING_STANDARDS.md`, `CODING_REPO_CONVENTIONS.md` |
| Refactor for clarity without behavior change | `CODING_RULES.md`, `CLEAN_CODE_PRINCIPLES.md` |
| Investigate bug, fix, and validate in CI-safe tests | `CODING_RULES.md`, `UNIT_TESTING_STANDARDS.md` |
| Prepare codebase for commit hooks and formatting | `CODING_REPO_CONVENTIONS.md`, `CODING_RULES.md` |
| Draft or improve a project ticket | `UI_RULES.md` |

## Maintenance Instructions

When adding a new rule file in this folder:

1. Add metadata frontmatter with at least:
   - `id`, `description`, `when_to_use`, `scope`, `priority`, `applies_to`.
2. Add a new entry in **Rule Directory**.
3. Update **Routing Decision Tree** if it introduces a new task type.
4. Update **Rule Composition and Precedence** if it should override existing rules.
5. Add at least one row in **Common Task Patterns**.
