---
name: refactor-service
description: Diagnoses a microservice or pipeline service and produces a refactoring plan focused on modularity, test coverage, lint/type health, runbooks, and service READMEs. Use when the user asks to refactor a service, pipeline, microservice, worker, batch job, or study service and wants a plan before implementation. Slash-only.
disable-model-invocation: true
metadata:
  owner: mark
  scope: project
  category: planning
---

# Refactor Service

Diagnose an existing microservice-level or pipeline-level code area, then produce a refactoring plan. This skill is planning-only: do not implement the refactor unless the user explicitly asks in a later step.

## When to Use

- User asks to refactor a service, pipeline, worker, batch job, ingestion job, model evaluation job, ETL step, API service, or study service.
- User wants a diagnosis before deciding what to change.
- User wants a plan that improves modularity, tests, lint/type health, and docs without changing intended behavior.
- User asks for service runbooks or service READMEs as part of a refactor.

## Do Not Use

- Do not use for broad architecture brainstorming without a concrete service or pipeline target.
- Do not use for implementation after a plan has already been approved; use the implementation workflow the user requests.
- Do not use as a generic code review when the user only wants bug findings.
- Do not use when the user asks to rewrite behavior from scratch.

## Relationship to `create-implementation-plan`

Use `create-implementation-plan` for the final plan scaffold, asset location rules, manual verification structure, and parallel task packet rules. Do not duplicate those instructions here.

This skill contributes the service-refactor-specific diagnosis and planning content that should be inserted into that plan:

- current-state diagnosis
- service boundaries and dataflow
- behavior-preserving invariants
- key files to touch and avoid
- modularization opportunities
- test coverage plan
- lint/type/CI plan
- runbook and README plan
- discovered bugs and improvement opportunities
- edge cases and rollback risks

## Hard Boundary

Do not change service code, tests, docs, configs, CI, or generated files while using this skill. Read files, inspect structure, and run safe diagnostic commands only. The output is a diagnosis plus a plan.

If diagnostic commands would mutate state, require credentials, process production data, or hit external services, do not run them. Note the skipped command and explain what evidence is missing.

## Inputs to Gather

- Service name and path.
- Entry points: CLIs, API routes, workers, schedulers, notebooks, pipeline DAGs, or scripts.
- Runtime commands and environment requirements.
- Existing tests and coverage configuration.
- Existing lint/type commands, such as `ruff` and `pyright` (for Python code).
- Existing docs, README, runbooks, architecture notes, or protocol references.
- Data contracts: inputs, outputs, schemas, files, queues, database tables, APIs, model artifacts, or reports.
- Operational contracts: retries, idempotency, logging, metrics, alerts, backfills, and failure handling.

Ask at most 1-3 clarifying questions if service scope, success criteria, or forbidden behavior changes are unclear. Otherwise inspect the repository and proceed.

## Diagnosis Workflow

1. Identify the service boundary.
   - Name the exact directories, modules, entry points, tests, docs, configs, and CI jobs that belong to the service.
   - Separate service-owned code from shared libraries and unrelated callers.
2. Trace the happy flow.
   - Describe how data enters the service, how it is transformed, what side effects occur, and what outputs are produced.
   - Include exact file and symbol references where possible.
3. Record current invariants.
   - Capture behavior that must not change: data schemas, output formats, ordering guarantees, idempotency, retry behavior, error semantics, timestamps, naming conventions, and study-specific assumptions.
4. Assess modularity.
   - Look for mixed responsibilities, oversized functions, hidden global state, ad hoc parsing, duplicated logic, tangled IO and business logic, unclear boundaries, and hard-to-test side effects.
5. Assess tests.
   - Inventory unit, integration, fixture, golden-file, contract, and end-to-end coverage.
   - Identify missing tests for happy path, edge cases, failures, idempotency, and study-critical outputs.
6. Assess lint/type health.
   - Identify the exact `ruff` and `pyright` commands the repo expects.
   - If safe, run them in diagnostic mode. Do not fix failures.
7. Assess docs.
   - Check whether the service has a README at the service root or equivalent local docs.
   - Check whether a runbook exists under `docs/runbooks/services/` unless the user specifies another location.
8. Identify risks.
   - Name likely breakpoints, migration hazards, test brittleness, unclear ownership, and dependencies that make refactoring risky.
