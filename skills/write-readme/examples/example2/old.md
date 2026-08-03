# Academic Torrents Reddit Pushshift Toxicity Pipeline

Chunked, resumable pipeline for Pushshift comment `.zst` files. Filters comments, scores survivors with batched Perspective API (TOXICITY only, threshold >= 0.7), and writes per-file deliverables until 50,000 high-toxic comments are accumulated globally.

**Production runs on Quest HPC:** see **[HOW_TO_RUN_ACTUAL_DATA.md](HOW_TO_RUN_ACTUAL_DATA.md)** for Bolun package ingest, Slurm submission, disk/API budgets, and monitoring.

## Setup (local smoke test)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # once, if uv < 0.11
export PATH="${HOME}/.local/bin:${PATH}"
export UV_LINK_MODE=copy
uv sync --frozen --no-dev   # or `uv sync` locally for full dev group
```

Set `GOOGLE_API_KEY` in repo-root `.env`.

## Data sources

| Source | Use case | Ingest |
|--------|----------|--------|
| **Bolun package** (Google Drive, ~16GB tar.zst) | Production — pre-filtered six subreddits, ~109M comments | `scripts/prepare_bolun_package.py` |
| **Academic Torrents** | Local smoke / single-month probes | `scripts/download_at_sample.sh` |

### Bolun package (production)

Bolun's archive contains Parquet + raw JSONL `.zst` partitioned by month. The pipeline consumes **comment JSONL** (`RC_*.zst`).

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

Staged inputs land in `data/raw/bolun/comments/RC_*.zst` (symlinks into `data/bolun/extracted/`). Inventory is cached at `data/bolun/inventory.json`.

Drive link: `https://drive.google.com/file/d/17412qQBz9UTkDGCO0F-vHjWMkJNOdTgh/view`

### Academic Torrents (smoke)

```bash
bash experiments/fetch_reddit_pushshift_dump_2026_06_15/scripts/download_at_sample.sh
bash experiments/fetch_reddit_pushshift_dump_2026_06_15/scripts/download_at_sample.sh RC_2005-12.zst
```

Tiny inspection files (e.g. `RC_2005-12.zst`, ~143 KB) are useful for format checks. Raw early-month AT files are **not** pre-filtered to the six political subreddits.

## Run

```bash
# Unit tests (no network)
PYTHONPATH=. uv run pytest experiments/fetch_reddit_pushshift_dump_2026_06_15/tests/ -q

# Process one file
PYTHONPATH=. uv run python experiments/fetch_reddit_pushshift_dump_2026_06_15/runner.py \
  --input-file experiments/fetch_reddit_pushshift_dump_2026_06_15/data/raw/bolun/comments/RC_2024-06.zst

# Orchestrator (default: max 10 files attempted)
PYTHONPATH=. uv run python experiments/fetch_reddit_pushshift_dump_2026_06_15/main.py

# Unlimited file cap; Quest production uses --stem-prefix RC_2025 (see HOW_TO_RUN_ACTUAL_DATA.md)
PYTHONPATH=. uv run python experiments/fetch_reddit_pushshift_dump_2026_06_15/main.py --max-files 0 --stem-prefix RC_2025
```

On Quest, use Slurm templates in `scripts/`:

- **`run_quest_one_month.slurm`** — calibration on one `RC_2025-*.zst` month (default `RC_2025-06`)
- **`run_quest.slurm`** — full 2025 orchestration (`--stem-prefix RC_2025`)

Details in [HOW_TO_RUN_ACTUAL_DATA.md](HOW_TO_RUN_ACTUAL_DATA.md).

## Outputs

For each scanned input file `RC_YYYY-MM.zst`:

```text
outputs/{stem}/
  metadata.json
  high_toxic_comments.parquet   # mirrorview 13 cols + prob_toxic, prob_toxic >= 0.7 only
outputs/total_metadata.json     # cumulative counts across files
```

Re-running a file whose `metadata.json` already exists logs `Skipping {stem}, metadata.json exists` and does not re-score.

## Limits (config.py)

- `GLOBAL_STOP_COUNT = 50_000` — high-toxic comments across all files
- `MAX_SESSION_API_CALLS = 1_000_000` — Perspective API calls per `main.py` session
- `MAX_FILES_TO_PROCESS = 10` — testing cap (override with `--max-files 0`)
