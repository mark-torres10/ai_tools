# Coding Repo Conventions

## Pre-commit hooks
- For JavaScript/TypeScript: Use Prettier to automatically format and lint the code.
- For JavaScript/TypeScript: verify that builds work without errors (e.g., `npm run build`).
- For Python: Use [Ruff][https://github.com/astral-sh/ruff] to check and enforce styling conventions.
- If pre-commit hooks don't exist for a project yet, set it up on the next commit.
    - For JavaScript/Typescript, add a Linter and also require that `npm run build` passes.
    - For Python projects, use Ruff.

## Package management
- For Python projects, use [uv](https://github.com/astral-sh/uv) for any and all package management. DO NOT USE PIP.
