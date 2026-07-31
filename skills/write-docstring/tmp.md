# What makes a good docstring

## Principels

| Good                                            | Avoid                                             |
| ----------------------------------------------- | ------------------------------------------------- |
| Describe **what** the code does                 | Restating the implementation                      |
| Explain **why** something exists if non-obvious | Describing every line of code                     |
| Mention behavior, side effects, and assumptions | Repeating information obvious from names or types |
| Stay accurate as the code evolves               | Becoming stale documentation                      |
| Begin with a one-line summary                   | Long introductory paragraphs                      |

## Function-level docstrings

numpy-style docstrings

Function docstrings

Function docstrings explain:

- What the function accomplishes
- Any important behavior
- Important parameters (not every obvious one)
- Return value
- Exceptions or side effects
- Preconditions/postconditions if important

Explains behaviors instead of implementation:

Bad:

```python
"""
Loops through events and compares timestamps.
"""
```

Good:

```python
"""
Groups events into contiguous sessions separated by more than
30 minutes of inactivity.
"""
```

Documents surprising behavior.

```python
"""
Returns cached results when available.

The cache is refreshed automatically if it is older than one hour.
"""
```

Explains assumptions:

```python
"""
Args:
    users:
        Must already be sorted by signup date.
"""
```

Documents side effects (though functions should try to avoid having side effects):

```python
"""
Also updates the local cache.
"""
```

Documents exceptions:

```python
Raises:
    ValueError:
        If duplicate IDs are encountered.
```


Bad example:

```python
def normalize(df):
    """
    Normalize dataframe.

    Args:
        df: dataframe

    Returns:
        normalized dataframe
    """
```

Good example:

```python
def normalize(df):
    """
    Normalize numeric columns to the range [0, 1].

    Non-numeric columns are left unchanged. Missing values are
    preserved.

    Args:
        df: Input dataframe.

    Returns:
        A new dataframe with normalized numeric columns.

    Raises:
        ValueError: If a numeric column contains infinite values.
    """
```

## Class-level docstrings

A class docstring should describe

- What the object represents
- Its responsibility
- Its lifecycle/state
- Important invariants
- Major collaborators

Notice it should not simply repeat constructor parameters.

Explains the abstraction:

```python
"""
Represents an authenticated user session.
"""
```

Explains responsibilities:

```python
"""
Coordinates ingestion jobs across multiple workers while ensuring
that each file is processed exactly once.
"""
```

Mentions important invariants:

```python
"""
At most one ingestion job may exist per dataset.
"""
```

Bad example:

```python
class Cache:
    """
    Cache class.

    Stores cache.
    """
```

Better version:

```python
class Cache:
    """
    In-memory LRU cache for expensive query results.

    Automatically evicts the least recently used entries once the
    configured capacity is reached. Thread-safe for concurrent reads
    and writes.
    """
```

## File-level docstrings

A module docstring answers "Why does this file exist?" not "What Python code is inside it?"

Good traits:

- High-level purpose
- Describe scope
- Mention major exported APIs
- Include usage when helpful
- Explain architectural role

Example:

Bad version:

```python
"""On-disk Bluesky Jetstream cursor contract (format_version 1).

Disk is the hot-path source of truth. DynamoDB backups (see
``backup_jetstream_cursor``) are a cold disaster-recovery mirror only.
"""
```

Good version:

```python
"""On-disk Bluesky Jetstream cursor contract"""
```

Docstring skill shouldn't leave implementation details in the docstring. Nor should it make reference to things like format_version 1. No details about versioning or anything that could become stale. Docstrings should keep explanations at the highest level of abstraction, so we know the purpose of the work.

Bad version:

```python
"""Daily DynamoDB disaster-recovery backup for the Bluesky Jetstream disk cursor.

Example / offline-capable entrypoint: reads the on-disk cursor contract, builds a
metadata-rich DynamoDB item, and writes it only after validation. Failed writes
do not delete or mutate a prior good backup (atomic put_item only).

Does not run on the ingestion hot path. Live AWS table provisioning and HPC cron
install are out of scope for the example PR — see the recovery runbook and cron
example under docs/.

Run from the repo root:

    PYTHONPATH=. uv run python data_platform/ingestion/backup_jetstream_cursor.py \\
        backup --cursor-path data_platform/data/bluesky/jetstream/cursor.json
```

Good version:

```python
"""Daily DynamoDB disaster-recovery backup for the Bluesky Jetstream disk cursor.

Run from the repo root:

    PYTHONPATH=. uv run python data_platform/ingestion/backup_jetstream_cursor.py \\
        backup --cursor-path data_platform/data/bluesky/jetstream/cursor.json
```
