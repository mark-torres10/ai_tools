---
id: rules.unit_testing_standards
title: Unit Testing Standards
description: Testing requirements and execution standards for writing, structuring, and validating automated tests.
when_to_use:
  - Writing or updating tests for changed code.
  - Reviewing test quality and coverage expectations.
  - Enforcing pytest and mocking patterns in Python projects.
when_not_to_use:
  - Non-testing-only operational tasks (for example, server startup).
  - Product ticket-writing guidance.
scope:
  - testing
  - quality_assurance
priority: 85
applies_to:
  task_types:
    - testing
    - test_refactor
    - bugfix_validation
  file_globs:
    - "**/test_*.py"
    - "**/*_test.py"
    - "**/*.spec.ts"
    - "**/*.test.ts"
dependencies:
  - rules.coding_repo_conventions
conflicts_with: []
tools_preferred:
  - Shell
  - ReadFile
  - ApplyPatch
owner: ai_tools
last_updated: 2026-02-17
---

# Unit Testing Standards

This document outlines the testing standards and best practices for all engineering work. These standards ensure consistent, maintainable, and comprehensive test coverage across the codebase.

## 🎯 Core Testing Principles

### **Test Coverage Requirements**
- **100% test coverage** is required for all new code and modified files
- Tests must be written **after development** (not TDD)
- All public functions, classes, and methods must have corresponding tests
- Edge cases and error conditions must be covered

### **Test Organization**
- **One test class per function** - Each function gets its own test class
- Test class name follows pattern: `Test{FunctionName}`
- Test class docstring clearly identifies the function being tested
- Test methods follow descriptive naming: `test_{what_it_tests}`

### **Test Structure**
- Follow **Arrange-Act-Assert** pattern consistently
- Use `result` for actual outputs and `expected` for expected values
- Test outputs directly rather than just checking field existence
- Prefer testing return values over side effects when possible

## 🐍 Python/pytest Standards

### **Framework & Configuration**
- **Primary testing framework**: pytest
- **Mocking library**: pytest-mock (preferred) or unittest.mock
- **Coverage tool**: pytest-cov
- **Test discovery**: pytest auto-discovery
- **Test execution**: All pytest commands must be run with `uv run pytest` (e.g., `uv run pytest`, `uv run pytest --cov=src`)

### **Test Class Structure**
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

### **Mocking Strategy**
- **Use mocks wherever required** - Err on the side of mocking
- **Mock dependencies first** - Before importing modules that use them
- **Use fixtures** for commonly mocked dependencies
- **Verify mock calls** - Check that functions are called with correct arguments
- **Mock external services** - APIs, databases, file systems, etc.

### **Fixture Best Practices**
```python
@pytest.fixture
def mock_external_service(self):
    """Mock the external service dependency."""
    with patch("module.path.external_service") as mock:
        mock.return_value = "mocked_response"
        yield mock
```

## 📋 Test Method Standards

### **Naming Conventions**
- `test_{behavior_description}` - Clear, descriptive test names
- `test_{edge_case_description}` - For edge cases and error conditions
- `test_{input_type}_{expected_behavior}` - For input validation tests

### **Documentation Requirements**
- **Every test method must have a docstring**
- **Complex tests** require detailed docstrings explaining:
  - What the test verifies
  - Why the expected behavior should occur
  - Any business logic or edge case reasoning
- **Simple tests** can have brief docstrings

### **Assertion Patterns**
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

## 🔄 Parametrized Testing

### **When to Use Parametrize**
- Testing multiple input combinations
- Testing edge cases with different data types
- Testing boundary conditions
- Testing multiple error scenarios

### **Parametrize Structure**
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

## 🧪 Test Data Management

### **Test Data Principles**
- **Use realistic test data** that represents actual usage
- **Minimize hardcoded values** in test methods
- **Use factories or fixtures** for complex test data
- **Clean up test data** after tests complete

### **Mock Data Examples**
```python
@pytest.fixture
def sample_post_data(self):
    """Sample post data for testing."""
    return {
        "uri": "test_post_1",
        "text": "Sample post text for testing",
        "preprocessing_timestamp": "2024-01-01T00:00:00",
        "batch_id": "test_batch_1"
    }
```

