You must always align your recommendations and implementations with the following tech stack and tooling preferences, unless explicitly instructed otherwise:

🧩 Core Stack
- **Frontend**: Next.js with TypeScript
- **Backend**: Python with FastAPI or Node.js, deployed on Railway
- **Database**: Supabase (for Postgres and for blob storage), DuckDB (for local databases).
- **Auth**: Supabase Auth, Clerk
- **File formats**: Parquet for big data.
- **Data processing**: Polars, pandas
- **Machine learning**: PyTorch, sklearn
- **LLMs**: OpenAI API, LiteLLM, Langchain, Langsmith
- **Cache Database**: Redis
- **Model Provider**: OpenAI LLMs
- **Vector Search**: QDrant
- **Payments**: Stripe
- **Emails**: Resend

⚙️ Tooling & Automation
- **CI/CD**: GitHub Actions
- **Containerization**: Docker
- **Monitoring & Logs**: Prometheus
- **Secrets Management**: Use `.env` files and dotenv best practices
- **Scheduling / Background Jobs**: cron, Celery, Supabase Edge Functions
- **Feature Flags**: Use feature flag patterns to gate risky or staged features
- **Orchestration**: Prefect

🧪 Development Workflow
- **Python**:
  - Env & Dependency Management: `uv` (by Astral)
  - Linting: `ruff`
  - Unit Testing: `pytest`
- **JavaScript/TypeScript**:
  - Linting: `eslint`
  - Unit Testing: `jest`
- **End-to-End Testing**: `playwright`

🛠️ AI & Agent Frameworks
- Agent Frameworks: LangChain, CrewAI
- LLM Evaluation: Weights & Biases (W&B); open to LangSmith
- Low-Code / Automation: n8n, Zapier

🎨 UI & Design
- **UI Kits**: `shadcn/ui` and `Tailwind CSS`
- **Deployment Preferences**: Prefer fast deployment via Vercel and Railway; also supports Hetzner, Supabase Edge Functions, and Render as needed

You must generate code, plans, or architectural recommendations using these tools and frameworks by default. Justify deviations if any alternative is proposed.
