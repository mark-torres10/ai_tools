# Manager Probe Reference

## Session Shape

Use this default flow unless the user asks for a shorter or narrower session.

1. Intake
   - topic
   - audience
   - stage of work
   - desired depth
2. User explanation
   - ask the user to explain the work in their own words
3. Probing rounds
   - requirements
   - assumptions
   - architecture and trade-offs
   - non-functional requirements
   - rollout, failure modes, and metrics
4. Final evaluation
   - concise assessment
   - rubric scores
   - improved answer
   - next practice questions

## Default Intake Questions

Ask only what is missing:

- What is the feature, system, or decision?
- Who is the audience you are trying to explain this to?
- What stage is the work in: idea, design, implementation, rollout, or postmortem?
- What do you most want pressure-tested?

## Probing Question Bank

Use these patterns, not as a script but as a menu.

### Problem And Scope

- What problem are you solving, and for whom?
- What is explicitly in scope, and what is out of scope?
- How will you know the change succeeded?

### Requirements

- What are the functional requirements?
- Which requirements are hard constraints versus nice-to-haves?
- What assumptions are you making about upstream or downstream systems?

### Non-Functional Requirements

- What are the latency or throughput expectations?
- What reliability target matters here?
- What security or privacy properties must hold?
- What are the cost or operational constraints?

### Design And Trade-Offs

- Why is this design better than the main alternative?
- What did you optimize for, and what did you explicitly de-optimize?
- Where does the design become fragile at larger scale?

### Execution Realism

- What is the rollout plan?
- How will you detect failure quickly?
- What is the rollback path?
- What tests and observability are required before launch?

### Failure Modes

- What breaks if an assumption is false?
- Which edge case is most likely to surprise you in production?
- What is the most expensive failure mode here?

## Feedback Style

After each answer:

1. Give 1-3 sentences of critique.
2. Name what was missing or weak.
3. Ask the next question at the right level.

Prefer language like:

- "This answer is directionally right but too vague on..."
- "You named the component, but not the mechanism."
- "You explained the happy path, but not the operational failure case."
- "Your trade-off is asserted, not justified."

## Scoring Rubric

Score each category from 0 to 10. Be conservative.

- `comprehension`: Does the user show real understanding instead of repeating labels?
- `correctness`: Are the statements accurate and internally consistent?
- `precision`: Are terms, boundaries, and mechanisms stated concretely?
- `depth`: Does the answer reach mechanism level rather than surface summary?
- `reasoning`: Are causal links, trade-offs, and decisions justified?
- `transfer`: Can the user connect the topic to adjacent systems or analogous cases?
- `edge_cases`: Does the user address failures, exceptions, and boundary conditions?
- `communication`: Is the answer organized and audience-aware?
- `brevity`: Is it concise without omitting critical content?
- `confidence_calibration`: Does the user distinguish facts, assumptions, and unknowns?

Interpretation:

- `0-3`: weak or mostly incorrect
- `4-5`: partial understanding with major gaps
- `6-7`: solid baseline, still missing important nuance
- `8-9`: strong and defensible
- `10`: unusually rigorous, precise, and complete

## Report Template

Write `probe_understanding/<timestamp>_<topic_slug>/main.md` using this template:

```markdown
# Probe Understanding Report

## Session
- Mode: manager-probe
- Topic: <topic>
- Timestamp: <YYYY_MM_DD-HH:MM:SS>
- Goal: <why the user ran this>

## Summary
<2-5 sentence assessment>

## Scores (/10)
- Comprehension: x/10
- Correctness: x/10
- Precision: x/10
- Depth: x/10
- Reasoning: x/10
- Transfer: x/10
- Edge cases: x/10
- Communication: x/10
- Brevity: x/10
- Confidence calibration: x/10

## Strongest Areas
- ...

## Gaps And Critique
- ...

## Suggested Better Answer
<short model answer or improved framing>

## Next Questions To Practice
1. ...
2. ...
3. ...
```

## Timestamp And Slug

Use a local timestamp in this exact format:

`YYYY_MM_DD-HH:MM:SS`

If you need to generate it in the shell, use:

`date +"%Y_%m_%d-%H:%M:%S"`

Slug rules:

- lowercase
- ASCII only
- replace spaces with underscores
- remove punctuation except underscores
- keep it short and specific

Examples:

- `system_design_foo_feature`
- `ai_rag_latency_tradeoffs`
- `db_migration_backfill_plan`
