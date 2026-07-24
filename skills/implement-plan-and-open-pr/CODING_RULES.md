# Rules for software development

## Code Quality & Architecture

- Single Responsibility Principle: Each class/function should have one clear purpose
- Dependency Injection: Use constructor injection for testability and loose coupling
- Interface Segregation: Define narrow, focused interfaces rather than monolithic ones
- Composition over Inheritance: Favor composition to avoid deep inheritance hierarchies
- Keep changes narrowly scoped: When updating an existing file, make only minimal changes, emphasizing changes that are directly related to your purpose for refactoring that file.
- Abstraction levels should be consistent within a function: A function should either coordinate high-level operations or implement low-level details, but should not mix both. Extract low-level parsing, serialization, validation, or database operations into focused helpers.

Bad:

```python
def generate_report(report_id: str) -> Report:
  connection = psycopg.connect(DATABASE_URL)
  cursor = connection.cursor()
  cursor.execute("SELECT payload FROM reports WHERE id = %s", (report_id,))
  raw_payload = cursor.fetchone()[0]
  parsed_payload = json.loads(raw_payload)
  return render_report(parsed_payload)
```

Good:

```python
def generate_report(report_id: str) -> Report:
  report_data = load_report_data(report_id)
  return render_report(report_data)
```

## Database & Data Management

- Connection Pooling: Always use connection pools for database access
- Transaction Boundaries: Keep transactions short and well-defined
- Query Optimization: Index frequently queried columns, avoid N+1 queries
- Data Validation: Validate at API boundaries, not just database constraints
- Migration Safety: All schema changes must be backward compatible
- Prepared Statements: Use parameterized queries to prevent SQL injection
- Use Alembic for Python DB migrations.

## Code Style & Readability

- Meaningful Names: Variables and functions should be self-documenting

| Original name              | Why it's bad                                                                               | Suggested replacement          | Why it's better                                                                             |
| -------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------ | ------------------------------------------------------------------------------------------- |
| `data` (variable)          | Too generic; it doesn't communicate what the data represents.                              | `customer_records`             | Describes both the contents and the domain, making the code self-documenting.               |
| `temp` (variable)          | Indicates a temporary value but not its purpose or meaning.                                | `normalized_text`              | Explains what transformation the value represents.                                          |
| `x` (variable)             | Single-letter names are hard to follow outside of short mathematical contexts.             | `retry_count`                  | Clearly communicates the variable's role.                                                   |
| `stuff` (variable)         | Vague catch-all name that forces readers to inspect the implementation.                    | `pending_jobs`                 | Makes the contents and intent immediately obvious.                                          |
| `flag` (variable)          | Doesn't indicate what condition the boolean is tracking.                                   | `is_authenticated`             | Boolean naming makes the condition explicit and naturally readable.                         |
| `do_it()` (function)       | Gives no clue about what action the function performs.                                     | `process_uploaded_files()`     | Clearly describes the operation and the object being acted upon.                            |
| `handle_data()` (function) | "Handle" is an overloaded verb that could mean almost anything.                            | `validate_user_profile()`      | Uses a specific verb and object to describe the function's responsibility.                  |
| `get_info()` (function)    | "Info" is ambiguous and doesn't reveal what is being retrieved.                            | `fetch_weather_forecast()`     | Identifies both the source action and the returned data.                                    |
| `process()` (function)     | Generic verbs hide the actual behavior and often indicate too many responsibilities.       | `generate_monthly_report()`    | Specifies the concrete outcome of the function.                                             |
| `run()` (function)         | Meaning depends entirely on surrounding context and becomes confusing in larger codebases. | `train_recommendation_model()` | States exactly what operation is being executed, improving readability and discoverability. |

- Function Length: Keep functions under 20 lines, methods under 50

- Cyclomatic Complexity: Maximum complexity of 10 per function. For Python, enforce with `radon`, and for other libraries, enforce with the appropriate package.

- No magic numbers or literal values: Use named constants for all literal values

- Avoid excessive if/else usage and use a registry pattern when there are >= 3 options.

Bad:

```python
if resolved_settings.provider is LlmProvider.BEDROCK: 
  return get_chat_bedrock_model(resolved_settings)
elif resolved_settings.provider is LlmProvider.GEMINI:
  return get_chat_gemini_model(resolved_settings)
else:
  return get_chat_openai_model(resolved_settings)
```

Good:

```python
llm_providers = {
    LlmProvider.BEDROCK: get_chat_bedrock_model,
    LlmProvider.GEMINI: get_chat_gemini_model,
    LlmProvider.OPENAI: get_chat_openai_model,
}
provider = llm_providers.get(resolved_settings.provider, get_chat_openai_model)
return provider(resolved_settings)
```

- If a function requires >= 3 verification steps, abstract this into a verification function.

Bad:

