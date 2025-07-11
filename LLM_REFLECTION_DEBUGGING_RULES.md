# LLM-Specific Reflection & Debugging Rules

This document defines how the agent, as a Large Language Model-based system, should reflect, debug, and recover from issues to ensure reliability, maintainability, and alignment with staff/principal engineer practices. Reflections and debugging logs are stored in Markdown format in the project-specific directory `/planning/<projectId_prefix>_<project_name>/`, with filenames prepended by the first 6 digits of the Linear project ID and issue ID (e.g., `8f4c2b_9a0b1c_reflection.md` for project ID `8f4c2b1a-...` and issue ID `9a0b1c2d-...`). These rules integrate with `TASK_PLANNING_AND_PRIORITIZATION.md` and `GITHUB_OPERATIONS.md` to support autonomous feature execution.

## Error Detection & Categorization

When encountering an error, the agent must:

- Evaluate the failure mode using the following taxonomy:
  - **Planning Error**: Incorrect sequence or logic in task decomposition (e.g., missing a dependency in `plan_<feature>.md`).
  - **Specification Misunderstanding**: Misinterpreted user instructions or ambiguous intent (e.g., assuming OAuth without confirmation).
  - **Code Generation Error**: Syntax or semantic errors in generated code (e.g., invalid Python syntax in a function).
  - **Tooling Failure**: Errors due to tool misuse, file I/O, or environment setup (e.g., incorrect `gh` command syntax).
  - **Hallucination**: Made-up APIs, nonexistent files, or invalid assumptions (e.g., referencing a nonexistent `utils.get_feature_vector`).
  - **Out-of-Bounds Querying**: Accessing data or references beyond known context (e.g., querying an undefined variable).
- Log the error type, location (e.g., subtask name, file path, line number), and a human-readable reason in `/planning/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md`. Use a Markdown section titled `### Error: <timestamp>` with fields:
  - **Type**: The error category from the taxonomy.
  - **Location**: The subtask, file, or line where the error occurred.
  - **Reason**: A concise explanation of the failure.
  - Example:
    ```markdown
    ### Error: 2025-07-07T22:34:00Z
    **Type**: Code Generation Error
    **Location**: /src/api.py, line 42
    **Reason**: Syntax error in Python function due to missing colon after if statement.
    ```

## Self-Reflection Loop

Whenever a subtask is completed, a test fails, or an error occurs, the agent must:

- Perform a structured reflection in `/planning/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md` under a section titled `### Reflection: <timestamp>`. Include:
  - **What Was Attempted**: A concise description of the action (e.g., “Generated authentication API endpoint”).
  - **Outcome**: Success or failure, with details (e.g., “Test failed due to null pointer exception”).
  - **Why It Failed** (if applicable): Reference the error taxonomy (e.g., “Code Generation Error: incorrect variable scope”).
  - **How to Fix It** (if applicable): A concrete plan (e.g., “Add type checking to ensure variable is defined”).
  - **Confidence Level**: A score from 0.0 to 1.0 for the fix’s likelihood of success (e.g., 0.9 for a validated syntax correction).
  - **Next Steps**: The recovery plan or next action (e.g., “Update code, rerun tests, and create PR”).
  - Example:
    ```markdown
    ### Reflection: 2025-07-07T22:35:00Z
    **What Was Attempted**: Generated authentication API endpoint
    **Outcome**: Test failed
    **Why It Failed**: Code Generation Error - incorrect variable scope
    **How to Fix It**: Add type checking to ensure variable is defined
    **Confidence Level**: 0.9
    **Next Steps**: Update code, rerun tests, and create PR
    ```
- Commit the reflection file to GitHub using `gh` per `GITHUB_OPERATIONS.md` with a message like `[reflection] Log reflection for Linear issue <issue_identifier>`.

## Hallucination Control

Before referencing tools, APIs, or file paths, the agent must:

- Verify the reference exists in the current context (e.g., check file system for paths, API manifest for endpoints) using a language-specific validation (e.g., Python’s `os.path.exists`, JavaScript’s `fs.existsSync`).
- If unsure, issue a verification query (e.g., “Does `utils.get_feature_vector` exist in the project?”) and log the query in `/planning/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md`.
- If the reference is speculative, mark it in code with a comment, e.g.:
  ```python
  # TODO: Assuming existence of utils.get_feature_vector; confirm before use
  ```
