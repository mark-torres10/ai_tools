# Experimental gate (Layer 1)

Read when the PR is an **experiment** under `experiments/` (or equivalent `experiment/` / `exp/` tree the repo uses for experimental work).

## Fires when

Changed files live primarily under `experiments/` (or the repo’s experiment root). Productization PRs that only *mention* an experiment do not fire this gate unless the diff is the experiment itself.

## Required under Details

1. **Results summary** — Terse executive-style summary (3–6 short sentences). What was tested, what happened, what it means for a decision. No lab-notebook prose.
2. **Results table** — One clear markdown table. McKinsey-style: scannable descriptors, precise detail, decision-relevant columns. No wall of numbers without labels.

### Table format (use these columns)

| Dimension | Finding | Evidence | Implication |
|-----------|---------|----------|-------------|
| Short label for the axis (e.g. Accuracy, Latency p95, Cost / 1k) | One-line result in plain language | Concrete number, comparison, or cite (metric ±, vs baseline, n=) | So-what for the decision (ship / iterate / kill / need more data) |

Rules:

- One row per decision-relevant dimension. Prefer 3–7 rows.
- Descriptors in **Dimension** and **Finding** must be self-explanatory without reading the code.
- **Evidence** holds the hard detail; do not bury the headline in Evidence alone.
- **Implication** is action-oriented and terse.
- If results are not yet available, say so in the summary and omit fabricated rows; ask the user for numbers rather than inventing them.

## Example shape

```markdown
### Results summary

Compared chronological vs embedding rerank on a 2-week holdout (n=12k impressions).
Rerank lifts offline NDCG@10 and hurts p95 latency within budget.
Recommend a 5% production experiment next; do not full-roll yet.

### Results

| Dimension | Finding | Evidence | Implication |
|-----------|---------|----------|-------------|
| Ranking quality | Rerank beats chronological | NDCG@10 0.41 → 0.47 (+6 pts), n=12k | Worth online test |
| Latency | Slower but inside SLO | p95 48ms → 71ms (SLO 100ms) | Acceptable for 5% traffic |
| Cost | Modest increase | +$0.12 / 1k requests | Fine at 5%; revisit at 50% |
| Failure mode | Cold-start users flat | No lift for accounts <7d | Exclude or separate treatment |
```

## Checklist

- [ ] Diff is under `experiments/` (or repo experiment root)
- [ ] Executive summary is terse and decision-oriented
- [ ] Table uses Dimension / Finding / Evidence / Implication
- [ ] No invented metrics; missing results → prompt user
- [ ] No lab-notebook dump
