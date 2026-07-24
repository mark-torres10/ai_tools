# Unit Testing Standards

This document outlines the testing standards and best practices for all engineering work. These standards ensure consistent, maintainable, and comprehensive test coverage across the codebase.

## Core Testing Principles

### When NOT to write unit tests

- Configuration changes.
- Setting up access to resources like AWS and Terraform.
- Work in experimental code (typically code added to `experiments/`).

### Test Coverage Requirements

- Public functions, classes, and methods must have corresponding tests
- Edge cases and error conditions must be covered

## Best practices

- Err on the side of shared mock data (and factories) and fixtures.
- Make liberal use of `conftest.py` for shared fixtures.
- Unless the work is truly greenfield, assume that there is already either a fixture or a shared mock data loader (and factories) that could be used, or if not, create one that future callers can use.
- Look for opportunities to use parameterization to increase the number of test cases and to test for edge case inputs.
- Clean up and tear down test setups after each test.

### Test Organization

- One test class per function** - Each function gets its own test class
- Test class name follows pattern: `Test{FunctionName}`
- Test class docstring clearly identifies the function being tested
- Test methods follow descriptive naming: `test_{what_it_tests}`

### Test Structure

- Follow **Arrange-Act-Assert** pattern consistently
- Use `result` for actual outputs and `expected` for expected values
- Test outputs directly rather than just checking field existence
- Prefer testing return values over side effects when possible

## Python/pytest Standards

### Framework & Configuration

- Primary testing framework**: pytest
- Mocking library: pytest-mock (preferred) or unittest.mock
- Coverage tool: pytest-cov
- Test discovery: pytest auto-discovery
- Test execution: All pytest commands must be run with `uv run pytest` (e.g., `uv run pytest`, `uv run pytest --cov=src`)

### Test Class Structure

```python
class TestFunctionName:
    """Tests for function_name function."""

    def test_specific_behavior(self):
        """Test description of what this test verifies."""
        # Arrange
        input_data = "test_input"
        expected = "expected_output"
        
        # Act
        result = function_name(input_data)
        
        # Assert
        assert result == expected
```

### Fixture Best Practices

```python
@pytest.fixture
def mock_external_service(self):
    """Mock the external service dependency."""
    with patch("module.path.external_service") as mock:
        mock.return_value = "mocked_response"
        yield mock
```

## Test Method Standards

### Assertion Patterns

```python
# Direct value comparison (preferred)
assert result == expected

# Mock call verification
mock_function.assert_called_once_with(expected_args)
mock_function.assert_called_once()

# Multiple assertions for complex objects
assert result["field1"] == expected["field1"]
assert result["field2"] == expected["field2"]
assert "required_field" in result
```

## Parametrized Testing

### When to Use Parametrize

- Testing multiple input combinations
- Testing edge cases with different data types
- Testing boundary conditions
- Testing multiple error scenarios

### Parametrize Structure

```python
@pytest.mark.parametrize("input_value,expected", [
    ("valid_input", "expected_output"),
    ("edge_case", "edge_expected"),
    ("error_case", None)
])
def test_function_with_various_inputs(self, input_value, expected):
    """Test function behavior with different input types."""
    result = function_name(input_value)
    assert result == expected
```

### Mock Verification Examples

```python
def test_function_calls_dependencies_correctly(self, mock_dependency):
    """Test that dependencies are called with correct parameters."""
    result = function_name("test_input")
    
    # Verify the dependency was called
    mock_dependency.assert_called_once()
    
    # Verify it was called with correct arguments
    mock_dependency.assert_called_once_with("test_input")
    
    # Verify return value
    assert result == "expected_output"
```

## Test Documentation Standards

### Docstring Requirements

- Test class docstrings: Identify the function being tested
- Test method docstrings: Explain what the test verifies
- Complex test docstrings: Include reasoning and business logic
- Parametrized test docstrings: Document parameter meanings

### Documentation Examples

```python
def test_complex_business_logic(self):
    """Test that business rule X is correctly applied.
    
    This test verifies that:
    1. Input validation occurs before processing
    2. Business rule X is applied to valid inputs
    3. Results are formatted according to specification
    4. Error cases are handled gracefully
    
    Business rule X states that...
    """
    # Test implementation
```

```python
class TestCalculateDiscount:
    """Tests for calculate_discount()."""
```

```python
def test_applies_percentage_to_subtotal(self):
    """Verifies the discount percentage is applied to the subtotal."""
    # Test implementation
```

```python
@pytest.mark.parametrize(
    "subtotal,rate,expected",
    [
        (100.0, 0.10, 90.0),  # 10% off
        (50.0, 0.0, 50.0),  # no discount
        (200.0, 1.0, 0.0),  # 100% off
    ],
)
def test_discount_rates(self, subtotal, rate, expected):
    """Verifies calculate_discount for common rate cases.

    Parameters:
        subtotal: Pre-discount amount
        rate: Discount rate in [0.0, 1.0]
        expected: Amount after discount
    """
    # Test implementation
```
