# Function Docstrings

Explain what the function accomplishes and any non-obvious contract. Use numpy-style sections when parameters, returns, or raises need documenting.

## Criteria

A good function docstring:

- Opens with a one-line summary of the **outcome**
- Expands only for surprising behavior, assumptions, or side effects
- Documents important parameters—not every obvious one
- States return value when it is not obvious from the name/type
- Documents raised exceptions that callers must handle
- States preconditions/postconditions when they matter
- Explains **behavior**, never the implementation loop or algorithm steps

It should answer:

1. What does calling this do?
2. What must the caller already guarantee?
3. What can go wrong or change outside the return value?

## Section checklist (numpy-style)

Include a section only when it adds information not clear from the signature:

| Section | Include when |
|---------|----------------|
| Summary + optional body | Always |
| `Parameters` | Non-obvious meaning, units, ordering, or constraints |
| `Returns` | Shape, units, or semantics not obvious from the type |
| `Raises` | Callers must catch or prevent the failure |
| `Notes` / `Warnings` | Surprising cache, mutation, or concurrency behavior |

## Good vs bad

### Behavior vs implementation

Bad — narrates the code:

```python
"""
Loops through events and compares timestamps.
"""
```

Good — names the outcome:

```python
"""
Groups events into contiguous sessions separated by more than
30 minutes of inactivity.
"""
```

### Surprising behavior and assumptions

Good — documents cache refresh:

```python
"""
Returns cached results when available.

The cache is refreshed automatically if it is older than one hour.
"""
```

Good — documents a precondition in `Parameters`:

```python
"""
Parameters
----------
users : sequence
    Must already be sorted by signup date.
"""
```

Good — documents a side effect (prefer pure functions when possible):

```python
"""
Also updates the local cache.
"""
```

Good — documents exceptions:

```python
"""
Raises
------
ValueError
    If duplicate IDs are encountered.
"""
```

### Full example

Bad — restates names; empty of contract:

```python
def normalize(df):
    """
    Normalize dataframe.

    Parameters
    ----------
    df : dataframe
        dataframe

    Returns
    -------
    dataframe
        normalized dataframe
    """
```

Good — range, column policy, missing-value policy, failure mode:

```python
def normalize(df):
    """
    Normalize numeric columns to the range [0, 1].

    Non-numeric columns are left unchanged. Missing values are
    preserved.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    Returns
    -------
    pandas.DataFrame
        A new dataframe with normalized numeric columns.

    Raises
    ------
    ValueError
        If a numeric column contains infinite values.
    """
```

## Anti-patterns

- "Does X" that only repeats the function name
- Listing every parameter when types already say enough
- Describing internal helpers, loop structure, or temporary variables
- Promising behavior the tests/code do not enforce