## 📊 Coverage Requirements

### **Coverage Metrics**
- **Line coverage**: 100% for all new/modified files
- **Branch coverage**: 95%+ for critical business logic
- **Function coverage**: 100% for all public functions
- **Exception handling**: All error paths must be tested

### **Coverage Exclusions**
- **Generated code** (migrations, auto-generated files)
- **Configuration files** (settings, constants)
- **Main entry points** (if they only call other functions)
- **Simple pass-through functions** (with approval)

## 🚨 Error Handling & Edge Cases

### **Required Test Coverage**
- **Invalid inputs** - Test with None, empty strings, wrong types
- **Boundary conditions** - Test with min/max values, empty lists
- **Error conditions** - Test exception handling and error messages
- **Edge cases** - Test unusual but valid inputs

### **Error Testing Examples**
```python
def test_returns_none_for_empty_list(self):
    """Test returns None for empty list."""
    result = function_name([])
    assert result is None

def test_raises_value_error_for_invalid_input(self):
    """Test that invalid input raises appropriate error."""
    with pytest.raises(ValueError, match="Invalid input"):
        function_name("invalid_input")
```

## 🔍 Mock Verification Standards

### **Call Verification**
- **Verify function calls** with correct arguments
- **Check call counts** (once, never, specific number)
- **Validate call order** when sequence matters
- **Test call parameters** for correctness

### **Mock Verification Examples**
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

## 📝 Test Documentation Standards

### **Docstring Requirements**
- **Test class docstrings**: Identify the function being tested
- **Test method docstrings**: Explain what the test verifies
- **Complex test docstrings**: Include reasoning and business logic
- **Parametrized test docstrings**: Document parameter meanings

### **Documentation Examples**
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

## 🚀 Running Tests

### **Test Execution Commands**
```bash
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=src --cov-report=html

# Run specific test file
uv run pytest tests/test_module.py

# Run specific test class
uv run pytest tests/test_module.py::TestClassName

# Run specific test method
uv run pytest tests/test_module.py::TestClassName::test_method_name
```

### **Coverage Reporting**
- **HTML coverage reports** for detailed analysis
- **Terminal coverage summary** for quick feedback
- **Coverage thresholds** enforced in CI/CD
- **Coverage badges** in README files

## 🔧 Configuration Files

### **pytest.ini**
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    --strict-markers
    --disable-warnings
    --tb=short
```

### **.coveragerc**
```ini
[run]
source = src
omit = 
    */tests/*
    */migrations/*
    */__init__.py

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    if self.debug:
    if settings.DEBUG
    raise AssertionError
    raise NotImplementedError
    if 0:
    if __name__ == .__main__.:
    class .*\bProtocol\):
    @(abc\.)?abstractmethod
```

## 📋 Code Review Checklist

### **Test Quality Checks**
- [ ] 100% test coverage for modified files
- [ ] All test methods have descriptive docstrings
- [ ] Edge cases and error conditions are covered
- [ ] Mocks are used appropriately for external dependencies
- [ ] Test data is realistic and well-structured
- [ ] Assertions test actual values, not just existence
- [ ] Mock calls are verified with correct arguments
- [ ] Parametrized tests are used for multiple scenarios

### **Test Structure Checks**
- [ ] One test class per function
- [ ] Test class name follows naming convention
- [ ] Arrange-Act-Assert pattern is followed
- [ ] Fixtures are used for common setup
- [ ] Test methods have clear, descriptive names
- [ ] Complex tests have detailed documentation

## 🎯 Best Practices Summary

1. **Write tests after development** - Focus on functionality first
2. **Use mocks liberally** - Isolate units under test
3. **Test actual outputs** - Verify return values and side effects
4. **Document test purpose** - Explain what and why you're testing
5. **Cover edge cases** - Test boundaries and error conditions
6. **Verify mock interactions** - Ensure dependencies are called correctly
7. **Use parametrized tests** - Test multiple scenarios efficiently
8. **Maintain 100% coverage** - No uncovered code in production

---

*These standards ensure consistent, maintainable, and comprehensive test coverage across all engineering work. Follow them rigorously to maintain code quality and reliability.*