- When hallucinations are detected, replace fabricated code with a placeholder and log in the reflection file under `### Error: <timestamp>` with Type: Hallucination. Example:
  ```markdown
  ### Error: 2025-07-07T22:36:00Z
  **Type**: Hallucination
  **Location**: /src/utils.py
  **Reason**: Referenced nonexistent function utils.get_feature_vector
  ```

## Retry Logic

If any step fails (e.g., test failure, syntax error, invalid plan):

- Retry the step after:
  - Modifying inputs (e.g., refining plan, correcting function signature).
  - Logging the retry rationale in `/planning/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md` under `### Retry: <timestamp>`.
  - Limiting to 2 retries per failure class, escalating if needed.
- Escalation Triggers: After 2 retries, stop and escalate to the user with a message: “Multiple retries failed for Linear issue <issue_identifier>. Proposed fix: <fix>. Please confirm or revise.” Log the escalation in the reflection file.
- Commit retry and escalation logs using `gh` per `GITHUB_OPERATIONS.md`.

## Evaluation Checkpoints

At each major milestone (e.g., planning complete, tests pass, PR created), the agent must:

- Log a checkpoint in `/planning/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md` under `### Checkpoint: <timestamp>` with:
  - **Summary of State**: What has been accomplished (e.g., “Completed UI design and unit tests”).
  - **Open Questions**: Remaining uncertainties (e.g., “Unclear if OAuth is required”).
  - **Assumptions**: Unverified assumptions (e.g., “Assumed 100ms API response time”).
  - Example:
    ```markdown
    ### Checkpoint: 2025-07-07T22:37:00Z
    **Summary of State**: Completed UI design and unit tests
    **Open Questions**: Unclear if OAuth is required
    **Assumptions**: Assumed 100ms API response time
    ```
- Commit the checkpoint to GitHub using `gh` per `GITHUB_OPERATIONS.md`.

## Reflection-Aware Planning

The agent must incorporate prior reflections into future planning:

- Before starting a new subtask, summarize prior errors and successful strategies from all `<projectId_prefix>_<issueId_prefix>_reflection.md` files in the project directory.
- Avoid repeating known mistakes (e.g., if a prior hallucination referenced a nonexistent API, double-check references).
- Reuse successful strategies (e.g., if type checking resolved a past error, apply it proactively).
- Log the summary in `/planning/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md` under `### Planning Summary: <timestamp>`.

## Structured Prompt Hygiene

When constructing prompts for other models or tools, the agent must:

- Avoid nested prompts beyond 2 levels deep to prevent complexity.
- Validate all referenced variables, functions, and instructions exist in the prompt context using language-specific checks (e.g., Python’s `globals()`, JavaScript’s `typeof`).
- Include a reflection hook in prompts: “Before completing this, reflect on whether the inputs are sufficient. If not, return a clarifying question.”
- Log prompt validation results in `/planning/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md`.

## Fail-Soft Design

- For non-critical errors (e.g., optional module missing), proceed with a warning and degraded behavior, logging in `/planning/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md`. Example: “Optional analysis skipped due to missing `pandas` dependency.”
- Notify the user of degraded behavior in PR comments per `GITHUB_OPERATIONS.md`.

## Controlled Creativity

- Make creative design decisions only when no clear instruction exists, logging the rationale in `/planning/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md`. Example: “Chose FastAPI over Flask for Python API due to async support.”
- Inform the user of divergences in PR descriptions, referencing `AGENT_CONVERSATION_STYLE.md`.

## Final Output Quality Check

Before submitting a PR or marking a task complete:

- Run an internal checklist in `/planning/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md`:
  - Does the output match the original intent?
  - Are all assumptions stated?
  - Are known caveats noted?
  - Is the reflection file updated?
  - Would this pass a senior engineer’s code review?
- If any answer is “No”, replan or re-execute, logging the decision and committing using `gh`.

## Implementation Notes

- Store reflection logs in `/planning/<projectId_prefix>_<project_name>/<projectId_prefix>_<issueId_prefix>_reflection.md`, using Markdown headers and fields for structure.
- Use language-specific validation tools (e.g., Python’s `os`, JavaScript’s `fs`) for hallucination checks, aligning with the project’s language per `CODING_RULES.md`.
- Test reflection and debugging logic with pytest (Python) or jest (JavaScript) in the `bluesky-research` conda environment, ensuring >90% coverage.
- Commit all reflection files to GitHub using `gh` per `GITHUB_OPERATIONS.md`, with messages like `[reflection] Update reflection for Linear issue <issue_identifier>`.
