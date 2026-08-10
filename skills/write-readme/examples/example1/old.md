# Phase 1 Free-Response Analysis

## Summary

Describes Phase 1 pair-reflection free responses and paired influence ratings from the MirrorView Study Phase 2 Part 1 pilot export, broken down by party × condition (`training` vs `training_assisted`).

Influence ratings are moderately high overall (mean 4.86, median 5.0 on a 1–7 scale). `training_assisted` rates higher than `training` for both Democrats and Republicans. Reflection length is comparable across cells. Keyword theme EDA points most often to civility / harm framing.

## Purpose

Establish a descriptive read of whether the Phase 1 pair-reflection exercise felt influential, and what users say they attended to when reflecting.

The experiment is intended to identify:

- Whether assisted training looks more influential than unassisted training
- Whether party × condition cells differ in rating level or distribution shape
- Whether reflection themes align with MirrorView design goals (form and conversational value of speech, not pure ideological agreement)

## Setup

- Dataset: `STUDY_PHASE_2_PART_1_RESULTS_PILOT` via `shared.data.dataloader` → `shared/data/raw/study_phase_2_part_1/results/pilot.csv`
- Method: descriptive summaries, keyword theme matching, and Matplotlib plots (no inference model)
- Filter: `phase == 1`, non-empty `phase1_pair_reflection_text`, numeric `phase1_pair_influence_rating`
- Conditions retained after filter: `training`, `training_assisted`
- Party groups: `democrat`, `republican`
- Primary outcomes: influence rating (1–7); secondary: reflection length and theme keyword shares
- Theme matching: simple regex keyword categories (civility / harm, evidence / truth, productive discussion, pair comparison, personal agreement)

Yields 1,320 rows from 1,316 distinct users. Analysis is descriptive only: no significance tests, no participant-level covariates, and theme coding is keyword-based EDA.

## Flow

```text
load STUDY_PHASE_2_PART_1_RESULTS_PILOT
→ filter Phase 1 reflections with valid influence ratings
→ cache filtered CSV (reuse on later runs)
→ summarize ratings, lengths, themes, and top terms by party × condition
→ write plots under plots/
```

## Run

From the repo root:

```bash
PYTHONPATH=. uv run python experiments/free_response_analysis_2026_04_28/main.py
```

On first run, writes `phase1_free_response_filtered.csv` in this directory. Later runs reuse that cache if present. Delete the cached CSV to rebuild from the registered pilot export.

## Results

### Overall

| Measure | Value |
| --- | ---: |
| Filtered rows | 1,320 |
| Distinct users | 1,316 |
| Mean influence rating | 4.855 |
| Median influence rating | 5.000 |
| Mean reflection length | 26.974 words |

### Main descriptive pattern

`training_assisted` has higher mean influence than `training` in both party groups. Democrats in `training_assisted` sit at the top of the cell means; Republicans in `training` sit at the bottom and show a thicker low-rating tail. Word-count distributions look broadly similar across cells, so rating differences do not look like a verbosity artifact.

### Theme and term notes

Row-normalized theme shares put civility / harm first in every party × condition cell. Top non-stopword terms cluster around posts, speech, language, and allow/remove decisions. The Republican `training` cell is notable for `free` / misspelled `speach`, suggesting free-speech framing in that subgroup.

### Outputs

- `phase1_free_response_filtered.csv` — cached filtered analysis table
- `plots/mean_influence_by_party_condition.png` — cell means with approximate 95% CIs
- `plots/influence_rating_distribution.png` — rating boxplots by party × condition
- `plots/reflection_word_count_boxplot.png` — reflection length by party × condition
- `plots/theme_mentions_heatmap.png` — row-normalized theme shares

Console tables cover overview counts, rating summaries and histograms, text-length stats, theme proportions, top terms, and one high-influence example per cell. See [`WRITEUP.md`](WRITEUP.md) for narrative detail and embedded plot interpretation.

## Conclusion

Treat assisted training as descriptively more influential than unassisted training in this pilot slice. Users mostly report moderation criteria tied to civility, harm, and pair symmetry—aligned with MirrorView’s design goal of judging form and conversational value rather than pure agreement.

Do not treat these patterns as causal or inferential. A next pass should add formal tests on rating differences and a stronger qualitative coding procedure for reflection themes.
