# Fix evaluation metrics joined on shuffled row order

## Summary

The evaluation harness joined model predictions to labels by row index after shuffling the eval set, so metrics compared unrelated examples and could falsely report improvement.

Predictions are now matched to labels by stable `example_id` before scoring.

## Purpose

Offline eval runs that shuffle for batching or stratified sampling produce nonsense precision/recall (or accuracy) and can green-light a worse model.

This fix corrects join semantics in the harness scoring step. Changing train/serving feature parity checks and live A/B metrics is out of scope.

## Reproduction

Setup: an eval set with distinct `example_id`s; a predictions file ordered differently from labels (or harness shuffle enabled).

1. Score a fixed model checkpoint against the eval set with shuffle on.
2. Record headline metrics (e.g. accuracy or F1).
3. Re-run with shuffle off (or a different seed) against the same checkpoint and labels.

Expected: Metrics are identical across runs for the same checkpoint and label set.

Actual: Metrics change with shuffle order; inspecting a few rows shows prediction `i` paired with label `j` where `example_id`s differ.

## Root cause

After shuffle, the harness aligned the predictions frame to the labels frame by positional index instead of by `example_id`. Positional join is only valid when both frames share the same unshuffled order.

## Fix

Scoring now inner-joins predictions and labels on `example_id` (failing the run if required IDs are missing or duplicated) and computes metrics on the joined frame. Row order no longer affects pairing.

## How to verify

```bash
pytest tests/eval/test_harness_join.py -q
```

1. Run the same checkpoint twice with different shuffle seeds; metrics must match within floating-point tolerance.
2. Corrupt predictions by permuting rows but keeping `example_id`; metrics must still match the unpermuted run.
3. Drop or duplicate an `example_id` in predictions; the harness must fail with a clear join error instead of silently scoring.
4. Spot-check a tiny three-row fixture: shuffled input yields the same per-id pairs as sorted input.
