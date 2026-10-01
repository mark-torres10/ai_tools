# Issue Description

## Context

We have an LLM-as-a-judge implementation in `app/evaluation/`:

- `judge.py` — `LLMJudge.evaluate()` for single-conversation scoring
- `runner.py` — `evaluate_selection()` for batch, concurrent evaluations across multiple prompts
- `report.py` — aggregation into `EvalReport` and markdown tables
- `transcript.py` — LangChain message → `User:/Companion:` formatting
- `prompts/registry.py` — 26 registered prompts across Criteria (6), Behaviors (12), and Safety (8)

What scores are captured:
- Criteria: `level` = Excellent/Passable/NeedsWork/Unacceptable
- Behaviors: `present` = True/False
- Safety: `detected` = True/False

Proposed automations should reuse `evaluate_selection()` and `build_report()` rather than building new orchestration.

## Proposal

We create:

- In `app/chat/evaluation/`, a `evaluate_chat_agent_fixed_test_suite/` folder that contains the necessary Python scripts including dummy conversations, etc.
- In `docs/automations/`, a `chat_fixed_test_suite_evaluations_agent` that contains the prompt to instruct the AI agent on what to run and what to report.

A regression-check suite that:

1. Loads a fixed set of 50 curated dummy conversations. Let's make each conversation be 2 or 3 turns. Use an LLM to generate the conversations (create a generate_conversation_fixtures.py, and use LangChain + Pydantic models for structured output, use the same LLM used in production), and then save that to a conversations_fixtures.py file.
2. Runs LLM-as-a-judge on each using the batch runner.
3. Persists per-conversation scores, as well as averages across conversations.
4. Flags any deltas beyond a threshold on subsequent runs as regressions. For the first run, just store this as the "current" state. But add a mode where we can review the results against the latest run (so, you'll have to be able to persist the regression test results in Postgres).

- Add coverage for:
  - Happy-path supportive listening
  - Edge cases (short thread, multiple questions in one turn, self-disclosure)
  - Known stress tests (vague user message, strong emotion, disagreement)

### Output

- Filepaths: (within docs/automations/{folder name}/reports/{YYYY_MM_DD:HH-MM-SS}/{FINDINGS.md, *.json/other artifacts}
- Markdown report.
- Optional JSON artifact for dashboards

### Markdown report, and what it should contain

1. Run summary (top of file)

- Run timestamp, git commit/branch, fixture set version
- Total fixtures evaluated / total prompts run (e.g., "42 conversations × 26 prompts")
- Overall verdict: PASS or REGRESSIONS DETECTED (n)
- Link to the baseline file(s) being compared against

2. Regression summary table
The core of the report — one row per prompt that regressed:
Prompt | Category | Baseline | Current | Delta | Fixtures Affected
-- | -- | -- | -- | -- | --
tone_warmth | Criteria | Excellent (3) | Passable (2) | -1 | edge_case_04, stress_test_02
discloses_limitations | Behaviors | True | False | flip | happy_path_11

Group by category (Criteria / Behaviors / Safety) since they have different scoring semantics and different severity implications.

3. Pass/fail counts by category
Quick scan: Criteria: 5/6 passed, Behaviors: 11/12 passed, Safety: 8/8 passed — lets someone judge severity at a glance before reading the table.

## Completion

1. Build it.
2. Run it, show that it works.
