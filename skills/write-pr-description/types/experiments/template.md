# <Experiment Name>

**Date:** YYYY-MM-DD
**Status:** Planned | Running | Complete | Abandoned

## Summary

Compared <conditions or methods> on <task, dataset, or evaluation>.

<Main result>. <Important secondary finding or tradeoff>.

## Purpose

Determine whether <experimental variable> affects <outcome or decision>.

The experiment is intended to identify:

- <question or decision>
- <question or decision>
- <question or decision>

## Setup

- Dataset:
- Model or method:
- Conditions:
- Prompt or configuration:
- Primary metric:
- Secondary metrics:
- Random seeds:
- Important fixed parameters:

<Optional sentence explaining what changed and what remained fixed.>

## Flow

```text
input data
→ prepare conditions
→ run experiment
→ calculate results
→ compare conditions
````

## Run

```bash
python run_experiment.py \
  --config configs/<experiment>.yaml
```

## Results

| Condition | Primary metric | Secondary metric |
| --------- | -------------: | ---------------: |
|           |                |                  |
|           |                |                  |

Outputs:

* `outputs/<artifact>`
* `outputs/<artifact>`

## Conclusion

<Decision supported by the results>.

<Important qualification or highest-value follow-up experiment>.
