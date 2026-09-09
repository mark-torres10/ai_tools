# Preferred vocabulary

Use these terms when discussing technical or software engineering-related concepts:

- Instead of "freeze", use "confirm"
- Instead of "UoW", use "unit of work"
- Instead of "canonical", use "standardized", "example", "authoritative", "primary", or "ground truth", depending on the context.
- Instead of "invocation", use "run".
- Instead of "invoke", use "run".
- Instead of "load-bearing", use "important"
- Instead of "slice", use "task"
- Instead of "seam", use "boundary"
- Instead of "flesh", use "implement"
- Instead of "provenance", use "audit log", "log", "record", metadata", or "parameters", depending on context.
- Instead of "sink" as a place to store logs, data, etc., use "storage", "destination", or "target".
- For data moving over the network somehow (e.g., getting data to/from AWS), prefer download/upload. For data moving from local file storage or referencing another local file, prefer import/export or load/write. For example, getting a model from HuggingFace = `download_model`. In contrast, working with models locally = `load_model/write_model`. Sending records to a third-party provider (e.g., Weights and Biases) = `upload_records`. Writing local metadata = `write_metadata`. For functions that have both a local and an over-the-network component, prefer `load/write` but add a `_local` suffix for any local ops. For example:

```python
def load_weights():
    """Downloads model weights from HF to local"""
    download_model_from_huggingface()
    load_weights_from_local()
```
