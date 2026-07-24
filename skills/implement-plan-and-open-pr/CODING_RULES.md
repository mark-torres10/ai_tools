---
id: rules.coding_rules
title: Core Development Rules
description: Cross-cutting software engineering standards for architecture, data, testing, style, performance, and reliability.
when_to_use:
  - Implementing or refactoring application code.
  - Reviewing code quality and maintainability.
  - Defining baseline engineering guardrails for new work.
when_not_to_use:
  - Running or troubleshooting local servers (use server management rules).
  - Generating project tickets or PM artifacts.
scope:
  - coding
  - architecture
  - reliability
priority: 80
applies_to:
  task_types:
    - implementation
    - refactor
    - bugfix
    - code_review
  file_globs:
    - "**/*.{py,ts,tsx,js,jsx,go,java,rs}"
dependencies:
  - rules.coding_repo_conventions
  - rules.unit_testing_standards
conflicts_with: []
tools_preferred:
  - ReadFile
  - ApplyPatch
  - ReadLints
owner: ai_tools
last_updated: 2026-02-17
---

# Rules for development

## Code Quality & Architecture

- **Single Responsibility Principle**: Each class/function should have one clear purpose
- **Dependency Injection**: Use constructor injection for testability and loose coupling
- **Interface Segregation**: Define narrow, focused interfaces rather than monolithic ones
- **Composition over Inheritance**: Favor composition to avoid deep inheritance hierarchies
- **Keep changes narrowly scoped**: When updating an existing file, make only minimal changes, emphasizing changes that are directly related to your purpose for refactoring that file.

## Database & Data Management

- **Connection Pooling**: Always use connection pools for database access
- **Transaction Boundaries**: Keep transactions short and well-defined
- **Query Optimization**: Index frequently queried columns, avoid N+1 queries
- **Data Validation**: Validate at API boundaries, not just database constraints
- **Migration Safety**: All schema changes must be backward compatible
- **Prepared Statements**: Use parameterized queries to prevent SQL injection

## Testing Standards

- **Test Coverage**: Maintain >90% line coverage, >80% branch coverage
- **Test Isolation**: Each test must be independent and idempotent
- **Test Naming**: Use descriptive names that explain the scenario being tested
- **Mock External Dependencies**: Never hit real databases/APIs in unit tests
- **Integration Tests**: Test critical paths end-to-end with real components
- **Property-Based Testing**: Use for complex business logic validation
- **Testing against expected results**: Write the expected output and save it to a "expected_result" variable. Then have your assertions, where relevant, test directly against the "expected_result" to see if the content is correct. This helps with improving readability of tests.
- **Make sure all tests can run in CI**: This means no browser requirements, no GUI access, and the like. For any UI tests, if necessary, it must be headless.

## Code Style & Readability

- **Meaningful Names**: Variables and functions should be self-documenting
- **Function Length**: Keep functions under 20 lines, methods under 50

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

## Performance & Scalability

- **Lazy Loading**: Load data only when needed
- **Caching Strategy**: Cache at appropriate layers with TTL policies
- **Async Operations**: Use async/await for I/O bound operations
- **Resource Management**: Always use context managers for resource cleanup
- **Memory Efficiency**: Prefer generators over lists for large datasets
- **Database Pagination**: Never load unbounded result sets

## Error Handling & Monitoring

- **Fail Fast**: Validate inputs early and throw meaningful exceptions
- **Structured Logging**: Use structured logs with correlation IDs
- **Circuit Breakers**: Implement circuit breakers for external service calls
- **Graceful Degradation**: System should degrade gracefully under load
- **Health Checks**: Implement comprehensive health check endpoints
- **Metrics Collection**: Instrument critical code paths with metrics
