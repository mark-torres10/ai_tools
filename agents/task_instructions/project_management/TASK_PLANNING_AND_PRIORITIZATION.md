# Task Planning and Prioritization

This document outlines the rules for planning and prioritizing tasks to ensure the coding agent delivers high-value features efficiently and autonomously. These guidelines enable the agent to break down complex tasks, estimate effort accurately, align work with user and stakeholder goals, and scale to enterprise-level projects, reflecting the standards of a staff or principal engineer. Integration with Linear and GitHub ensures tasks and projects are managed with Linear as the source of truth, synchronized with local Markdown files organized in a `/projects/<projectId_prefix>_<project_name>/` folder structure, and each Linear ticket corresponds to a GitHub pull request (PR) for review and completion. The agent uses language-specific primitives and best practices (e.g., Python for Python projects, JavaScript for JavaScript projects) as specified by the user and per `CODING_RULES.md`.

## Task Planning

Task planning involves decomposing user requests into actionable subtasks, estimating effort, identifying dependencies, and validating feasibility to ensure systematic progress.

- Decompose user requests into granular subtasks, each with a single responsibility, to facilitate focused implementation and testing. For example, a request to build a login feature should be broken into subtasks like designing the UI, implementing authentication logic, and writing tests.
- Define clear deliverables for each subtask, specifying expected inputs, outputs, and success criteria. For instance, the authentication logic subtask should deliver a function that validates credentials against a database, returning a session token on success.
- Identify dependencies between subtasks and across features or projects to determine the execution order. For example, the UI subtask depends on the authentication logic, and a feature may depend on a DevOps pipeline setup.
- Estimate effort for each subtask in hours, using historical data or industry benchmarks: API endpoint (2-4 hours), database migration (4-8 hours), complex UI component (8-12 hours). Document assumptions, such as familiarity with the tech stack, in a `plan_<feature>.md` file stored in `/projects/<projectId_prefix>_<project_name>/`.
- Create a task plan in `/projects/<projectId_prefix>_<project_name>/plan_<feature>.md`, summarizing subtasks, deliverables, dependencies, and effort estimates in a Markdown table (e.g., `| Subtask | Deliverable | Dependencies | Effort (hrs) | Priority Score | Linear Issue ID | Linear Issue Identifier | PR URL |`). Commit to version control using `gh` per `GITHUB_OPERATIONS.md` with a message like `[plan] Define task plan for <feature> in /projects/<projectId_prefix>_<project_name>/`.
- Validate the task plan against user requirements by cross-referencing deliverables with the original request. If discrepancies arise, infer intent from historical tasks in `/projects/<projectId_prefix>_<project_name>/lessons_learned.md` and propose a minimal viable solution, seeking user confirmation within 24 hours.
- Simulate the task plan before execution by mapping dependencies and effort to a Gantt chart, identifying infeasible timelines or missing steps. Write a language-specific script (e.g., Python for Python projects, JavaScript for JavaScript projects) to check `plan_<feature>.md` for missing dependencies or effort estimates, failing if any subtask lacks a deliverable, following the user-specified language’s best practices (e.g., Python’s `argparse` for CLI tools, JavaScript’s `commander` for Node.js).
- Reassess the task plan daily or if new requirements increase effort by >20% or introduce new dependencies, updating `plan_<feature>.md` and creating or updating a PR per `GITHUB_OPERATIONS.md`.
- Use language-specific primitives and best practices for the project’s programming language, as specified by the user. For Python projects, follow PEP 8, use type hints, and structure code with modules per `CODING_RULES.md`. For JavaScript projects, use ES6+ syntax, ESLint for linting, and modular imports/exports. Do not implement in a language other than the user-specified one (e.g., no Python for a JavaScript project).

## Multi-Feature and Roadmap Planning

To scale planning across projects and align with long-term goals, the agent maintains a roadmap and coordinates cross-feature tasks.

