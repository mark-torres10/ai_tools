# Issue Description

What we want to do is use LLMs for text mining, as described in https://github.com/METResearchGroup/lab_wiki/blob/main/docs/manuals/methods/HOW_TO_MINE_TEXT_FOR_FEATURES.md#approach-3-asking-an-llm-to-give-features

We want to actually mine features from our ~20,000 posts.

## Cross-cutting concerns

- Store all static assets into S3. The PR should only contain .py and .md files. S3 bucket should be same as other experiments here and prefix should be experiments/study_2_llm_based_feature_extraction_2026_09_29/
- Before running any LLM step, do a smoke test on 5 queries and from that, generate estimates for runtime, total tokens (input/output), and price estimate. Report low/median/high estimates for each. Report as a table where the rows are the values and the columns are low/median/high estimates. Let low and high be +/- 20% estimates of the median.
- Do all work in experiments/study_2_llm_based_feature_extraction_2026_09_29/

### File structure

```
experiments/study_2_llm_based_feature_extraction_2026_09_29/
  - README.md (slim, redirects to RESULTS.md and SETUP.md)
  - SETUP.md
  - RESULTS.md
  - shared/ (shared helpers, such as a constants.py or an llm.py that manages calls to the LLM layer and uses the existing OpenAI engine or rewrites its own thin layer on top)
  - src/
     - step1_setup/*.py
     - step2_mine_candidate_features/*.py
     - step3_embed_features/*.py
     - step4_cluster_records/*.py
     - step5_name_clusters/*.py
     - step6_label_posts_with_features/*.py
     - step7_analyze_post_features/*.py, *.{html,css,js} (for the webapp)
```

## Procedure

What we want to do is something like:

### Setup

- Assign a keep/remove label to each original+mirror combination based on the modal label. Stick to posts with exactly 5 labels.
- Then, create batches. Each batch is 10 posts with a majority keep label and 10 posts with a majority remove label.

### Mining candidate features

- Take each batch. Interpolate it into a prompt template.
- Run using the OpenAI batch API. Let's use GPT 5.6 Terra. Use the OpenAI engine that already exists in the codebase. Use structured output.
- The Pydantic model should have fields `features_from_kept_posts` and `features_from_removed_posts`. Within each of those two keys should be another object with keys `lexical`, `topic_subject`, `semantic_content`, `pragmatics`, `target`, `structure`. Each of these keys should have a list of strings, each string being a discovered feature.

The output should render to something like:

```json
{
  "features_from_kept_posts": {
      "lexical": ["...", "..."],
      "topic_subject": ["...", "..."],
      "semantic_content": ["...", "..."],
      "pragmatics": ["...", "..."],
      "target": ["...", "..."],
      "structure": ["...", "..."]
   },
  "features_from_removed_posts": {...}
}
```

The candidate generation prompt that I want used is something like:

```markdown
## Task

You are a computational linguistics analyst studying social-media posts from a keep/remove moderation task.

You will be shown a batch of posts that human annotators kept on the platform and a batch of posts that human annotators removed. Your job is to consider them jointly, and to find features that are distinct to the posts that were kept and distinct to the posts that were removed.

Return as structured output.

## Categories of features

Here are the categories that we want to consider:

### Category 1: Surface and lexical (`lexical`)

This category is about how the post is written, not what claim it makes. It covers length, slang, heavy punctuation, all-caps emphasis, profanity, hashtags and account mentions, and a high density of proper names.

Examples include emphatic typography, profane derogatory insults, colloquial language and insults, and hashtags and account mentions.

### Category 2: Topic and subject matter (`topic_subject`)

This category is about the subject of the post. Examples include a policy area (guns, climate, immigration, abortion, elections), a specific event or bill, a geographic scope, a historical analogy, and culture-war salience.

### Category 3: Semantic content (`semantic_content`)

This category is about the kind of claim the post makes. Examples include causal claims, moral language, a factual claim versus speculation, conspiracy, a claim that a group is being persecuted, a policy prescription, and a cost-benefit argument.

### Category 4: Pragmatics and communicative intent (`pragmatics`)

This category is about what the post is doing to the reader. Examples include sarcasm, mockery, a call to action, persuasion, venting, hedging, and outrage.

### Category 5: Target and directionality (`target`)

This category is about who the post attacks or praises, and which political side it points at. Examples include the type of actor criticized or praised, a left/right cue, us-versus-them framing, and elite-versus-populist framing.

### Category 6: Compositional and syntactic structure (`structure`)

This category is about the shape of the sentences. Examples include if-then conditionals, contrast with "but" or "however," rhetorical questions, parallel repetition, lists, quoted or attributed speech, and direct address in the second person.

## Stimuli

### Posts that were kept

Here are ten post pairs that were kept by human annotators:

{Enumerated post pairs}

### Posts that were removed

Here are ten post pairs that were removed by human annotators:

{Enumerated post pairs}

## Task (repeated)

...

```

### Embed the feature records and cluster them

- Take all the features across the batches and do some light deduplication (exact string match after lowercase and removing stopwords).
- Then embed the features (let's use Amazon Titan embeddings)
- Then cluster the features (let's use HDBSCAN, with seed = 1)

### Name each cluster

- An LLM sees a sample of the features in one cluster and returns a label of at most eight words plus a one-sentence definition.
- Similar caveats as before. Run using the OpenAI batch API. Let's use GPT 5.6 Terra. Use the OpenAI engine that already exists in the codebase. Use structured output and define the Pydantic model as part of your plan.

### Label every post against the features

- Let's see how many features and the relative number of posts that have each feature from above. Prompt the user here for some feedback and suggestions.
- Once confirmed, let's use Jev to label every post against the features. Let's do 1 original+mirror post at a time, and let's return a noul for each of the features.
- Then given that, let's set an arbitrary threshold for now of p=0.7 (put this in a constants.py), and let's return a feature label for each post and feature. This should give us a table where the rows are on unique original+mirror, and columns are post ID, original text, mirror text, and then is_{label name}, with a 0 or 1 (also include a LABEL_TO_DETAIL constant with a hash map where the key is the `is_{label}` column name and the value is a dictionary with keys "name" (for a human-readable name for the feature, used by visualizations) and "description" (the 1-sentence description or definition generated in the "Name each cluster" section).

For the Jev prompt, start with something like this:

```markdown
You are labeling one social-media post against an approved feature list.

For each feature, return present=true when the feature clearly applies to the
post text, otherwise present=false. Use only the provided feature definitions.

Features:
{feature json}
```

### Report analyses

Given this, report analyses. Store these in an analyses/ folder. Then, generate a UI in Vercel, using HTML, that displays the key results. For visuals, use https://github.com/rhiever/evident-charts/blob/main/skills/evident-charts/SKILL.md to generate better visuals.

Some of the key questions we care about include:

1. Which topics most commonly appear?
2. Which topics are more common in left leaning posts, and which in right leaning posts? (looking at posts where the original was left/right leaning)
3. Which topics are more common for (original) posts at low, medium, and high toxicity?
4. Which topics did Democratic/Republican raters keep, and which did they remove?
5. For posts that had 0, 1, 2, 3, 4, or 5 removes (keep only posts with 5 labels), what were the top 10 most common topics for each? Report as a table.
