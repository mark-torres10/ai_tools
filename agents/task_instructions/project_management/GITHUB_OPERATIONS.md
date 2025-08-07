# GitHub Operations

This document outlines the rules for the coding agent to perform GitHub operations using the GitHub CLI (`gh`) for direct interactions, leveraging the MCP spec’s pre-configured integration with Cursor for seamless authentication and connectivity. These instructions ensure that each Linear ticket corresponds to a pull request (PR), with titles including the first six digits of the Linear issue ID and a feature snippet, descriptions linking to Linear projects and issues, and tasks marked as complete only after PR review. The agent operates at a staff/principal engineer level, adhering to best practices for version control, collaboration, and traceability as per `CODING_RULES.md`.

## Setup

- Use the GitHub CLI (`gh`) to perform all direct GitHub operations (e.g., branching, committing, pushing, PR creation). Verify connectivity by running `gh repo view` on the repository (e.g., `metresearch/project-repo`) on startup, logging any failures to `/projects/<project prefix>/logs.md`.
- Leverage the MCP spec’s pre-configured GitHub integration in Cursor for authentication, ensuring seamless access to the GitHub API and CLI commands.
- Cache repository details (e.g., `owner`, `repo`) in memory for the session to optimize CLI operations, retrieved via `gh repo view --json owner,name`.

## Branch Creation

- For each Linear issue, create a feature branch named `feature/<issueId_prefix>_<feature_snippet>`, where `<issueId_prefix>` is the first six characters of the Linear issue `id` (UUID, e.g., `8f4c2b`) and `<feature_snippet>` is a lowercase, underscore-separated summary of the issue (e.g., `user_profile_ui`). For example, issue `id` `8f4c2b1a-4f3e-4a6b-9c2d-7e8f9a0b1c2d` for “Design User Profile UI” becomes `feature/8f4c2b_user_profile_ui`.
- Initialize the branch using `gh` and git: `git checkout main && git pull && gh repo sync && git checkout -b feature/<issueId_prefix>_<feature_snippet>`.
- Commit the branch creation with a message like `[init] Create branch for Linear issue <issue_identifier>` (e.g., `MET-123`), using `git commit -m` and `git push origin feature/<issueId_prefix>_<feature_snippet>`.

## Committing Changes

- Make incremental commits for each logical change (e.g., code, tests, documentation), following the Single Responsibility Principle per `CODING_RULES.md`. Keep commits under 50 lines where possible to ensure focused changes.
- Use descriptive commit messages following the format: `[<type>] <description> (Linear <issue_identifier>)`, where `<type>` is `feat`, `fix`, `test`, `docs`, or `refactor`, and `<description>` summarizes the change. For example, `[feat] Implement user profile UI (Linear MET-123)`.
- Include the Linear issue URL (e.g., `https://linear.app/metresearch/issue/<issue_identifier>`) in the commit message footer for traceability, e.g., `See: https://linear.app/metresearch/issue/MET-123`.
- Push commits to the remote branch using `gh repo sync && git push origin feature/<issueId_prefix>_<feature_snippet>`.
- Validate commits locally with `git log --oneline` to ensure clarity and correctness before pushing. Log any push failures to `/projects/<project prefix>/logs.md`.

## Creating Pull Requests

- Create a PR for each Linear issue using `gh pr create`, targeting the main branch (e.g., `main`).
- Set the PR title to `(<Linear ticket reference>) <feature_snippet>`, where `<Linear ticket reference>` is the Linear identifier (e.g., MET) and ticket number (e.g., 26). For example, for the ticket MET-26, the PR for it would be titled `(MET-26) <Feature snippet>`  and `<feature_snippet>` is a concise summary of the feature (e.g., `(MET-26) User Profile UI Design`).
- Populate the PR description with:
  - A summary of the changes, referencing the Linear issue (e.g., “Implements UI design for user profile page as per Linear MET-123”).
  - Links to the Linear issue (e.g., `https://linear.app/metresearch/issue/<issue_identifier>`) and project (e.g., `https://linear.app/metresearch/project/<project_identifier>`).
  - A checklist of completed subtasks.
  - A reference to tests written per `tdd.md` (e.g., “Unit tests cover 90% of UI components”).
  - Example:
    ```
    Implements UI design for user profile page as per Linear MET-123.

    **Linear Links**:
    - Issue: https://linear.app/metresearch/issue/MET-123
    - Project: https://linear.app/metresearch/project/MET-456

    **Changes**:
    - Designed responsive UI with Streamlit components
    - Added unit tests for UI interactions

    **Subtasks Completed**:
    - [x] Create UI layout
    - [x] Implement form validation
    - [x] Write unit tests

    **Tests**:
    - Unit tests cover 90% of UI components (see tests/ui_test.py)
    ```
- Use `gh pr create --title "(<Linear ticket reference>) <feature_snippet>" --body "<description>" --base main --assignee @<user> --label feature,needs-review` to create the PR, assigning it to the user for review and adding labels.
- If the label "feature" doesn't exist, create it first and then proceed with PR creation.
- Store the PR URL (e.g., `https://github.com/metresearch/project-repo/pull/123`) in `/projects/<project prefix>/plan_<feature>.md` as a table column (`PR URL`) and commit with a message like `[pr] Create PR for Linear issue <issue_identifier>`.

## Task Completion

- A Linear issue is considered complete only after the PR is reviewed and approved by the user on GitHub.
- Monitor the PR status using `gh pr view <pr_number> --json state,reviewDecision,mergedAt`, checking for `state: OPEN`, `reviewDecision: APPROVED`, or `mergedAt` timestamp.
- If the PR is approved, update the Linear issue `state` to `Completed` via `issueUpdate` and mark the corresponding subtask in `/projects/<project prefix>/todo.md` as `[x]`. Log the completion in `/projects/<project prefix>/logs.md`.
- If the PR requires changes, address review comments by pushing additional commits to the feature branch using `git commit -m "[fix] Address review comments (Linear <issue_identifier>)" && gh repo sync && git push`, updating the PR description if needed, and notifying the user for re-review with `gh pr comment <pr_number> --body "Updated based on feedback, please re-review"`.
- Once merged, archive the feature branch using `gh pr merge <pr_number> --delete-branch`, which deletes the remote branch, and locally with `git branch -d feature/<issueId_prefix>_<feature_snippet>`.

## Error Handling

- Retry `gh` command failures (e.g., rate limits, network issues) up to three times with exponential backoff (1s, 2s, 4s). Log attempts to `/projects/<project prefix>/logs.md` with context (e.g., “Retry failed: 429 Rate Limit on gh pr create”).
- For persistent errors (e.g., repository access issues), escalate to the user with a template: `Error: <issue>. Impact: <effect>. Solution: <fix, e.g., verify repository access>. ETA: <time>.` If no response within 48 hours, queue changes locally in `/projects/<project prefix>/sync_queue.json` and retry daily.
- Handle merge conflicts by running `git pull origin main`, resolving conflicts locally, and pushing updated commits with `gh repo sync && git push`. Log conflicts and resolutions in `logs.md`.

## Implementation Notes

- Use the `gh` CLI for all GitHub operations integrated with CI pipelines per `CODING_RULES.md`.
- Ensure PR descriptions follow `AGENT_CONVERSATION_STYLE.md`, using prose for summaries and natural language lists for subtasks (e.g., “Completed tasks include: UI layout, form validation”).
- Instrument GitHub operations with Prometheus metrics (e.g., PR creation latency, commit frequency) and set alerts for error rates >1% over a 5-minute window, logged in `/projects/<project prefix>/metrics.md`.