- Create a `roadmap.md` file in the project root for features spanning multiple sprints, outlining high-level goals, milestones, and cross-feature dependencies. Map each feature to an OKR (Objective and Key Result) to ensure alignment with measurable outcomes.
- Validate roadmap priorities with stakeholders (e.g., product managers, developers) via a summary email, incorporating feedback within 24 hours. Document stakeholder input in `roadmap.md` and commit using `gh` per `GITHUB_OPERATIONS.md`. Log validation in `/projects/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md`.
- Limit active subtasks to 5-7 per day, based on estimated effort, to avoid overloading processing capacity. If capacity is exceeded, defer low-priority tasks and update `plan_<feature>.md` in `/projects/<projectId_prefix>_<project_name>/`.
- Maintain a `dependencies.md` file in the project root listing all cross-project dependencies (e.g., shared libraries, external team deliverables), updated weekly to reflect resolved or new blockers. Commit changes using `gh` per `GITHUB_OPERATIONS.md`.

## Prioritization

Prioritization ensures the agent focuses on high-impact tasks, balancing user needs, technical constraints, and project goals.

- Prioritize subtasks based on user impact, defined as the value delivered to the user (e.g., core functionality over polish). For example, prioritize login authentication over password strength indicators.
- Consider technical dependencies, ensuring foundational subtasks (e.g., database schema setup) are completed before dependent ones (e.g., API endpoints).
- Account for risk and complexity, prioritizing high-risk or complex subtasks early to surface issues sooner. For instance, tackle a novel algorithm before UI refinements.
- Use a scoring system to rank subtasks, assigning 1-5 points for user impact, risk, and urgency, then summing the scores. Execute subtasks with higher scores first, breaking ties by favoring lower effort unless a critical dependency exists.
- Document prioritization decisions in `/projects/<projectId_prefix>_<project_name>/plan_<feature>.md`, including the scoring rationale and trade-offs (e.g., delaying a feature to unblock another). Use a table format: `| Subtask | Impact | Risk | Urgency | Total Score | Linear Issue ID | Linear Issue Identifier | PR URL |`.
- Re-evaluate priorities after completing each subtask or receiving new user input, updating `plan_<feature>.md` and creating or updating a PR per `GITHUB_OPERATIONS.md`. If a high-priority task emerges, pause low-priority subtasks and notify the user.
- Resolve prioritization conflicts using a decision tree: (1) Compare total scores; (2) If equal, prioritize lower effort; (3) If still tied, favor tasks unblocking critical dependencies. For unresolved conflicts, escalate to the user with a table listing subtasks, scores, pros/cons, and a recommended choice. If no response within 48 hours, proceed with the recommended option, logging the decision in `/projects/<projectId_prefix>_<project_name>/logs.md`.
- Validate prioritization outcomes post-feature by measuring user impact (e.g., feature usage metrics) and comparing to scores. Log discrepancies in `/projects/<projectId_prefix>_<project_name>/lessons_learned.md`.

## Dependency Management

Managing dependencies ensures smooth task execution by addressing blockers and external requirements.

- Map all dependencies in `/projects/<projectId_prefix>_<project_name>/plan_<feature>.md` and `/projects/<projectId_prefix>_<project_name>/dependencies.md`, including internal (e.g., other subtasks) and external (e.g., third-party APIs, DevOps deliverables). For example, note that an API subtask requires a service key.
- Mitigate external dependency risks by identifying alternatives or fallbacks. For instance, if a third-party API is unavailable, mock it with a stub returning sample data, documented in `/projects/<projectId_prefix>_<project_name>/mocks.md`.
- Research alternative solutions for missing dependencies (e.g., open-source libraries) and propose them in `plan_<feature>.md` before escalating. For example, replace a delayed API with a community-maintained equivalent.
- Communicate dependency blockers to the user promptly, proposing workarounds or adjusted timelines (e.g., parallelizing UI development during a database migration delay). Use a template: `Blocker: <issue>. Impact: <delay>. Proposed Solution: <workaround>.`
- Update `plan_<feature>.md` and `dependencies.md` to reflect resolved dependencies, ensuring the execution order remains valid. Commit changes and create a PR using `gh` per `GITHUB_OPERATIONS.md` with a message like `[plan] Update dependencies for <feature> in /projects/<projectId_prefix>_<project_name>/`.
- Assign ownership for shared dependencies using a RACI matrix in `/projects/<projectId_prefix>_<project_name>/dependencies.md`, clarifying who is Responsible, Accountable, Consulted, and Informed.

## Progress Tracking and Self-Reflection

Tracking progress and reflecting on outcomes ensure alignment with goals and continuous improvement.

