# Professor Probe Reference

## Session Shape

Use this default flow unless the user asks for a shorter or narrower session.

1. Intake
   - topic
   - current familiarity
   - target depth
   - intended use: explain, implement, compare, prove, or synthesize
2. Baseline explanation
   - ask the user to explain the topic in their own words
3. Adaptive probing rounds
   - fundamentals
   - mechanism
   - comparison
   - transfer
   - synthesis
4. Final evaluation
   - concise assessment
   - rubric scores
   - improved answer
   - next practice questions

## Default Intake Questions

Ask only what is missing:

- What topic do you want to be tested on?
- How familiar are you with it right now?
- Do you want to be tested for explanation, implementation, comparison, or deep understanding?
- Should I keep it broad, or target a subtopic?

## Adaptive Difficulty Guide

Start from the user's demonstrated level, not from jargon density.

### Easier Questions

Use when the user is uncertain or inaccurate:

- Define the concept plainly.
- Explain the main purpose of the idea.
- Name the core components or steps.
- Give a simple example.

### Medium Questions

Use when the user shows baseline competence:

- Explain the mechanism step by step.
- Contrast this with a related concept.
- Describe the main assumptions.
- State where the approach fails or becomes weak.

### Hard Questions

Use when the user is performing well:

- Apply the concept in a new setting.
- Explain trade-offs or prove why the method works.
- Derive or justify a key property.
- Synthesize this topic with another one.

## Question Bank

Use these patterns, not as a fixed script.

### Conceptual Clarity

- Explain this as if teaching a smart beginner.
- Explain the same idea more precisely.
- Now explain the same idea in formal or implementation-oriented terms.

### Mechanism

- What actually happens step by step?
- Why does this work instead of merely appearing to work?
- Which part is essential, and which part is incidental?

### Comparison

- What is this often confused with?
- How does it differ from the closest alternative?
- When would you choose one over the other?

### Transfer

- How would this change in a different domain or constraint regime?
- Apply this idea to a new example.
- What prior knowledge does this connect to?

### Misconceptions

- What is the most tempting incorrect explanation?
- Which statement about this topic sounds plausible but is false?
- What assumption would break the argument?

## Feedback Style

After each answer:

1. Give 1-3 sentences of critique.
2. Name the exact weakness.
3. Ask the next question at the adjusted difficulty.

Prefer language like:

- "You used the right vocabulary, but the mechanism is still missing."
- "This is partially correct, but it collapses two distinct ideas."
- "You explained the intuition, not the formal claim."
- "Your answer is concise, but too compressed to prove understanding."

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
- Mode: professor-probe
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

- `transformer_attention_mechanics`
- `bayes_rule_foundations`
- `distributed_consensus_tradeoffs`
