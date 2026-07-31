# Class Docstrings

Describe the abstraction the class represents and the responsibilities it owns. Do not restate constructor parameters.

## Criteria

A good class docstring:

- Names what the object **is** (the abstraction)
- States its primary **responsibility**
- Mentions lifecycle or state when that affects callers
- Records important **invariants**
- Notes major collaborators only when that clarifies the role
- Does **not** dump `__init__` args (put those on `__init__` if needed)

It should answer:

1. What concept does an instance represent?
2. What is this class allowed / required to do?
3. What must always stay true while it is alive?

## What to cover

| Cover | Skip |
|-------|------|
| Role and boundary of the type | Echo of every attribute |
| Invariants and ownership | Blow-by-blow of methods |
| Thread-safety / lifecycle if non-obvious | Restating `__init__` parameters |
| Collaboration that defines the design | Implementation of private helpers |

## Good vs bad

### Abstraction and responsibility

Good — what it represents:

```python
"""
Represents an authenticated user session.
"""
```

Good — what it coordinates:

```python
"""
Coordinates ingestion jobs across multiple workers while ensuring
that each file is processed exactly once.
"""
```

Good — invariant:

```python
"""
At most one ingestion job may exist per dataset.
"""
```

### Full example

Bad — tautology; no contract:

```python
class Cache:
    """
    Cache class.

    Stores cache.
    """
```

Good — policy, eviction, concurrency:

```python
class Cache:
    """
    In-memory LRU cache for expensive query results.

    Automatically evicts the least recently used entries once the
    configured capacity is reached. Thread-safe for concurrent reads
    and writes.
    """
```

### Full example (no constructor dump)

Bad — restates `__init__` args; skips what the type owns:

```python
class IngestionCoordinator:
    """
    Ingestion coordinator.

    Parameters
    ----------
    workers : int
        Number of workers.
    queue : Queue
        Job queue.
    store : DatasetStore
        Dataset store.
    """
```

Good — responsibility, invariant, collaborator role; ctor details stay on `__init__`:

```python
class IngestionCoordinator:
    """
    Coordinates ingestion jobs across workers so each file is processed
    exactly once.

    Owns scheduling and deduplication against the dataset store. At most
    one active job may exist per dataset. Workers pull work from the
    shared queue; this class does not perform file I/O itself.
    """
```

## Anti-patterns

- "X class" / "Handles X" with no extra meaning
- Pasting the constructor signature into the class docstring
- Documenting every public method in the class docstring (use method docstrings)
- Claiming invariants the implementation does not enforce
