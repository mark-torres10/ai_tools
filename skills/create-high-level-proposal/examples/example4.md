# Issue Description

This work is motivated by [this paper](https://www.alphaxiv.org/pdf/2503.11572). It would be interesting to see if, for ambiguous moderation cases, if the LLM has to "think" about various PoVs or if it expresses uncertainty. It would also be interesting to see if there's any tension displayed in their reasoning traces. We can also then compare that to humans and how long they took to moderate the same posts. Read this paper first, ideally using the AlphaXiv MCP (the `ALPHAXIV_API_KEY` is available in the env).

Let's store all this work in an experimental folder, experiments/reasoning_during_moderation_2026_09_15/

The problem we're interested in is seeing if there is a tangible difference between how LLMs think about boundary cases for moderation as opposed to really clear and obvious cases for moderation. Let's see if that happens to be the case. 

Let's split our latest study data (minimum 4 labels on a post) into three bins:

- Posts that had split labels (2/2, 3/2, 2/3).
- Posts that had unanimous keep (all labelers agreed on a label to keep the posts).
- Posts that had unanimous remove (all labelers agreed to remove posts)

Let's see how many are in each of the two groups first. If there's a nontrivial amount and it's not too imbalanced, we can proceed with the following:

- Let's use two models, `Qwen3.5 4B` and `DeepSeek-R1-Distill-Qwen-7B` (access them both via HuggingFace). Enable thinking mode for each (and do a few smoke tests to make sure that thinking mode is enabled and we can run that).
- Pass in the exact same prompt provided to users during the study itself (see https://github.com/METResearchGroup/mirrorView-task/pull/292/ for a similar experimental setup). Feel free to create a new prompts.py in shared/ that has the same prompt if you do use the same one as in the aforementioned PR link.
- Measure the number of intermediate reasoning tokens generated in the model's step-by-step thinking block before producing the final answer.

## Experiment 1

Store all work for this in {experiment folder}/experiment1/

The experimental setup is:

- For each of the 3 conditions and for each of the 2 models, measure the number of intermediate reasoning tokens generated in the step-by-step thinking block.
- Then, report the summary statistics for the number of intermediate reasoning tokens for each condition.
- Also, for each, store the actual reasoning traces, for exploratory analysis later.

Here, we don't report anything like f1,accuracy,etc as we would need a precise labeling policy (plus by virtue of setup, if some posts are split labels, we'd have to collapse into a single label anyways).

At the end, there should be 1 table, with 6 rows:

- Qwen, split labels
- Qwen, unanimous keep
- Qwen, unanimous remove
- DeepSeek, split labels
- DeepSeek, unanimous keep
- DeepSeek, unanimous remove

## Experiment 2

Store all work for this in {experiment folder}/experiment2/

We created a list of criteria in experiments/llm_prompt_engineering_2026_08_05/

Use that list of criteria and add to the prompt.

Then, rerun the setup in Experiment 1.

## Experiment 3

Let's get a human baseline. Let's look at the average response time for posts in each group in the human cases.

## Experiment 4

Do some basic exploratory analysis on the reasoning traces from Experiment 1 and Experiment 2. Things to flag:

- Are there signs of tension, opinion change, etc?
- Do this for Experiment 1 and Experiment 2. Then see, does having the criteria list given reduce the reasoning tokens used and the back-and-forth or the tension (perhaps because the LLM has been given a rubric?).

This can just be a simple bag-of-words approach as part of a V1.