- Update `/projects/<projectId_prefix>_<project_name>/plan_<feature>.md` after completing each subtask, marking it as done and noting deviations from estimated effort or deliverables. For example, if a subtask took 6 hours instead of 4, document the reason (e.g., edge cases) in `/projects/<projectId_prefix>_<project_name>/lessons_learned.md`.
- Maintain a `/projects/<projectId_prefix>_<project_name>/todo.md` file as a checklist of subtasks, synchronized with `plan_<feature>.md` and Linear issues, following `AGENT_WORKFLOW.md`. Update markers (e.g., `[x]`) based on Linear issue `state` (e.g., `Completed`) after PR approval per `GITHUB_OPERATIONS.md`.
- Conduct self-reflection after major milestones (e.g., feature completion), comparing actual outcomes to planned deliverables. Log reflections in `/projects/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md` and `/projects/<projectId_prefix>_<project_name>/lessons_learned.md`, covering successes, challenges, and process improvements (e.g., “Underestimated UI complexity due to responsive design”).
- Compare actual vs. estimated effort for each subtask in `lessons_learned.md`, updating benchmarks in `plan_<feature>.md` if deviations exceed 20%. For example, increase database task estimates by 10% if consistently underestimated.
- Verify task completion by running all relevant tests (per `tdd.md`), validating against user requirements, and ensuring the corresponding PR is approved on GitHub per `GITHUB_OPERATIONS.md`. If gaps exist, create new subtasks, update `plan_<feature>.md`, and create a new PR.
- Instrument task completion times with Prometheus metrics to identify bottlenecks (e.g., subtasks taking >150% of estimated effort). Log metrics in `/projects/<projectId_prefix>_<project_name>/metrics.md`.

## Error Handling and Recovery

Errors during planning, prioritization, or GitHub operations require swift detection and correction to maintain progress.

- Detect planning errors (e.g., missed dependencies) by reviewing `plan_<feature>.md` before execution and after updates. Correct errors by revising the plan, notifying the user if delays exceed 1 day, and updating the PR per `GITHUB_OPERATIONS.md`. Log errors in `/projects/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md`.
- Handle prioritization errors (e.g., focusing on low-impact tasks) by re-scoring subtasks during daily reassessments. Adjust the execution order, document the rationale in `plan_<feature>.md`, and update the PR.
- Implement retry logic for transient issues (e.g., temporary API unavailability for Linear or GitHub) with up to three attempts using exponential backoff (1s, 2s, 4s). Log attempts in `/projects/<projectId_prefix>_<project_name>/logs.md`.
- Escalate persistent errors to the user with a proposed solution and timeline, using a template: `Error: <issue>. Impact: <effect>. Solution: <fix>. ETA: <time>.` If no response within 48 hours, proceed with the proposed fix, logging the decision in `logs.md` and updating the PR.
- For ambiguous requirements, infer intent from `lessons_learned.md` and propose a minimal viable solution, seeking confirmation. If unresolvable, prototype both options, A/B test with a user subset, and update the PR with results. Log the process in `/projects/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md`.

## Linear Integration

Linear serves as the primary source of truth for project and task management, with `/projects/<projectId_prefix>_<project_name>/plan_<feature>.md` and `/projects/<projectId_prefix>_<project_name>/todo.md` synchronized to reflect Linear’s state. The agent uses Linear’s GraphQL API via the MCP spec integrated with Cursor to create projects and issues, read updates, and maintain consistency for the appropriate team, using a shortened project identifier and project name for folder organization.

### Setup
- Leverage the MCP spec’s pre-configured Linear integration in Cursor to access the GraphQL API without explicit authentication. Verify access by querying the `viewer` endpoint on startup, logging any failures to `/projects/<projectId_prefix>_<project_name>/logs.md`.
- If you haven't been told the team, DO NOT ASSUME. ASK THE USER FOR CLARIFICATION. Use the Linear MCP to fetch the list of teams, and then use that team. ALWAYS ASK.
- Use the appropriate team’s `teamId` for all operations, retrieved via the `teams` query (e.g., `name: "MET"`). Cache the `teamId` in memory for the session to optimize API calls.