```python
def load_llm_config(*, config_path: Path) -> LlmConfig:
    """Load LLM configs from YAML.

    Parameters
    ----------
    config_path: Path to the YAML file.

    Returns
    -------
    LlmConfig
        Frozen config for the active provider and model.

    Raises
    ------
    FileNotFoundError
        When the YAML file does not exist.
    ValueError
        When required keys are missing or values are invalid.
    """
    if not config_path.is_file():
        raise FileNotFoundError(config_path.resolve())

    with config_path.open(encoding="utf-8") as handle:
        raw = yaml.safe_load(handle)

    if not isinstance(raw, dict):
        raise ValueError(f"{config_path}: root must be a mapping")

    provider = _require_str(raw, "provider").lower()
    bedrock_model_id = _require_str(raw, "model_id")
    openai_model_id = _require_str(raw, "openai_model_id")
    temperature = _require_float(raw, "temperature")
```

Good:

```python
def _return_validated_llm_config_values(yaml_config: dict) -> dict:
    if not isinstance(raw, dict):
        raise ValueError(f"{path}: root must be a mapping")

    provider = _require_str(raw, "provider").lower()
    bedrock_model_id = _require_str(raw, "model_id")
    openai_model_id = _require_str(raw, "openai_model_id")
    temperature = _require_float(raw, "temperature")
    return {
      "provider": provider,
      "bedrock_model_id": bedrock_model_id,
      "openai_model_id": openai_model_id,
      "temperature": temperature
    }

def load_llm_config(*, config_path: Path) -> LlmConfig:
    """Load LLM configs from YAML.

    Parameters
    ----------
    config_path: Path to the YAML file.

    Returns
    -------
    LlmConfig
        Frozen config for the active provider and model.

    Raises
    ------
    FileNotFoundError
        When the YAML file does not exist.
    ValueError
        When required keys are missing or values are invalid.
    """
    if not config_path.is_file():
        raise FileNotFoundError(config_path.resolve())

    with config_path.open(encoding="utf-8") as handle:
        raw = yaml.safe_load(handle)

    config_values: dict = _return_validated_llm_config_values(raw)
```

- Make state changes explicit: Avoid in-place mutation. Avoid functions that silently mutate arguments or shared module-level state. Prefer returning a new value or making the mtutation clear through the function name and return type.

Bad:

```python
def normalize(records: list[Record]) -> None:
  for record in records:
    record.name = record.name.strip().lower()
```

Good:

```python
def normalize_records(records: list[Record]) -> list[Record]:
  return [
    replace(record, name=record.name.strip().lower())
    for record in records
  ]
```

### Data models

