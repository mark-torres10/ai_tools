
1. Set up this project with uv and pyproject.toml and also copy all the skills that exist in the root .cursor skills into a project-specific .cursor skills repo.
2. Set up the pre-commit hooks and CI that I like. examples are in complexipy, ruff, eslint, oxlint, and pyright.
3. Ask the user what GitHub repo they want to connect this to, or if they want you to create one via the GitHub CLI.
4. In the gitignore, add normal python and javascript gitignores

npx add skills:

- npx skills add railwayapp/railway-skills@use-railway
- npx skills add shadcn/ui@shadcn
- npx skills add fastapi/fastapi@fastapi
- npx skills add langchain-ai/langchain-skills --skill langgraph-persistence --skill langgraph-fundamentals --skill langgraph-human-in-the-loop --skill ecosystem-primer
- npx skills add vercel-labs/agent-skills