9. Note bugs and improvement opportunities discovered along the way.
   - For each item, explicitly classify it as either required for full test coverage/CI success or optional follow-up work.
   - Do not fold optional improvements into the core refactor unless the user approves the expanded scope.

## Refactoring Plan Requirements

The plan should preserve existing behavior unless there is an explicit bug called out by the user or strongly evidenced by tests/docs.

Include these service-specific sections:

1. **Diagnosis**
   - Current service purpose.
   - Current file/module ownership.
   - Current happy flow.
   - Current tests, docs, lint/type status.
   - Main maintainability risks.
2. **Behavior-Preserving Invariants**
   - Bullet list of contracts that must remain unchanged.
   - Name the test or verification step that will protect each invariant.
3. **Refactor Boundaries**
   - Files/directories to inspect.
   - Files/directories allowed to change.
   - Files/directories not to touch unless explicitly approved.
   - Shared interfaces, schemas, configs, or public APIs to freeze before implementation.
4. **Modularization Plan**
   - Proposed module boundaries.
   - Responsibilities moving into helpers/classes/functions.
   - Responsibilities that should stay in place.
   - Any abstractions to avoid because they are speculative.
5. **Test Coverage Plan**
   - Exact test files to add or update.
   - Fixtures or mocks needed.
   - Happy path, edge cases, failure modes, and regression tests.
   - Coverage expectation based on existing project thresholds or, if none exist, sufficient behavior coverage for service-critical paths.
6. **Lint, Type, and CI Plan**
   - Exact commands for `ruff`, `pyright`, tests, and relevant CI checks.
   - Expected passing result.
   - Known pre-existing failures, if any, separated from failures the refactor must fix.
7. **Docs Plan**
   - README path for each service.
   - Runbook path under `docs/runbooks/services/` unless the user specified otherwise.
   - Required README contents: purpose, entry points, local run commands, required env vars, inputs, outputs, tests, and ownership notes.
   - Required runbook contents: service purpose in the study, operating model, how to run, dependencies, failure modes, recovery steps, observability, and escalation notes.
8. **Discovered Bugs and Improvements**
   - Bugs or defects observed during diagnosis.
   - Improvement opportunities that are not required for the behavior-preserving refactor.
   - For each item, state `required for full coverage/CI` or `optional follow-up`.
   - If required, identify the test, lint, type, or CI check that makes it blocking.
9. **Edge Cases and Rollback**
   - Inputs, failures, empty data, partial outputs, repeated runs, stale artifacts, interrupted jobs, external dependency failures, and rollback strategy.

## Quality Bar

- Plan before implementation.
- Prefer small, behavior-preserving refactors over rewrites.
- Improve modularity only where it makes testing, ownership, or readability materially better.
- Keep service interfaces stable unless the user explicitly approves a contract change.
- Tests should characterize existing behavior before internals move.
- Docs should explain how the service works, how to run it, and why it matters to the study.
- Bugs and improvements found during diagnosis should be captured, but only blocking bugs should enter the core plan without explicit approval.
- The plan is not complete unless it accounts for service README, runbook, test coverage, `ruff`, `pyright`, and CI.

## Output Format

Return a concise diagnosis first, then a refactoring plan using `create-implementation-plan` formatting.

Start with:

```markdown
## Diagnosis

**Service:** `<name/path>`
**Current purpose:** ...
**Current flow:** ...
**Evidence reviewed:** ...
**Main risks:** ...

## Refactoring Plan

<basic outline of refactoring plan>
```

If evidence is incomplete, state exactly what was not inspected and why. Do not invent file paths, commands, test coverage, or CI status.

## Response Rules

- Be specific about files, commands, entry points, and contracts.
- Distinguish evidence from assumptions.
- Do not propose behavior changes unless clearly labeled as bug fixes requiring approval.
- When noting bugs or improvements, explicitly say whether each item is required to pass full test coverage/CI or is optional follow-up for later work.
- Do not recommend new frameworks, orchestration systems, or abstractions unless the existing service already justifies them.
- Keep the plan high-level enough to avoid implementation, but concrete enough that a later coding agent can execute it.
- Prefer direct module extraction, pure functions around business logic, explicit IO boundaries, and tests around public behavior.
