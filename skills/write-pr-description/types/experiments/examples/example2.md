# Training-Set Size Ablation

**Date:** 2026-07-22
**Status:** Complete

## Summary

Trained the same ModernBERT classifier on 10%, 25%, 50%, and 100% of the available labeled training data.

Performance improved consistently as the training set grew, but the largest gains occurred before the 50% condition. Training on the full dataset produced the best result, although the improvement over 50% was comparatively small.

## Purpose

Measure how sensitive model performance is to the amount of labeled training data.

The experiment is intended to identify:

* Whether additional labeled data remains valuable
* A smaller training subset suitable for faster development
* Whether the current learning curve suggests prioritizing more labels or improvements to the modeling approach

## Setup

* Dataset: `data/splits/`
* Model: `modernbert-base`
* Training sizes:

  * 10%
  * 25%
  * 50%
  * 100%
* Validation and test sets: Fixed across conditions
* Primary metric: F1 for `is_remove=1`
* Secondary metrics: Accuracy and ROC-AUC
* Seeds: `42`, `43`, and `44`
* Epochs: `5`
* Early stopping: Validation F1

Training subsets were stratified by label and nested so that smaller conditions were contained within larger conditions.

## Flow

```text
training data
→ create stratified subsets
→ train each condition
→ evaluate on fixed test set
→ aggregate across seeds
→ compare learning curve
```

## Run

```bash
python run_experiment.py \
  --config configs/training_size_ablation.yaml
```

## Results

Results are averaged across three random seeds.

| Training data | Accuracy |   F1 | ROC-AUC |
| ------------: | -------: | ---: | ------: |
|           10% |     0.63 | 0.43 |    0.66 |
|           25% |     0.66 | 0.49 |    0.70 |
|           50% |     0.69 | 0.54 |    0.73 |
|          100% |     0.69 | 0.56 |    0.74 |

Outputs:

* `outputs/run_metrics.csv`
* `outputs/aggregate_metrics.csv`
* `outputs/learning_curve.png`
* `outputs/predictions/`

## Conclusion

Use the full dataset for final reported models and the 50% subset for routine development.

The results suggest that additional labeled data still helps, but future data collection may be most useful when targeted toward rare or difficult examples rather than simply increasing the dataset uniformly.
