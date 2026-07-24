# Rules for software development

## Code Quality & Architecture

- Single Responsibility Principle: Each class/function should have one clear purpose
- Dependency Injection: Use constructor injection for testability and loose coupling
- Interface Segregation: Define narrow, focused interfaces rather than monolithic ones
- Composition over Inheritance: Favor composition to avoid deep inheritance hierarchies
- Keep changes narrowly scoped: When updating an existing file, make only minimal changes, emphasizing changes that are directly related to your purpose for refactoring that file.

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

Bad:

...

Good:

...

- Function Length: Keep functions under 20 lines, methods under 50

- Cyclomatic Complexity: Maximum complexity of 10 per function. For Python, enforce with `radon`, and for other libraries, enforce with the appropriate package.

- No magic numbers or literal values: Use named constants for all literal values

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

Avoid excessive use of `*` in parameter signatures. This is noisy and doesn't help downstream callers.

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
