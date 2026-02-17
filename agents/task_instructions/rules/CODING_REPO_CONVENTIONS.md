---
id: rules.coding_repo_conventions
title: Repository Conventions
description: Repository-level conventions for pre-commit checks, formatting, build verification, and package management.
when_to_use:
  - Preparing code for commit.
  - Setting or auditing pre-commit conventions.
  - Making decisions about project package-management tooling.
when_not_to_use:
  - Deep code architecture decisions.
  - Server runtime troubleshooting.
scope:
  - repo_conventions
  - pre_commit
priority: 70
applies_to:
  task_types:
    - commit_preparation
    - linting
    - formatting
    - package_management
  file_globs:
    - "**/*"
dependencies: []
conflicts_with: []
tools_preferred:
  - Shell
  - ReadFile
owner: ai_tools
last_updated: 2026-02-17
---

# Coding Repo Conventions

## Pre-commit hooks

- For JavaScript/TypeScript: Use Prettier to automatically format and lint the code.
- For JavaScript/TypeScript: verify that builds work without errors (e.g., `npm run build`).
- For Python: Use [Ruff][https://github.com/astral-sh/ruff] to check and enforce styling conventions.
- If pre-commit hooks don't exist for a project yet, set it up on the next commit.
    - For JavaScript/Typescript:
        - Add a linter
        - Require that `npm run build` passes.
        - For any frontend changes, use the `playwright` MCP to check the local build and vrify that the requested features have been added.

    - For Python projects, use Ruff.

## Package management

- For Python projects, use [uv](https://github.com/astral-sh/uv) for any and all package management. DO NOT USE PIP.