### Project Creation
- For each new feature, create a Linear project in the appropriate team using the `projectCreate` mutation, generating a unique `projectId` (UUID, e.g., `8f4c2b1a-4f3e-4a6b-9c2d-7e8f9a0b1c2d`).
- Create a project-specific folder `/projects/<projectId_prefix>_<project_name>/`, where `<projectId_prefix>` is the first 6 characters of the `projectId` and `<project_name>` is the Linear project name (lowercased, spaces replaced with underscores, e.g., `/projects/8f4c2b_user_profile_page/` for “User Profile Page”). Store `plan_<feature>.md`, `todo.md`, `lessons_learned.md`, `logs.md`, `metrics.md`, `mocks.md`, and `<projectId_prefix>_<issueId_prefix>_reflection.md` within it.
- Map `plan_<feature>.md` fields: `name` to the feature name (e.g., “User Profile Page”), `description` to deliverables and milestones, `startDate` to the current date, and `targetDate` to the planned completion date based on effort estimates.
- Store the full `projectId` in `plan_<feature>.md` as a table column (`Linear Project ID`) and in `/projects/<projectId_prefix>_<project_name>/metadata.md` as a key-value pair (e.g., `projectId: 8f4c2b1a-4f3e-4a6b-9c2d-7e8f9a0b1c2d`). Commit using `gh` per `GITHUB_OPERATIONS.md` with a message like `[plan] Create /projects/<projectId_prefix>_<project_name>/ for <feature> with Linear project ID`. Log creation in `/projects/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md`.

### Task Creation and Updates
- Create a Linear issue for each subtask in `plan_<feature>.md` using the `issueCreate` mutation, generating a unique issue `id` (UUID). Set:
  - `title`: Subtask name (e.g., “Design User Profile UI”).
  - `description`: Deliverable, dependencies, and priority score.
  - `estimate`: Effort in hours, rounded to the nearest integer.
  - `priority`: Map priority score (1-5) to Linear’s scale (0-4, e.g., 5→1=Urgent, 4→2=High, 3→3=Medium, 2→4=Low, 1→0=None).
  - `projectId`: Link to the feature’s Linear project.
  - `teamId`: The team’s ID from Linear.
- Store the issue `id` and human-readable `identifier` (e.g., `MET-123`) in `plan_<feature>.md` as table columns (`Linear Issue ID`, `Linear Issue Identifier`) and commit using `gh` per `GITHUB_OPERATIONS.md`. Log creation in `/projects/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md`.
- Update issues via `issueUpdate` when `plan_<feature>.md` changes (e.g., updated effort, priority, or status). For example, if a subtask’s effort increases, update the issue’s `estimate` field and update the PR.  Log updates in `/projects/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md`.
- When completing a subtask, wait for PR approval on GitHub per `GITHUB_OPERATIONS.md`, then set the Linear issue `state` to `Completed` and update `/projects/<projectId_prefix>_<project_name>/todo.md` to `[x]`. Log completion in `/projects/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md`.

### Synchronization Process

- Run a sync process every 10 minutes to align Linear, GitHub, and `/projects/<projectId_prefix>_<project_name>/` files, triggered also on task completion, plan reassessment, PR updates, or reflection events per `LLM_REFLECTION_DEBUGGING_RULES.md`.
- Query Linear’s `issues` for the project using the `projectId`, retrieving `id`, `identifier` (e.g., `MET-123`), `title`, `description`, `estimate`, `priority`, `state`, and `updatedAt`. Compare with `plan_<feature>.md` using a `last_modified` field in the Markdown file’s frontmatter (e.g., `---\nlast_modified: 2025-07-07T16:00:00Z\n---`).
- **Linear to Markdown**: If an issue’s `updatedAt` is newer, update `plan_<feature>.md` and `todo.md` to reflect changes (e.g., status, estimate). For example, if an issue moves to In Progress, update todo.md to [ ] with a note: “In Progress in Linear.” Log the sync in `/projects/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md.`
- **Markdown to Linear**: If `plan_<feature>.md`’s `last_modified` is newer, push changes to Linear via `issueUpdate` or `issueCreate` for new subtasks. For example, if a subtask’s priority score changes, update the issue’s `priority` and PR description.
- **GitHub Synchronization**: Update the PR description via `gh pr edit` to reflect Linear issue changes (e.g., updated subtasks, status). Ensure `plan_<feature>.md` includes the latest PR URL.  Log PR updates in `/projects/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md`.
- Resolve conflicts by prioritizing Linear’s state, logging discrepancies in `/projects/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md` with a timestamp and resolution (e.g., “Overwrote local effort estimate to match Linear”).
- Maintain a one-to-one correspondence between `plan_<feature>.md` subtasks, Linear issues, and GitHub PRs, creating or archiving issues and PRs as subtasks are added or removed. If an issue is deleted in Linear, archive the corresponding subtask in `/projects/<projectId_prefix>_<project_name>/archive/subtask_<issueId>.md.`

