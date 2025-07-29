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
- **Activate conda environment**: Activate the conda environment for the repo. For this current repo, the name of the conda env is 'bluesky-research'.

## Code Style & Readability

- **Meaningful Names**: Variables and functions should be self-documenting
- **Function Length**: Keep functions under 20 lines, methods under 50
- **Cyclomatic Complexity**: Maximum complexity of 10 per function
- **No Magic Numbers**: Use named constants for all literal values
- **Early Returns**: Reduce nesting with guard clauses and early returns
- **Type Hints**: All public APIs must have complete type annotations

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

## Debugging

- **Evaluate current behaviors**: Evaluate the current behaviors. Note one by one each observed behavior and if it is intended or not. Make a note of what results are incorrect and what the intended results are. Then, for the incorrect results, make an action plan of how to fix those results and include what the expected results should look like instead.
- **Diagnose the bug and create a plan**: When asked by the user to fix the bug, propose a plan to fix it comprehensively, and propose how to create tests to ensure that the bug is fixed. Return this proposed plan before actually making any changes.
