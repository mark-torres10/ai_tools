# Bluesky Research Infrastructure

A comprehensive data platform and research infrastructure for analyzing social media content from Bluesky. This project provides end-to-end capabilities for real-time data ingestion, ML-powered content analysis, personalized feed generation, and research tooling for social media researchers and data scientists.

## Architecture Overview

The system is built as a modular, scalable data platform with the following core components:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Bluesky       │───▶│  Data Pipeline   │───▶│  Research       │
│   Firehose      │    │  & Processing    │    │  Interface      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │  Feed Generation │
                       │  & API Services  │
                       └──────────────────┘
```

### Data Flow

1. **Ingestion**: Real-time stream processing from Bluesky's firehose
2. **Processing**: ML inference, content classification, and data enrichment
3. **Storage**: Parquet-based data lake with efficient querying capabilities
4. **Analysis**: Research interface and API for data exploration
5. **Generation**: Personalized feed algorithms and recommendation systems

## Project Setup

### Prerequisites

- **Python 3.10+** (3.10, 3.11, 3.12 supported)
- **uv** (preferred) or **conda** for package management
- **Node.js 18+** (for frontend development)
- **Docker** (for service deployment)
- **Git** with pre-commit hooks

### Quick Setup (Recommended)

Use our automated setup script for the fastest installation:

```bash
# Clone the repository
git clone https://github.com/METResearchGroup/bluesky-research.git
cd bluesky-research

# Quick setup with uv and Python 3.10 (default)
./scripts/setup_environment.sh

# Or with custom options
./scripts/setup_environment.sh --python 3.12 --env-name my-bluesky-env

# Or use conda instead of uv
./scripts/setup_environment.sh --conda --python 3.11
```

The setup script will:
- ✅ Install/validate package manager (uv or conda)
- ✅ Create virtual environment with specified Python version
- ✅ Install all project dependencies (core, dev, ML tooling)
- ✅ Set up pre-commit hooks
- ✅ Install project in editable mode
- ✅ Run validation tests to ensure everything works

**Setup Script Options:**
- `-p, --python VERSION` - Python version (3.10, 3.11, 3.12)
- `-c, --conda` - Use conda instead of uv
- `-e, --env-name NAME` - Custom environment name
- `-h, --help` - Show detailed help

### Manual Installation with uv (Recommended)

If you prefer manual setup with flexible dependency groups:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/METResearchGroup/bluesky-research.git
   cd bluesky-research
   ```

2. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Create and activate virtual environment**:
   ```bash
   uv venv --python 3.10  # or 3.11, 3.12
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. **Install project dependencies** (choose based on your needs):

   **Option A: Core only (lightweight, ~50 packages)**
   ```bash
   uv pip install -e .
   ```

   **Option B: Development setup (core + dev tools)**
   ```bash
   uv pip install -e ".[dev]"
   ```

   **Option C: Research & LLM work (without heavy ML)**
   ```bash
   uv pip install -e ".[dev,llm,valence,telemetry]"
   ```

   **Option D: Full ML stack (includes PyTorch)**
   ```bash
   uv pip install -e ".[dev,ml,llm,valence,telemetry]"
   ```

   **Option E: Everything (for CI or comprehensive development)**
   ```bash
   uv pip install -e ".[all]"
   ```

5. **Set up pre-commit hooks** (if using dev dependencies):
   ```bash
   pre-commit install
   ```

### Manual Installation with Conda

1. **Create conda environment**:
   ```bash
   conda create -n bluesky-research python=3.10  # or 3.11, 3.12
   conda activate bluesky-research
   ```

2. **Install dependencies** (choose based on your needs):
   ```bash
   # Core only (lightweight)
   pip install -e .
   
   # Development setup
   pip install -e ".[dev]"
   
   # Research & LLM work (without PyTorch)
   pip install -e ".[dev,llm,valence,telemetry]"
   
   # Full ML stack (includes PyTorch)
   pip install -e ".[dev,ml,llm,valence,telemetry]"
   
   # Everything
   pip install -e ".[all]"
   ```

### Environment Configuration

1. **Copy environment template**:
   ```bash
   cp .env.example .env
   ```

2. **Configure required environment variables**:
   - `GOOGLE_API_KEY` - For Perspective API
   - `OPENAI_API_KEY` - For LLM inference
   - `AWS_ACCESS_KEY_ID` & `AWS_SECRET_ACCESS_KEY` - For S3 storage
   - `MONGODB_URI` - For document storage (if used)

### Dependency Management

The project uses a unified `pyproject.toml` with logical dependency groups:

#### Core Dependencies (always installed)
- **Web & API**: flask, requests
- **Data Processing**: pandas, numpy, duckdb, pyarrow
- **Cloud & Storage**: boto3, atproto, peewee
- **Utilities**: matplotlib, python-dotenv, click

#### Optional Dependency Groups

**`[dev]` - Development Tools (~76 packages)**
```bash
uv pip install -e ".[dev]"
```
- pytest, ruff, pre-commit, autopep8, faker

**`[ml]` - Machine Learning (~73 packages, includes PyTorch)**
```bash
uv pip install -e ".[ml]"
```
- torch, transformers, sentence-transformers, scikit-learn, scipy

**`[llm]` - LLM Services (~135 packages, no PyTorch)**
```bash
uv pip install -e ".[llm]"
```
- openai, langchain, tiktoken, litellm, google-generativeai

**`[valence]` - Lightweight Sentiment (~55 packages)**
```bash
uv pip install -e ".[valence]"
```
- vadersentiment (minimal footprint)

**`[feed_api]` - FastAPI Service**
```bash
uv pip install -e ".[feed_api]"
```
- fastapi, uvicorn, mangum, momento (for the feed API service)

**`[telemetry]` - Monitoring & Observability**
```bash
uv pip install -e ".[telemetry]"
```
- wandb, comet-ml, sentry-sdk, prometheus-client, grafana-client

**`[all]` - Everything (~185 packages)**
```bash
uv pip install -e ".[all]"
```
- All optional dependencies combined


All package versions are resolved consistently through uv's dependency resolver, eliminating the version conflicts that existed with the previous multi-file requirements setup.

## Development Workflow

### Running Tests

The project uses pytest with comprehensive test coverage:

```bash
# Run all tests
uv run pytest

# Run specific test modules
uv run pytest lib/tests
uv run pytest ml_tooling/tests
uv run pytest services/*/tests

# Run with coverage
uv run pytest --cov=lib --cov=ml_tooling
```

### Code Quality

All code must pass linting and formatting checks:

```bash
# Run linter (will fix auto-fixable issues)
ruff check .

# Format code
ruff format .

# Pre-commit hooks (runs automatically on commit)
pre-commit run --all-files
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