### Error Handling

- Retry API errors (e.g., rate limits, network issues) for Linear and GitHub gh commands up to three times with exponential backoff (1s, 2s, 4s). Log attempts to `/projects/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md` per `LLM_REFLECTION_DEBUGGING_RULES.md`.
For persistent errors (e.g., invalid teamId or repository access), escalate to the user with a template: `Error: <issue>. Impact: <effect>. Solution: <fix>. ETA: <time>`. If no response within 48 hours, queue changes locally in `/projects/<projectId_prefix>_<project_name>/sync_queue.json` and retry daily. Log escalations in `/projects/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md`.



Handle offline scenarios by queuing changes in sync_queue.json, syncing when connectivity is restored. Log queue status in /projects/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md.

### Testing

- Write language-specific unit tests to mock Linear (`projectCreate`, `issueCreate`, `issueUpdate`) and GitHub (`gh pr create`) operations, verifying field mappings (e.g., priority score to Linear priority, PR title format). For Python projects, use `pytest` with `unittest.mock`. For JavaScript projects, use `jest` with `jest-mock`. Ensure >90% line coverage per `CODING_RULES.md`.
- Run integration tests to create a test project in the correct Linear team, a test PR using `gh pr create`, and sync with `/projects/<projectId_prefix>_<project_name>/plan_<feature>.md`, asserting consistency (e.g., issue count, PR links). Use test-specific prefixes (e.g., “Test_<feature>” for projects, `test/<issueId_prefix>_<feature_snippet>` for branches).
- Validate sync accuracy by simulating a sync cycle (Linear↔Markdown↔GitHub) and asserting no data loss. Log test results in `/projects/<projectId_prefix>_<project_name>/tests.md`.
- Test error handling by simulating API and gh command failures (e.g., 429, network timeout), verifying retries and logging per `LLM_REFLECTION_DEBUGGING_RULES.md`.
- Verify folder structure integrity by checking that all required files (`plan_<feature>.md`, `todo.md`, etc.) exist in `/projects/<projectId_prefix>_<project_name>/` and match Linear and GitHub data.

### Scalability
- Implement Linear and GitHub operations in `linear_client.py` and `github_client.py` modules in the `bluesky-research` environment, using language-specific best practices (e.g., Python’s `requests` for HTTP, JavaScript’s `axios` for Node.js). Handle queries and mutations with reusable functions (e.g., `create_project`, `sync_issues`, `create_pr`).
- Monitor Linear (6000 points/hour) and GitHub (5000 requests/hour via `gh api rate_limit`) API rate limits, pausing operations if within 10% of the limit. Log rate limit status in `/projects/<projectId_prefix>_<project_name>/metrics.md`.
- For projects with >50 subtasks, store task plans in a SQLite database (`/projects/<projectId_prefix>_<project_name>/plans.db`), syncing with `plan_<feature>.md` for readability. Use a schema: `tasks(feature, subtask, deliverable, effort, priority, linear_issue_id, pr_url)`.
- Archive completed Linear projects in `/projects/<projectId_prefix>_<project_name>/archive/` with a copy of all files (e.g., `plan_<feature>_2025-07-07.md`) and set Linear status to `Completed`. Delete test projects and branches after integration tests.

## Risk Management

Proactive risk management mitigates potential blockers and ensures robust planning.

- Create a risk register in `/projects/<projectId_prefix>_<project_name>/plan_<feature>.md`, listing potential blockers (e.g., API downtime, PR review delays) with likelihood (1-5), impact (1-5), and mitigation plans. For example: `Risk: Linear API downtime. Likelihood: 3. Impact: 4. Mitigation: Queue changes locally and monitor status.`
- Review the risk register daily, updating mitigations and escalating high-impact risks (score >12) to the user with proposed actions, updating the PR per `GITHUB_OPERATIONS.md` if needed.
- Maintain a Kanban board in `/projects/<projectId_prefix>_<project_name>/plan_<feature>.md` with columns for To Do, In Progress, and Done, updating daily to visualize bottlenecks and prioritize risk mitigations.

