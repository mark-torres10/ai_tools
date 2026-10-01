# Proposal

Zero-shot, keep/remove, across all the LLMs. Report the label AND the probability.

## Cross-cutting concerns

### Data and analysis

Let's label all posts from Study 2. No need for a train/test split, just label everything all at once. Let's use `STUDY_2_KEEP_REMOVE_LABELS`. Let's filter only for posts with 5 labelers. On evaluation, let's split our evaluations across three datasets:

1. All: `STUDY_2_KEEP_REMOVE_LABELS` (filtered for posts with 5 labelers)
2. Unanimous: `STUDY_2_KEEP_REMOVE_UNANIMOUS_LABELS` (filtered for posts with 5 labelers)
3. Split: `STUDY_2_KEEP_REMOVE_SPLIT_LABELS` (filtered for posts with 5 labelers)

Report analysis on the three datasets:

- Total and proportion of keep/remove labels (use modal label)
- For the `STUDY_2_KEEP_REMOVE_SPLIT_LABELS`, how many posts had 1, 2, 3, and 4 removes. Calculate only from posts with 5 labelers. Report as a whole amount and as a proportion.

Report the following metrics: F1, accuracy, recall, precision

The unanimous and split datasets are generated in https://github.com/METResearchGroup/mirrorView-task/issues/325.

### Inference

Models to use (with their model IDs):

- Amazon Nova (`us.amazon.nova-micro-v1:0`)
- Qwen 3 32B (`qwen.qwen3-32b-v1:0`)
- OpenAI GPT-5.6 Terra (`us.openai.gpt-5.6-terra`)
- Claude Sonnet 5.5 (`us.anthropic.claude-sonnet-5-5`)

1. Use the Bedrock engine in `data_platform/generate_features/engines/bedrock_engine.py.`.
2. For the Pydantic model, see `shared.schemas.IsRemoveResult` for an example. This is the structured output: is_remove: bool, true when both posts in the pair should be removed. However, for our case, we want to report a probability as well. Let this be `p_remove`, the probability of removal as reported by the model.

### Storage

Locally, let's use `experiments/zero_shot_llm_inference_2026_09_30/`

Let's use S3 for storing all artifacts. The PR should only have *.py and *.md files. Use the following:

- S3 bucket: `mirrorview-experimental-artifacts`
- S3 prefix: `experiments/zero_shot_llm_inference_2026_09_30/`

### File structure

experiments/zero_shot_llm_inference_2026_09_30/
  - README.md (slim, redirects to RESULTS.md and SETUP.md)
  - SETUP.md
  - RESULTS.md
  - shared/ (shared helpers, such as a constants.py or an llm.py that manages calls to the LLM layer and uses the existing Bedrock engine or rewrites its own thin layer on top)
  - src/
    - step1_setup/*.py
    - step2_inference/*.py
    - step3_analysis/*.py

## Steps

### Setup

1. Create a dataloader that grabs the data. Should be relatively thin. Import functionality used elsewhere.
2. Create a schemas.py that creates the Pydantic model for the label. Again, thin here. Import functionality used elsewhere.

### Run inference

Here is the prompt to use:

```markdown
We are developing a new social media platform designed specifically for political discussion. As part of this process, we'd like to understand how people think content on their platform should be moderated. Your task will be to review a series of pairs of real political social media posts, and decide whether both posts in the pair should be allowed or removed from the platform.


The pairs are political mirrors of each other. This means that the mirror text recreates the original message from the opposite political stance. For example:

Original Text:
I'm a bleeding-heart liberal, and I think the issue of abortion is obviously about protecting women's rights!

Mirror Text:
I'm a staunch conservative, and abortion is fully about the sanctity of human life before birth!

Notice that the mirror text changes the core message to match that of the opposite political stance. In other words, the mirror text is not a response to the original text - it replicates the original message as if written from the opposite political stance.


Your job is to decide whether both posts in the pair should be allowed or removed from the platform.

When making your decisions, consider generally whether a post contributes to a healthy environment for political discussion, or whether it would be unhealthy for political discussion. Your goal is to evaluate the messages, using your own judgment.

Post 1: {post_1_text}

Post 2: {post_2_text}

Allow Or Remove?
```

This is imported from `experiments/predict_keep_remove_2026_07_01/models/llm_finetuning/api_baselines/prompts.py`, create a new shared/prompts.py and a BASELINE_ZERO_SHOT_KEEP_REMOVE_PROMPT variable that stores this prompt.

Run inference here using bedrock. Store the results in separate folders for each model, where the folder name is given by the model name (in your plan, specify in the folder layouts what these folders will be).

Ideally, run 1 process for each model, so that they can be done in parallel.

### Analysis

Analyze the results. Report a table, with rows equaling the models and the columns equaling the required metrics (f1, accuracy, precision, recall)
