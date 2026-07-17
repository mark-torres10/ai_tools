# Example: Pipeline + MemoryRepository

Canonical walkthrough for `implement-from-spec`. Mirror this order; do not invent a different sequence.

**Task:** Build a simple script that loads data from the DB, transforms it, and writes it back via `MemoryRepository`.

## Phase ↔ step map

| Skill phase | This example |
|-------------|----------------|
| 0 — Scope | Caller = `run`; files under `pipeline/` |
| 1 — Scaffold | Step 0 |
| 2 — Contracts | Step 1 |
| 3 — Test design | Step 2 |
| 4 — Flesh UoWs | Steps 3–6 (`get` → `write` → `transform` → `run`) |
| 5 — Done | All designed tests green |

---

## Step 0 — Scaffold files and wiring

```text
pipeline/
  main.py              # caller entrypoint
  models.py            # Pydantic contracts
  repository.py        # repository interface + MemoryRepository
  transform.py         # transform logic (stub)
  tests/
    test_pipeline.py
```

`main.py` only shows how pieces connect — no real logic yet:

```python
# main.py
from models import Record
from repository import MemoryRepository
from transform import transform_record


def run(repo: MemoryRepository, record_id: str) -> Record:
    # load → transform → write (stubbed)
    ...


if __name__ == "__main__":
    repo = MemoryRepository()
    run(repo, record_id="1")
```

---

## Step 1 — Models and boundaries (contracts only)

```python
# models.py
from pydantic import BaseModel


class Record(BaseModel):
    id: str
    value: int
    label: str | None = None


class TransformedRecord(BaseModel):
    id: str
    value: int
    label: str
```

```python
# repository.py
from models import Record, TransformedRecord


class MemoryRepository:
    """In-memory stand-in for a DB. get / write only."""

    def __init__(self) -> None:
        self._store: dict[str, Record] = {}

    def get(self, record_id: str) -> Record:
        ...

    def write(self, record: TransformedRecord) -> TransformedRecord:
        ...
```

```python
# transform.py
from models import Record, TransformedRecord


def transform_record(record: Record) -> TransformedRecord:
    ...
```

Caller shape (still thin, but now typed):

```python
# main.py
def run(repo: MemoryRepository, record_id: str) -> TransformedRecord:
    record = repo.get(record_id)
    transformed = transform_record(record)
    return repo.write(transformed)
```

---

## Step 2 — Expected tests (pseudocode → real)

Pseudocode:

```markdown
given a repo with Record(id="1", value=10, label=None)
when run(repo, "1")
then get returns that record
and transform sets label to "doubled" and value to 20
and write persists TransformedRecord(id="1", value=20, label="doubled")
and run returns that written record

when get("missing")
then raise KeyError

when write(transformed)
then get(transformed.id) returns the written data
```

Real tests (still failing until implementation):

```python
# tests/test_pipeline.py
import pytest
from models import Record, TransformedRecord
from repository import MemoryRepository
from transform import transform_record
from main import run


def test_get_returns_seeded_record():
    repo = MemoryRepository()
    repo._store["1"] = Record(id="1", value=10)  # demo seam; prefer public seed in real code
    assert repo.get("1") == Record(id="1", value=10, label=None)


def test_get_missing_raises():
    repo = MemoryRepository()
    with pytest.raises(KeyError):
        repo.get("missing")


def test_transform_doubles_value_and_sets_label():
    record = Record(id="1", value=10)
    assert transform_record(record) == TransformedRecord(
        id="1", value=20, label="doubled"
    )


def test_write_persists_and_returns():
    repo = MemoryRepository()
    out = repo.write(TransformedRecord(id="1", value=20, label="doubled"))
    assert out == TransformedRecord(id="1", value=20, label="doubled")
    assert repo.get("1").value == 20


def test_run_load_transform_write():
    repo = MemoryRepository()
    repo._store["1"] = Record(id="1", value=10)
    result = run(repo, "1")
    assert result == TransformedRecord(id="1", value=20, label="doubled")
```

---

## Step 3 — Flesh out one unit of work: `MemoryRepository.get`

```python
# repository.py
def get(self, record_id: str) -> Record:
    if record_id not in self._store:
        raise KeyError(record_id)
    return self._store[record_id]
```

Now `test_get_returns_seeded_record` and `test_get_missing_raises` pass.
Everything else still fails.

---

## Step 4 — Next unit: `MemoryRepository.write`

```python
# repository.py
def write(self, record: TransformedRecord) -> TransformedRecord:
    stored = Record(id=record.id, value=record.value, label=record.label)
    self._store[record.id] = stored
    return record
```

Now `test_write_persists_and_returns` passes.
`transform` and `run` still unfinished.

---

## Step 5 — Next unit: `transform_record`

```python
# transform.py
def transform_record(record: Record) -> TransformedRecord:
    return TransformedRecord(
        id=record.id,
        value=record.value * 2,
        label="doubled",
    )
```

Now `test_transform_doubles_value_and_sets_label` passes.

---

## Step 6 — Close the caller path: `run`

```python
# main.py
from models import Record, TransformedRecord
from repository import MemoryRepository
from transform import transform_record


def run(repo: MemoryRepository, record_id: str) -> TransformedRecord:
    record = repo.get(record_id)
    transformed = transform_record(record)
    return repo.write(transformed)


if __name__ == "__main__":
    repo = MemoryRepository()
    repo._store["1"] = Record(id="1", value=10)  # seed
    print(run(repo, "1"))
```

Now `test_run_load_transform_write` passes. Main caller is fully fleshed out; all designed tests are green.