## Archival and Scalability

To support enterprise-scale projects, task plans are organized, archived, and indexed for maintainability.

- Organize task plans in `/projects/<projectId_prefix>_<project_name>/` for each Linear project, with files like `plan_<feature>.md`, `todo.md`, `lessons_learned.md`, `logs.md`, `metrics.md`, and `mocks.md`. Link projects in `roadmap.md` in the project root.
- Archive completed projects in `/projects/<projectId_prefix>_<project_name>/archive/`, tagged with feature name and completion date (e.g., `plan_<feature>_2025-07-07.md`). Index `lessons_learned.md` entries with keywords (e.g., ‘database’, ‘UI’) for retrieval.
- Version task plans in git, committing changes with `gh` per `GITHUB_OPERATIONS.md` with messages like `[plan] Update <feature> plan in /projects/<projectId_prefix>_<project_name>/ for <change>`. Backup `/projects/` to a cloud storage service weekly.
- For large projects (>50 subtasks), use a SQLite database (`/projects/<projectId_prefix>_<project_name>/plans.db`) to store task plans, syncing with Markdown files for human readability.

## Integration with Other Processes

Task planning integrates with coding, testing, GitHub, and workflow rules for cohesive feature delivery.

- Align task plans with the TDD workflow in `tdd.md`, ensuring each subtask includes test cases as deliverables. For example, an API endpoint subtask must include unit and integration tests, documented in the PR per `GITHUB_OPERATIONS.md`. Use language-specific testing frameworks (e.g., `pytest` for Python, `jest` for JavaScript).
- Follow `CODING_RULES.md` for effort estimation, accounting for complexity limits (e.g., cyclomatic complexity <10) and testing requirements (e.g., >90% coverage). Adhere to language-specific best practices (e.g., Python’s PEP 8, JavaScript’s Airbnb style guide).
- If starting a new issue that hasn't had any development yet.
- Synchronize progress with `AGENT_WORKFLOW.md`, using `/projects/<projectId_prefix>_<project_name>/todo.md` for detailed tracking and `plan_<feature>.md` for high-level planning. Ensure updates reflect in Linear and GitHub PRs and `/projects/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md`.
- Incorporate `UI_RULES.md` for UI subtasks, prioritizing clarity and accessibility in deliverables, and document in PR descriptions.
- Communicate progress and escalations per `AGENT_CONVERSATION_STYLE.md`, using prose for updates and natural language lists (e.g., “current blockers include: x, y, z”) for summaries, included in PR comments or descriptions.
- Perform reflection and debugging per `LLM_REFLECTION_DEBUGGING_RULES.md` at key stages (e.g., error detection, subtask completion, PR creation), logging in `/projects/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md`

## Implementation Notes

- Use Markdown tables in `/projects/<projectId_prefix>_<project_name>/plan_<feature>.md` for subtasks, dependencies, priorities, Linear IDs, and PR URLs. Example: `| Subtask | Deliverable | Dependencies | Effort (hrs) | Priority Score | Linear Issue ID | Linear Issue Identifier | PR URL |`.
- Test task plans, Linear, and GitHub integration with a language-specific script, integrated into CI pipelines per `CODING_RULES.md`. For Python projects, use `pytest` and `unittest.mock`. For JavaScript projects, use `jest` and `esbuild` for bundling.
- Optimize planning for performance by limiting subtasks to 10-20 per feature, merging or splitting to balance granularity and manageability.
- Ensure compatibility with Streamlit or other frameworks by including framework-specific considerations in effort estimates (e.g., Streamlit’s rendering constraints for Python, React’s component lifecycle for JavaScript).
- Instrument planning efficiency with Prometheus metrics (e.g., plan reassessment frequency, sync latency, PR creation time) and set alerts for error rates >1% over a 5-minute window, logged in `/projects/<projectId_prefix>_<project_name>/metrics.md`.

## Planning Folder Nomenclature Rule

- All new planning folders must use the first 6 digits of the Linear project ID as prefix, followed by the project name, for all new backend/frontend projects. Example: `b94f21_bluesky_post_explorer_backend` for project ID `b94f21bf-f11b-4210-a8ef-67904301a8fa` and project name `Bluesky Post Explorer Backend`. This ensures consistent cross-project planning nomenclature and traceability.