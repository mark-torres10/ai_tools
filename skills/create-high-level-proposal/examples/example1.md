# Proposal: Zero-shot Jev inference on the Study 2 dataset

Scope: [issue 330](https://github.com/METResearchGroup/mirrorView-task/issues/330). This proposal covers only (1) the file structure, (2) the schema models, and (3) the Jev code. Everything else follows [issue 326](https://github.com/METResearchGroup/mirrorView-task/issues/326) and its plan in `docs/plans/2026-10-01_study_2_zero_shot_llm_inference_3187fc/`.

## Cross-cutting concerns

### Root-level Jev module

The core Jev code moves to a new root package, `shared/models/jev/`, so that later experiments can import it. The experiment keeps only the parts specific to the keep/remove task.

The split follows one rule: **root `shared/` never imports from `experiments/`.** Anything that depends on issue 326's prompt or schemas therefore stays in the experiment. So does anything that names this experiment's S3 prefix or model folder.

| Moves to `shared/models/jev/` | Stays in `experiments/zero_shot_jev_inference_2026_10_01/shared/` |
| --- | --- |
| Model ID, secret ID, timeout, retry backoff, rate limit, pricing | Experiment name, S3 prefix, `jev_1_13_0` folder name |
| `JevResult`: what one Jev call returns | Mapping a `JevResult` to 326's `PredictionRecord` |
| `TypeSafeClassifier` construction and API key lookup | Keep/remove instructions, built from 326's prompt |
| `JevScorer`: rate limiting, retries, response checks | `build_remove_request` (posts → `state`, remove `Noul`) |
| `RequestStartLimiter` | 0.5 remove threshold |

The root module is not tied to any task. It takes any `ClassifierRequest` and returns every requested `Noul` probability by question ID. That is why the returned type is a general `JevResult` and not `JevRemoveScore`.

### Reuse from issue 326

This proposal assumes issue 326's Step 1 exists. From `experiments/zero_shot_llm_inference_2026_09_30/shared/` the experiment imports:

- `prompts.py`: `BASELINE_ZERO_SHOT_KEEP_REMOVE_PROMPT`
- `schemas.py`: `ModelDefinition`, `Study2InputRecord`, `RemovePrediction`, `TokenUsage`, `PredictionRecord`, `FailureRecord`, `ModelRunManifest`, `InputManifest`
- `storage.py`: JSONL serialization, SHA-256, immutable writes
- The prepared input at `inputs/study_2_five_labeler/`

### Jev package

The integration is `langchain-typesafe==0.0.1a3` (`TypeSafeClassifier`). It is marked `@beta` and has no built-in retries. Root `shared/` code gets imported by many experiments, so the package should go in `pyproject.toml` rather than being pulled in per command with `uv run --with` (see decision 1).

## File structure

### Repository

```text
shared/
  models/
    __init__.py
    jev/
      __init__.py           public API re-exports
      constants.py          JEV_MODEL_ID, secret, timeout, backoff, rate limit, pricing
      schemas.py            JevResult
      client.py             get_jev_api_key, build_jev_classifier
      rate_limit.py         RequestStartLimiter (copied from Study 2's shared/jev.py)
      scorer.py             JevScorer, parse_response, build_jev_scorer

experiments/zero_shot_jev_inference_2026_10_01/
  README.md                 (slim, redirects to SETUP.md and RESULTS.md)
  SETUP.md
  RESULTS.md
  __init__.py
  shared/
    __init__.py
    constants.py            experiment name, S3 prefix, JEV_MODEL definition, request keys, threshold
    jev.py                  keep/remove instructions, build_remove_request, to_prediction_record
    storage.py              S3 key builders rooted at this experiment; everything else imported from 326
  src/
    __init__.py
    step1_setup/
      __init__.py
      prepare.py            copies 326's records.jsonl and manifest.json byte for byte and checks the SHA-256
    step2_inference/
      __init__.py
      run.py                one Jev process: --run-id, optional --limit, --max-workers; resumable
    step3_analysis/
      __init__.py
      analyze.py            joins predictions to gold labels; reuses 326 metric functions
      render.py             RESULTS.md tables
```

The experiment no longer has `shared/schemas.py` or `shared/prompts.py`. Its schemas come from 326 and `shared.models.jev`, and its prompt comes from 326.

`experiments/study_2_llm_based_feature_extraction_2026_09_29/` is left unchanged. Pointing its Step 6 at `shared.models.jev` is a separate follow-up, because its `JevScorer` wraps the older `typesafe_sdk.system_one` API.

### S3

```text
s3://mirrorview-experimental-artifacts/experiments/zero_shot_jev_inference_2026_10_01/
  inputs/
    study_2_five_labeler/
      records.jsonl         byte copy of 326's prepared input
      manifest.json         byte copy; SHA-256 must match
  runs/
    RUN_ID/
      jev_1_13_0/
        predictions/batch-000000.jsonl ...
        failures/batch-000000.jsonl ...
        manifests/manifest-000000.json ...
  analysis/
    RUN_ID/
```

The `jev_1_13_0/` folder uses the same layout as one 326 model folder. That lets 326's analysis read it as a fifth model without changes.

## Schema models

| Model | Lives in | Role |
| --- | --- | --- |
| `JevResult` | `shared/models/jev/schemas.py` (**new**) | Returned by every `JevScorer.score` call: `nouls` by question ID, `model`, `request_id`, token counts, `latency_ms`, `attempts`. |
| `Study2InputRecord` | 326 | Input to `build_remove_request`. |
| `RemovePrediction` | 326 | `is_remove` is computed as `p_remove >= 0.5`, so 326's threshold validator always passes. |
| `TokenUsage` | 326 | Built from `JevResult`. When Jev returns `None`, the count is stored as `0`. |
| `PredictionRecord` | 326 | One per post, built by `to_prediction_record`. |
| `FailureRecord`, `ModelRunManifest`, `InputManifest`, `ModelDefinition` | 326 | Used unchanged. |

`JevResult` exists only in memory. `PredictionRecord` rejects extra fields, so `request_id`, `latency_ms`, and `attempts` are not saved (see decision 4).

### `shared/models/jev/constants.py`

```python
"""Jev model, secret, and request settings shared across experiments."""

JEV_MODEL_ID = "jev-1.13.0"
JEV_SECRET_ID = "jev-typesafe-api-key"
JEV_SECRETS_REGION = "us-east-2"
JEV_REQUEST_TIMEOUT_SECONDS = 120.0
JEV_RETRY_BACKOFF_SECONDS = (1.0, 2.0, 4.0)
JEV_MAX_REQUESTS_PER_MINUTE = 1000
JEV_USD_PER_MILLION_INPUT = 0.042
JEV_USD_PER_MILLION_OUTPUT = 0.0
```

These values match the Jev constants in `experiments/study_2_llm_based_feature_extraction_2026_09_29/shared/constants.py`.

### `shared/models/jev/schemas.py`

```python
"""Typed result of one Jev request."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class JevResult(BaseModel):
    """Noul probabilities, usage, and request metadata from one Jev call."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    model: str = Field(min_length=1)
    request_id: str | None
    nouls: dict[str, float] = Field(min_length=1)
    input_tokens: int = Field(ge=0)
    output_tokens: int = Field(ge=0)
    latency_ms: float = Field(ge=0.0)
    attempts: int = Field(ge=1)

    def noul(self, question_id: str) -> float:
        """Return P(yes) for one Noul question.

        Raises
        ------
        KeyError
            When the result has no answer for ``question_id``.
        """
        return self.nouls[question_id]

    @property
    def total_tokens(self) -> int:
        """Input plus output tokens."""
        return self.input_tokens + self.output_tokens
```

`nouls` holds only probabilities, because those are all this experiment uses. If a later experiment needs `Choice` or `Score` answers, it can add `choices` and `scores` fields here.

### `experiments/zero_shot_jev_inference_2026_10_01/shared/constants.py`

```python
"""Constants for zero-shot Jev keep/remove inference on Study 2."""

from experiments.zero_shot_llm_inference_2026_09_30.shared.schemas import ModelDefinition
from shared.models.jev.constants import JEV_MODEL_ID

EXPERIMENT_NAME = "zero_shot_jev_inference_2026_10_01"
S3_BUCKET = "mirrorview-experimental-artifacts"
S3_PREFIX = f"experiments/{EXPERIMENT_NAME}/"
JEV_MODEL = ModelDefinition(
    display_name="Jev 1.13.0",
    folder_name="jev_1_13_0",
    model_id=JEV_MODEL_ID,
)
REMOVE_QUESTION_ID = "is_remove"
STATE_POST_1_KEY = "post_1"
STATE_POST_2_KEY = "post_2"
REMOVE_THRESHOLD = 0.5
```

## Jev code

### `shared/models/jev/client.py`

```python
"""TypeSafe API key lookup and ``TypeSafeClassifier`` construction."""

from __future__ import annotations

import json
import os

import boto3
from langchain_typesafe import TypeSafeClassifier

from shared.data.dataloader import _use_lab_credentials_when_unset
from shared.models.jev.constants import (
    JEV_MODEL_ID,
    JEV_REQUEST_TIMEOUT_SECONDS,
    JEV_SECRET_ID,
    JEV_SECRETS_REGION,
)

_SECRET_KEYS = ("api_key", "TYPESAFE_API_KEY", "key")


def get_jev_api_key() -> str:
    """Return the TypeSafe API key from ``TYPESAFE_API_KEY`` or Secrets Manager.

    Raises
    ------
    ValueError
        When the secret is empty or has none of the expected JSON keys.
    """
    from_env = os.environ.get("TYPESAFE_API_KEY", "").strip()
    if from_env:
        return from_env
    _use_lab_credentials_when_unset()
    client = boto3.client("secretsmanager", region_name=JEV_SECRETS_REGION)
    raw = (client.get_secret_value(SecretId=JEV_SECRET_ID).get("SecretString") or "").strip()
    if not raw:
        raise ValueError(f"secret {JEV_SECRET_ID} has no SecretString")
    if not raw.startswith("{"):
        return raw
    payload = json.loads(raw)
    for key in _SECRET_KEYS:
        value = str(payload.get(key) or "").strip()
        if value:
            return value
    raise ValueError(f"secret {JEV_SECRET_ID} has none of {_SECRET_KEYS}")


def build_jev_classifier(
    model_id: str = JEV_MODEL_ID,
    api_key: str | None = None,
    timeout: float = JEV_REQUEST_TIMEOUT_SECONDS,
) -> TypeSafeClassifier:
    """Build a classifier pinned to ``model_id``. Looks up the key when omitted."""
    return TypeSafeClassifier(
        model=model_id,
        api_key=api_key if api_key is not None else get_jev_api_key(),
        timeout=timeout,
    )
```

### `shared/models/jev/scorer.py`

```python
"""Call Jev once per request, with rate limiting and transient-error retries."""

from __future__ import annotations

import time
from collections.abc import Callable

from langchain_typesafe import (
    ClassifierRequest,
    ClassifierResponse,
    Noul,
    TypeSafeClassifier,
)
from langchain_typesafe.client import (
    TypeSafeAPIConnectionError,
    TypeSafeAPITimeoutError,
    TypeSafeInternalServerError,
    TypeSafeRateLimitError,
)

from shared.models.jev.client import build_jev_classifier
from shared.models.jev.constants import (
    JEV_MAX_REQUESTS_PER_MINUTE,
    JEV_MODEL_ID,
    JEV_RETRY_BACKOFF_SECONDS,
)
from shared.models.jev.rate_limit import RequestStartLimiter
from shared.models.jev.schemas import JevResult

_RETRYABLE_ERRORS = (
    TypeSafeRateLimitError,
    TypeSafeInternalServerError,
    TypeSafeAPIConnectionError,
    TypeSafeAPITimeoutError,
)


def parse_response(
    request: ClassifierRequest,
    response: ClassifierResponse,
    expected_model: str,
    latency_ms: float,
    attempts: int,
) -> JevResult:
    """Convert one classifier response into a ``JevResult``.

    Raises
    ------
    KeyError
        When a requested Noul question has no answer.
    ValueError
        When Jev answered with a model other than ``expected_model``.
    """
    if response.model != expected_model:
        raise ValueError(f"expected model {expected_model}, got {response.model}")
    noul_ids = [
        question_id
        for question_id, question in request["questions"].items()
        if isinstance(question, Noul)
    ]
    answers = response.nouls
    missing = [question_id for question_id in noul_ids if question_id not in answers]
    if missing:
        raise KeyError(f"missing Noul answers for {missing}")
    return JevResult(
        model=response.model,
        request_id=response.request_id,
        nouls={question_id: answers[question_id].noul for question_id in noul_ids},
        input_tokens=response.usage.input_tokens or 0,
        output_tokens=response.usage.output_tokens or 0,
        latency_ms=latency_ms,
        attempts=attempts,
    )


class JevScorer:
    """Send one ``ClassifierRequest`` at a time. Safe to share across threads."""

    def __init__(
        self,
        classifier: TypeSafeClassifier,
        limiter: RequestStartLimiter,
        clock: Callable[[], float],
        sleep_fn: Callable[[float], None],
        backoff_seconds: tuple[float, ...] = JEV_RETRY_BACKOFF_SECONDS,
    ) -> None:
        self._classifier = classifier
        self._limiter = limiter
        self._clock = clock
        self._sleep_fn = sleep_fn
        self._backoff_seconds = backoff_seconds

    def score(self, request: ClassifierRequest) -> JevResult:
        """Call Jev once, retrying only transient errors.

        Raises
        ------
        TypeSafeAPIError
            Non-retryable API errors are raised at once. Retryable errors are
            raised after the last backoff.
        KeyError, ValueError
            From ``parse_response``. Never retried.
        """
        max_attempts = 1 + len(self._backoff_seconds)
        for attempt in range(1, max_attempts + 1):
            self._limiter.wait()
            started = self._clock()
            try:
                response = self._classifier.invoke(request)
            except _RETRYABLE_ERRORS as error:
                if attempt == max_attempts:
                    raise
                self._sleep_fn(self._retry_delay(error, attempt))
                continue
            latency_ms = (self._clock() - started) * 1000.0
            return parse_response(
                request, response, self._classifier.model, latency_ms, attempt
            )
        raise AssertionError("unreachable")

    def _retry_delay(self, error: Exception, attempt: int) -> float:
        """Use the fixed backoff, or the server's retry-after when it is longer."""
        delay = self._backoff_seconds[attempt - 1]
        retry_after_ms = getattr(error, "retry_after_ms", None)
        if retry_after_ms is not None:
            delay = max(delay, retry_after_ms / 1000.0)
        return delay


def build_jev_scorer(model_id: str = JEV_MODEL_ID) -> JevScorer:
    """Build the real scorer: pinned classifier, shared limiter, real clock."""
    limiter = RequestStartLimiter(JEV_MAX_REQUESTS_PER_MINUTE, time.monotonic, time.sleep)
    return JevScorer(build_jev_classifier(model_id), limiter, time.perf_counter, time.sleep)
```

`rate_limit.py` is a copy of `RequestStartLimiter` from `experiments/study_2_llm_based_feature_extraction_2026_09_29/shared/jev.py`. `__init__.py` re-exports `JEV_MODEL_ID`, `JevResult`, `JevScorer`, `RequestStartLimiter`, `build_jev_classifier`, `build_jev_scorer`, `get_jev_api_key`, and `parse_response`.

### Request shape (experiment `shared/jev.py`)

A Jev request has two parts: `state` holds the data, and a `Noul` holds a yes/no question and returns P(yes). The 326 prompt is mapped onto that shape like this:

- **`state`**: `{"post_1": record.post_1_text, "post_2": record.post_2_text}`. Post order is the prepared order and is never swapped.
- **`Noul.instructions`**: the 326 prompt, unchanged up to `Post 1: {post_1_text}`. The block from `Post 1:` through `Allow Or Remove?` is replaced with a pointer to the state keys and the question "Should both posts in the pair be removed from the platform?". If the prompt does not end with exactly that block, `build_remove_instructions` raises an error, so a change to 326's prompt cannot slip through unnoticed.
- **`Noul.criteria`**: `true` = Remove and `false` = Allow, so the answer `noul` is `p_remove`.

Wire payload for one pair, as captured from the prototype:

```json
{
  "state": {"post_1": "Left post.", "post_2": "Right post."},
  "model": "jev-1.13.0",
  "questions": {
    "is_remove": {
      "type": "noul",
      "instructions": "<REMOVE_INSTRUCTIONS>",
      "criteria": {
        "true": "Remove: both posts in the pair should be removed from the platform.",
        "false": "Allow: both posts in the pair should be allowed on the platform."
      }
    }
  }
}
```

How `REMOVE_INSTRUCTIONS` ends:

```text
... Your goal is to evaluate the messages, using your own judgment.

Post 1 is in `post_1` and Post 2 is in `post_2`.

Should both posts in the pair be removed from the platform?
```

### `experiments/zero_shot_jev_inference_2026_10_01/shared/jev.py`

```python
"""Keep/remove request and result mapping on top of ``shared.models.jev``."""

from __future__ import annotations

from langchain_typesafe import ClassifierRequest, Noul, NoulCriteria

from experiments.zero_shot_jev_inference_2026_10_01.shared.constants import (
    JEV_MODEL,
    REMOVE_QUESTION_ID,
    REMOVE_THRESHOLD,
    STATE_POST_1_KEY,
    STATE_POST_2_KEY,
)
from experiments.zero_shot_llm_inference_2026_09_30.shared.prompts import (
    BASELINE_ZERO_SHOT_KEEP_REMOVE_PROMPT,
)
from experiments.zero_shot_llm_inference_2026_09_30.shared.schemas import (
    PredictionRecord,
    RemovePrediction,
    Study2InputRecord,
    TokenUsage,
)
from shared.models.jev import JevResult

PAIR_BLOCK = "Post 1: {post_1_text}\n\nPost 2: {post_2_text}\n\nAllow Or Remove?"
REMOVE_QUESTION = (
    f"Post 1 is in `{STATE_POST_1_KEY}` and Post 2 is in `{STATE_POST_2_KEY}`.\n\n"
    "Should both posts in the pair be removed from the platform?"
)
REMOVE_CRITERIA = NoulCriteria(
    true="Remove: both posts in the pair should be removed from the platform.",
    false="Allow: both posts in the pair should be allowed on the platform.",
)


def build_remove_instructions(prompt: str) -> str:
    """Swap the baseline prompt's pair block for a yes/no remove question.

    Raises
    ------
    ValueError
        When the prompt does not end with exactly one pair block.
    """
    preamble, separator, tail = prompt.partition(PAIR_BLOCK)
    if not separator or tail:
        raise ValueError("baseline prompt must end with the Post 1/Post 2 pair block")
    return preamble + REMOVE_QUESTION


REMOVE_INSTRUCTIONS = build_remove_instructions(BASELINE_ZERO_SHOT_KEEP_REMOVE_PROMPT)


def build_remove_request(record: Study2InputRecord) -> ClassifierRequest:
    """Build the classifier input for one prepared pair, posts in input order."""
    return {
        "state": {
            STATE_POST_1_KEY: record.post_1_text,
            STATE_POST_2_KEY: record.post_2_text,
        },
        "questions": {
            REMOVE_QUESTION_ID: Noul(instructions=REMOVE_INSTRUCTIONS, criteria=REMOVE_CRITERIA),
        },
    }


def to_prediction_record(
    run_id: str,
    record: Study2InputRecord,
    result: JevResult,
) -> PredictionRecord:
    """Map one ``JevResult`` onto the issue 326 prediction row.

    ``is_remove`` is derived from ``p_remove`` at 0.5, so the 326 threshold
    validator always passes.
    """
    p_remove = result.noul(REMOVE_QUESTION_ID)
    prediction = RemovePrediction(is_remove=p_remove >= REMOVE_THRESHOLD, p_remove=p_remove)
    usage = TokenUsage(
        input_tokens=result.input_tokens,
        output_tokens=result.output_tokens,
        total_tokens=result.total_tokens,
    )
    return PredictionRecord(
        run_id=run_id,
        model_folder=JEV_MODEL.folder_name,
        model_id=JEV_MODEL.model_id,
        post_id=record.post_id,
        is_remove=prediction.is_remove,
        p_remove=prediction.p_remove,
        usage=usage,
    )
```

Step 2 calls it like this, one pair at a time, with one `JevScorer` shared across its worker threads:

```python
scorer = build_jev_scorer()
row = to_prediction_record(run_id, record, scorer.score(build_remove_request(record)))
```

The `PredictionRecord` field names above come from the 326 Step 2 plan. Match them to 326's final `schemas.py`.

### Expected results

I ran the prototype against `httpx2.MockTransport`, injected through `TypeSafeClassifier(client=...)`. No live Jev calls were made.

| Scenario | Result |
| --- | --- |
| Jev returns `noul=0.83`, usage 612 in / 1 out | `JevResult(nouls={"is_remove": 0.83}, attempts=1)` → `PredictionRecord(model_folder="jev_1_13_0", is_remove=True, p_remove=0.83, usage=(612, 1, 613))` |
| 429 with `retry-after-ms: 3000`, then 503, then `noul=0.2` | 3 HTTP calls, sleeps `[3.0, 2.0]`, `attempts=3`, `is_remove=False` |
| 429 four times | 4 calls, sleeps `[1.0, 2.0, 4.0]`, raises `TypeSafeRateLimitError` (step 2 writes a `FailureRecord`) |
| 400 Bad Request | 1 call, no sleep, raises `TypeSafeBadRequestError` |
| `noul=0.5`, no usage reported | `is_remove=True` (ties go to remove, as in 326), usage `(0, 0, 0)` |
| Response `model="jev-1.14.0"` | `ValueError: expected model jev-1.13.0, got jev-1.14.0` |
| No `is_remove` answer | `KeyError: "missing Noul answers for ['is_remove']"` |

What to expect in a real run:

- Each of the 13,992 pairs gets one `p_remove` in [0, 1]. `is_remove` is computed from it, and Jev itself never returns a label.
- The output token count will probably be 0 or `None`. Study 2 priced Jev output at $0.
- The instructions are 1,501 characters (249 words), roughly 350 tokens. With the two posts that makes about 600 tokens per request: around 8.4M input tokens, or about $0.35 at $0.042 per 1M. Step 2's smoke run should replace this with measured numbers.
- The rate limit of 1,000 requests per minute means a full run takes at least 14 minutes.

## Decisions to confirm

1. **Add `langchain-typesafe==0.0.1a3` to `pyproject.toml`.** Root `shared/models/jev/` code is imported across experiments, so pulling the package in per command with `uv run --with` would be fragile. Pin the exact version, because it is an alpha release.
2. **Credentials in `client.py`.** It reuses the private `shared.data.dataloader._use_lab_credentials_when_unset` instead of adding a fifth copy of the same function. The alternative is to make that function public in the same PR.
3. **Pin `jev-1.13.0`** (the Study 2 version) instead of the classifier default `jev-latest`. `parse_response` raises an error on any other `response.model`. A smoke call should confirm that Jev echoes `jev-1.13.0`.
4. **Store 326's `PredictionRecord` unchanged.** This drops `request_id`, `latency_ms`, and `attempts`, but lets 326's analysis read the Jev folder as is.
5. **Instructions = 326 prompt with only the pair block replaced**, with posts in `state` and Remove = `true`. The other option is to send the fully rendered prompt as the instructions. That is closer to the Bedrock models, but it makes Jev answer the question "Allow Or Remove?" with a yes or no, which is ambiguous.
6. **Map missing Jev usage to `0`**, as Study 2 did, rather than failing the record.
