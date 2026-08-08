# Academic Torrents Reddit Pushshift Toxicity Pipeline

## Context

We needed to up-sample toxic posts. However, we could not sample enough data from the Reddit API, the Bluesky API, and the Twitter API in order to do so, so we made use of the PushShift dataset. In our HPC cluster, we have a terabyte of this data compressed into a series of files. We needed a way to sample relatively recent content and get a subset that met our criteria for high-toxic posts as determined by the Google Perspective API.

## Solution

This folder contains all the work related to this solution.

The steps include:

1. Logging into Quest
2. Downloading and extracting a dataset from Bolun's data.
3. Run a one-month test run, to get the code working.
4. Run for all 2025 posts, until you get enough toxic samples.

There are a few other files that are used as well.

We received ~109M comments (from 6 political subreddits, given certain keywords) as a ~16GB `tar.zst` file in Google Drive.

We downloaded the files from Google Drive to Quest (see `prepare_bolun_package`). We confirmed that we had data from January to June 2025.

Then we did a test run on one-month, June 2025, to check some basic stats before committing to a full run. We wanted to take each post and run the Google Perspective API to classify its toxicity and then grab the posts that met our threshold for "high toxicity" (p >= 0.7).

Once we confirmed this, we ran a larger batch job, running for all posts in our data dump until we either hit 50k high-toxicity posts or 1M API calls, whichever came first.

## Setup

We use `uv` for the Python setup.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # once, if uv < 0.11
export PATH="${HOME}/.local/bin:${PATH}"
uv sync --frozen --no-dev   # or `uv sync` locally for full dev group
```

## Implementation steps

### Extracting records from the Google Drive data dump

Bolun's archive contains Parquet + raw JSONL `.zst` partitioned by month.

```bash
# Full prepare: download, extract, stage symlinks, print inventory table
PYTHONPATH=. uv run python \
  experiments/fetch_reddit_pushshift_dump_2026_06_15/scripts/prepare_bolun_package.py \
  --all

# If tarball already downloaded manually:
PYTHONPATH=. uv run python \
  experiments/fetch_reddit_pushshift_dump_2026_06_15/scripts/prepare_bolun_package.py \
  --extract --stage --inventory --skip-row-counts
```

Staged inputs land in `data/raw/bolun/comments/RC_*.zst` (symlinks into `data/bolun/extracted/`).

We keep track of what's in the compressed file during extraction using a `inventory.json`. This stores the files that were successfully extracted, for which month, and the relative size. This gives us a peek into how extraction is going as well as how large each file is, without loading each file.

[Here's the Google Drive link to the data dump.](https://drive.google.com/file/d/17412qQBz9UTkDGCO0F-vHjWMkJNOdTgh/view)

### Getting a sense for the data types without loading the data

Given the size of the extracted datasets (they were ~16GB compressed, so they were a bit larger uncompressed), we wanted to iterate quickly using some test data. Downloading Reddit PushShift data from  early on, e.g., 2005, yields only a few rows, but the fields are consistent, so we can iterate on our scripts using these as starter datasets.

```bash
bash experiments/fetch_reddit_pushshift_dump_2026_06_15/scripts/download_at_sample.sh
bash experiments/fetch_reddit_pushshift_dump_2026_06_15/scripts/download_at_sample.sh RC_2005-12.zst
```

Tiny inspection files (e.g. `RC_2005-12.zst`, ~143 KB) are useful for format checks, but are not actually useful for development (as these don't have the posts we want and are far too old).

### Run the full extraction and classification

Once we get a sense for the format, we can now run the full extraction and classification pipeline.

This involves:

1. Loading in a given file.
2. Running it through the Perspective API to get toxicity scores.
3. Saving the ones that meet our criteria for "high toxicity".
4. Continuing until a stop condition is met.

```bash

# Process one file
PYTHONPATH=. uv run python experiments/fetch_reddit_pushshift_dump_2026_06_15/runner.py \
  --input-file experiments/fetch_reddit_pushshift_dump_2026_06_15/data/raw/bolun/comments/RC_2024-06.zst

# Orchestrator (default: max 10 files attempted)
PYTHONPATH=. uv run python experiments/fetch_reddit_pushshift_dump_2026_06_15/main.py

# Unlimited file cap; Quest production uses --stem-prefix RC_2025
PYTHONPATH=. uv run python experiments/fetch_reddit_pushshift_dump_2026_06_15/main.py --max-files 0 --stem-prefix RC_2025
```

Since there's not enough memory to run this as a regular Python script on the default login nodes on Quest, we have to submit these as Slurm jobs. We have two scripts for this:

- `run_quest_one_month.slurm`: a test run on one file`RC_2025-*.zst` month (default `RC_2025-06`)
- `run_quest.slurm` — full run on all 2025 data (`--stem-prefix RC_2025`)

## Outputs

For each scanned input file `RC_YYYY-MM.zst`:

```text
outputs/{stem}/
  metadata.json
  high_toxic_comments.parquet
outputs/total_metadata.json     # cumulative counts across files
```

We want to avoid expensive re-computation, so re-running a file whose `metadata.json` already exists logs `Skipping {stem}, metadata.json exists` and does not re-score (this assumes that file completed processing, which is an OK assumption on our end).

In `experiments/fetch_reddit_pushshift_dump_2026_06_15/outputs`, we store the outputs from `2025-05` and `2025-06`, as running these datasets gave us the total amount of high-toxicity posts that we needed (see `experiments/fetch_reddit_pushshift_dump_2026_06_15/outputs/total_metadata.json` for more details).
