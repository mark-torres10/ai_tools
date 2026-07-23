# Conversational Context Ablation

**Date:** 2026-07-22
**Status:** Complete

## Summary

Compared classification using the target post alone, the target post plus its direct parent, and the full preceding conversation thread.

Adding the direct parent improved recall and overall F1. Providing the full thread increased recall further but reduced precision, resulting in no additional improvement over the parent-only condition.

## Purpose

Determine how much conversational context should be provided when classifying a target post.

The experiment tests whether context helps the model interpret replies, quotations, references, and ambiguous targets, and whether broader thread context introduces irrelevant or misleading information.

## Setup

* Dataset: `data/eval/test.csv`
* Model: `qwen3-32b`
* Prompt: `prompts/classification_v2.txt`
* Conditions:

  * Target post only
  * Target post plus direct parent
  * Full preceding thread
* Primary metric: F1 for `is_remove=1`
* Secondary metrics: Accuracy, precision, and recall
* Temperature: `0`
* Maximum context length: `8,192` tokens

The same target posts were used in every condition. Only the amount of context included in the input changed.

## Flow

```text
labeled target posts
→ retrieve conversation context
→ construct input variants
→ run inference
→ calculate metrics
→ compare changed predictions
```

## Run

```bash
python run_experiment.py \
  --config configs/context_ablation.yaml
```

## Results

| Context         | Accuracy | Precision | Recall |   F1 |
| --------------- | -------: | --------: | -----: | ---: |
| Target only     |     0.70 |      0.63 |   0.55 | 0.59 |
| Target + parent |     0.71 |      0.62 |   0.61 | 0.61 |
| Full thread     |     0.69 |      0.58 |   0.64 | 0.61 |

Outputs:

* `outputs/predictions_target_only.csv`
* `outputs/predictions_target_and_parent.csv`
* `outputs/predictions_full_thread.csv`
* `outputs/context_comparison.csv`
* `outputs/changed_predictions.csv`

## Conclusion

Use the target post and its direct parent as the default input representation.

The direct parent supplies useful local context without exposing the classifier to the additional speakers, topics, and harmful language that can appear elsewhere in a longer thread. A follow-up experiment should test selectively retrieved context rather than including the full thread.