- Prefer explicit data models over unstructured dictionaries. Avoid unstructured dictionaries at all cost. Use `dataclass`, `Pydantic`, or `TypedDict`, when data has a known schema. Reserve `dict[str, Any]` for truly dynamic data (err on the side of assuming it's not truly dynamic).

Bad:

```python
def process_user(user: dict[str, Object]) -> str:
  return str(user["email"])
```

Good:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class User:
  email: str

def get_user_email(user: User) -> str:
  return user.email
```

- Enums Over String/Bool Literals: Use Enum for any fixed, known set of values instead of raw strings or booleans, to get type safety and autocomplete.

Bad:

```python
def get_chat_model(provider: str) -> ChatModel:
    if provider == "bedrock":
        ...
```

Good:

```python
class LlmProvider(str, Enum):
    BEDROCK = "bedrock"
    GEMINI = "gemini"
    OPENAI = "openai"

def get_chat_model(provider: LlmProvider) -> ChatModel:
    if provider is LlmProvider.BEDROCK:
        ...
```

- Named Tuples/Enums Over Positional Tuple Returns: Avoid returning bare tuples for multi-value returns; use a NamedTuple, dataclass, or small return type so callers don't have to guess positional order.

Bad:

```python
def get_model_settings() -> tuple[str, float, bool]:
    return "bedrock", 0.7, True

provider, temp, tracing = get_model_settings()  # order-dependent, error-prone
```

Good:

```python
class ModelSettings(NamedTuple):
    provider: str
    temperature: float
    enable_tracing: bool

def get_model_settings() -> ModelSettings:
    return ModelSettings(provider="bedrock", temperature=0.7, enable_tracing=True)

settings = get_model_settings()
print(settings.temperature)  # self-documenting access
```

- Use domain-specific types when doing so would add readability without cluttering the interface.

Bad:

```python
def transfer_funds(
  source_id: str,
  destination_id: str,
  amount: float
) -> None:
  ...
```

Good:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class AccountId:
  value: str


def transfer_funds(
  source_account_id: AccountId,
  destination_account_id: AccountId,
  amount: float
) -> None:
  ...
```

However, this can be taken to an extreme. Avoid every single permutation of domain-specific type and only add when doing so would be tasteful for the context of work and improve future readability.

For example, in the above example, we could've done:

Bad (too much domain-specific typing)

```python
... # everything from before

@dataclass(frozen=True)
class Money:
  amount: Decimal


def transfer_funds(
  source_account_id: AccountId,
  destination_account_id: AccountId,
  amount: Money
) -> None:
  ...
```

This would've been unnecessary. There is only 1 `amount` field, and a reader can easily infer that the float parameter is because it is a financial amount. A more useful custom type could have, for example, added validation (e.g., making sure it is >0):

```python
... # everything from before

from pydantic import BaseModel, validator
from decimal import Decimal, ROUND_DOWN

class Money(BaseModel):
    amount: Decimal

    @validator("amount")
    def validate_amount(cls, v: Decimal) -> Decimal:
        if v <= 0:
            raise ValueError("Amount must be greater than 0")
        quantized = v.quantize(Decimal("0.01"), rounding=ROUND_DOWN)
        # Check for exactly 2 decimal places
        if v != quantized:
            raise ValueError("Amount must have exactly 2 decimal places")
        return quantized

def transfer_funds(
  source_account_id: AccountId,
  destination_account_id: AccountId,
  amount: Money
) -> None:
  ...
```

### Arguments, parameters, and return signatures

- Early Returns: Reduce nesting with guard clauses and early returns

- Type Hints: All public APIs must have complete type annotations

- Avoid excessive nullability: parameters should be strictly required by default unless it would break existing functionality. By default, make parameters required and not nullable. Avoid default behavior within a function.

Bad:

```python
def foo(total_values: int | None):
  n = total_values or NUMBER_OF_VALUES
```

Good:

```python
def foo(total_values: int):
  n = total_values
```

- Avoid "God" functions that take a variety of arguments. Parameters for a function should be explicitly required for the unit of work that the function does. If you must have a container, err on the side of creating container classes for the arguments.

Bad:

```python
def main(
  user_ids: list[str],
  input_path: str,
  output_path: str,
  prompt: str,
  llm_model_name: str,
  temperature: float,
  enable_tracing: bool,
  tracing_provider: str,
  save_to_db: bool,
  app_db_backend: AppDbBackend,
  memory_db_backend: MemoryDbBackend,
  checkpointer_backend: CheckpointerBackend,
)
```

Good:

```python
class LLMConfig:
  llm_model_name: str
  temperature: float

class TelemetrySettings:
  enable_tracing: bool,
  tracing_provider: str

class DbSettings:
  app_db_backend: AppDbBackend,
  memory_db_backend: MemoryDbBackend,
  checkpointer_backend: CheckpointerBackend,
  input_path: str,
  output_path: str,
  save_to_db: bool

def main(
  user_ids: list[str],
  llm_config: LLMConfig,
  telemetry_settings: TelemetrySettings,
  db_settings: DbSettings
)
```

- Default constants should only be used by the highest-level caller for a function.

Bad:

```python
NUMBER_OF_VALUES = 1

def foo(total_values: int | None):
  n = total_values or NUMBER_OF_VALUES

def main():
  foo()
```

Good:

```python
NUMBER_OF_VALUES = 1

def foo(total_values: int):
  n = total_values

def main():
  foo(NUMBER_OF_VALUES)
```

- Avoid default arguments altogether where possible. Prefer callers to explicitly pass a global constant rather than having a function signature include a default argument.

- Avoid excessive use of `*` in parameter signatures. This is noisy and doesn't help downstream callers.

Bad:

```python
def _resolve_active_model_id(
    *,
    provider: str,
    bedrock_model_id: str,
    openai_model_id: str,
) -> str:
```

Good:

```python
def _resolve_active_model_id(
    provider: str,
    bedrock_model_id: str,
    openai_model_id: str,
) -> str:
```

## Docstrings

- Add numpy-style docstrings.
- In the file-level docstring, always add the relevant `uv run python ...` command.

Bad:

```python
def load_llm_config(*, config_path: Path | None = None) -> LlmConfig:
    """Load LLM defaults from YAML and apply optional env overrides.
    
    What happens is that it takes the parameters in config_path, does its work,
    and then returns the LLMConfig.
    
    But it can raise FileNotFoundError if broken.
    """
```

Good:

```python
def load_llm_config(*, config_path: Path | None = None) -> LlmConfig:
    """Load LLM defaults from YAML and apply optional env overrides.

    Parameters
    ----------
    config_path
        Optional path to the YAML file; defaults to ``llm.yaml`` beside this module.

    Returns
    -------
    LlmConfig
        Frozen config for the active provider and model.

    Raises
    ------
    FileNotFoundError
        When the YAML file does not exist.
    ValueError
        When required keys are missing or values are invalid.
    """
```

## Python environment

- Unless explicitly stated by the user, assume that `uv` (with `pyproject.toml`) is the default package manager.
- Require that all code can be run from the root of the repo, via a `uv run python ...` pattern.

## Performance & Scalability

- Lazy Loading: Load data only when needed
- Caching Strategy: Cache at appropriate layers with TTL policies
- Async Operations: Use async/await for I/O bound operations
- Resource Management: Always use context managers for resource cleanup
- Memory Efficiency: Prefer generators over lists for large datasets
- Database Pagination: Never load unbounded result sets

## Error Handling & Monitoring

- Fail Fast: Validate inputs early and throw meaningful exceptions
- Structured Logging: Use structured logs with correlation IDs
- Circuit Breakers: Implement circuit breakers for external service calls
- Graceful Degradation: System should degrade gracefully under load
- Health Checks: Implement comprehensive health check endpoints
- Metrics Collection: Instrument critical code paths with metrics
