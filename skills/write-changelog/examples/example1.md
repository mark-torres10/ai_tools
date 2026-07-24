# CHANGELOG

## 2026-07-24

1. Added unified AWS session auth (`app/lib/aws/session.py`) with explicit local profile or remote access-key modes (mutually exclusive), a `BedrockClient` wrapper for Bedrock Runtime, an AWS environment setup runbook, and a verification experiment that runs five Qwen3-32B queries via the Converse API. [PR #69](https://github.com/mark-torres10/kova/pull/69)

## 2026-07-21

1. Completed V1 planning for creating stage vs. prod environments. [PR #56](https://github.com/mark-torres10/kova/pull/56/)
2. Completed V1 planning for app feedback mechanisms, including table schemas, infra details (e.g,. Supabase), UI sketch, and how to expose feedback to the team. [PR #51](https://github.com/mark-torres10/kova/pull/51/)
3. Added backend layer for feedback. Included Alembic migrations, Postgres `FeedbackRepository`, enum-typed `FeedbackCategory`, and a backend route `POST /v1/feedback`. [PR #52](https://github.com/mark-torres10/kova/pull/52)
4. Updated Chainlit feedback UI to ten `FeedbackCategory` labels and POST `feedback_category` (issue #53). [PR #58](https://github.com/mark-torres10/kova/pull/58)
5. Gate feedback UI until the first assistant turn completes so submissions always satisfy backend message-anchor requirements. [PR #62](https://github.com/mark-torres10/kova/pull/62)

## 2026-07-18

1. Migrated Chainlit chats to backend `app.conversations` / `app.messages` tables the source of truth, creating a single source of truth instead of also writing to `public.*` tables. [PR #49](https://github.com/mark-torres10/kova/pull/49)
2. Tore down AWS RDS instances after the migration to Railway and Supabase was completed. Removed RDS terraform under `app/chat/infra/postgres/` and deleted the unused instances and details. Stopped treating AWS as the database path and pivoted to Supabase.
[PR #48](https://github.com/mark-torres10/kova/pull/48)

## 2026-07-17

1. Migrated Kova chat from ECS to a three-service Railway deploy (Chainlit, Backend, LangGraph). [PR #39](https://github.com/mark-torres10/kova/pull/39)
2. Hardened Supabase Postgres tables (`kova_app`, `app` + `langgraph_checkpoint`). Copied data from RDS instance to Supabse. [PR #40](https://github.com/mark-torres10/kova/pull/40)
3. Torn down the legacy AWS ECS chat stack (Express service, ALB, ECR chat repos, IAM, task defs, ECS logs) for a Railway-only hard cutover. Currently retains RDS until Supabase migration is completed. Removed ECS terraform/scripts/runbooks from deployment. [PR #43](https://github.com/mark-torres10/kova/pull/43)
4. Fixed Slack link unfurl preview by setting Chainlit `custom_meta_image_url` to the placeholder company logo. [PR #46](https://github.com/mark-torres10/kova/pull/46)
5. Added feature-flagged conversation feedback in the Chainlit UI. The interface each assistant reply expands vertically into four options (too long, didn't feel good, didn't understand me, It's something else). [PR #45](https://github.com/mark-torres10/kova/pull/45)
6. Hard-cutover Railway chat to Supabase Postgres. [PR #44](https://github.com/mark-torres10/kova/pull/44)

## 2026-07-16

1. Various improvements to promote a more graceful chat recovery on failure: classify httpx errors into calm timeout / unreachable / generic copy, persist `last_user_message` to allow for retries, soften empty/untitled strings (`No past check-ins yet` / `New check-in`), and update runbooks. [PR #38](https://github.com/mark-torres10/kova/pull/38)
2. Completed V1 end-to-end evals + integration testing design planning for the Kova AI chat experience. [PR #28](https://github.com/mark-torres10/kova/pull/28).

## 2026-07-15

1. Recovered production chat after RDS secret rotation by refreshing ECS task credentials, hardened the LangGraph Postgres checkpointer pool, added structured checkpointer error logging / CloudWatch alarms / recovery runbooks, and shipped the latest `kova-api:latest` image to prod. [PR #27](https://github.com/mark-torres10/kova/pull/27)
2. Add Chainlit v1 fake UI streaming: thinking step with five message variants, then progressive `stream_token` reveal of the completed assistant reply (API remains non-streaming). Suppress Chainlit default "Using/used" step prefixes via empty translation overrides so thinking copy reads cleanly. [PR #35](https://github.com/mark-torres10/kova/pull/35)
3. Warm first canvas: brand welcome copy, three conversation starters, quieter en-US placeholder, interim `public/` logo/avatar assets packed in the Chainlit Dockerfile, and updated smoke/local runbooks (issue #30). [PR #37](https://github.com/mark-torres10/kova/pull/37)
4. Official Kova logo v1 + calm companion theme: `static/kova_logo_v1.png` canonical asset, Chainlit `public/logo_*` / favicon derivatives, sage/olive/teal `kova.css` + `theme.json`, replacing default Chainlit empty-state branding. [PR #37](https://github.com/mark-torres10/kova/pull/37)

## 2026-07-14

1. Allocate `user_message_id` / `assistant_message_id` once in `run_chat`. [PR #24](https://github.com/mark-torres10/kova/pull/24)
2. Added system and implementation design for AI chat safety, writes, and reads. Finished V1 architecture flow and design of the full Kova AI chat experience. [PR #25](https://github.com/mark-torres10/kova/pull/25)

## 2026-07-13

1. Added chat safety implementation: multi-tiered safety policy, heuristic and LLM-based detection. Wiring safety detection into LangGraph. Added PII scrubbing. [PR #22](https://github.com/mark-torres10/kova/pull/22)

## 2026-07-12

1. Added a stubbed `craft_user_response` LangGraph node (with `record_violation`) so success and policy-failure paths craft user-facing text before streaming, and `write_memories` fans out from `store_response`. [PR #20](https://github.com/mark-torres10/kova/pull/20)

## 2026-07-08

1. Required TLS for chat Postgres connections so ECS can connect to RDS when `rds.force_ssl` is enabled. [PR #15](https://github.com/mark-torres10/kova/pull/15)
2. Added a multi-provider LLM experiment under `experiments/llm_provider_experiments_2026_06_07/` with smoke tests, rubric judging, king-of-the-hill comparisons, and initial benchmark results across OpenAI, Anthropic, Bedrock, and Gemini. [PR #16](https://github.com/mark-torres10/kova/pull/16)
3. Fixed production chat persistence by enabling Chainlit thread/sidebar storage in Postgres, adding backend conversation/message read APIs, wiring DB credentials to the Chainlit container, and auto-applying the Chainlit schema on startup. [PR #17](https://github.com/mark-torres10/kova/pull/17)
4. Renamed conversation history types from `ConversationSummary` to `ConversationListItem` to free `conversation_summaries` nomenclature for upcoming AI memory work without changing the JSON API contract. [PR #18](https://github.com/mark-torres10/kova/pull/18)
5. Added the foundations for memory retrieval: Alembic migration for eight memory tables, SQLAlchemy models, stub and Postgres `MemoryRepository`, memory-type retrieval, prompt builder integration. [PR #19](https://github.com/mark-torres10/kova/pull/19)

## 2026-07-07

1. Replaced the linear five-node chat LangGraph with a branched query pipeline . Current pipeline is stubbed with no implemented. [PR #13](https://github.com/mark-torres10/kova/pull/13).

## 2026-06-17

1. Added ECS Express Mode deployment for Kova Chat under `app/chat/infra/`: three-container Fargate task (Chainlit, FastAPI, chat agent), Terraform, ECR, deploy/verify scripts, and runbooks including per-service build-and-push and manual verification. [PR #9](https://github.com/mark-torres10/kova/pull/9)
2. Added PostgreSQL RDS under `app/chat` with restricted ingress, Secrets Manager credentials, live `kova-app` networking discovery, and `DB_*` env/secret wiring in the ECS task definition, register/verify scripts, and runbooks. [PR #8](https://github.com/mark-torres10/kova/pull/8) [PR #10](https://github.com/mark-torres10/kova/pull/10).
3. Wired `app/chat/` to Postgres behind local/prod backends: Alembic migrations for `app.conversations` and `app.messages`, `PostgresConversationRepository`, a Postgres LangGraph checkpointer, and runbooks/scripts for provisioning, migrations, and local verification. Also keeps stub persistence and SQLite checkpointing as the default for `pytest` (so this'll work for local testing + local runs). [PR #11](https://github.com/mark-torres10/kova/pull/11)
4. Replace ECS placeholder services with real Chainlit -> FastAPI -> LangGraph chat. Introduces a Chainlit client, API ECS entrypoint, Docker builds, Postgres runtime, and updated deploy runbooks. [PR #12](https://github.com/mark-torres10/kova/pull/12)

## 2026-06-16

1. Added Kova Chat API v1 under `app/chat/`: FastAPI `POST /v1/chat/messages`, five-node LangGraph scaffold, SQLite checkpointer, stub conversation repository, Pydantic request/response models, LangSmith run metadata, and unit plus integration tests with mocked LLM. Currently uses a default model: `gpt-5.4-nano`. [PR #6](https://github.com/mark-torres10/kova/pull/6)
2. Bootstrapped LangSmith tracing at API startup (`configure_langsmith_tracing`).
3. Refactored chat model provider: `get_chat_openai_model()` for OpenAI-specific setup and `get_chat_model()` as the graph-facing `BaseChatModel` swap point. [PR #6](https://github.com/mark-torres10/kova/pull/6)
4. Added chat runbooks under `docs/runbooks/chat/` (local dev, LangSmith, graph extension, thread debugging, model swap), a runbook template at `docs/runbooks/template_runbook.md`, and a breaking-changes note in `docs/runbooks/agents/AGENTS_BEST_PRACTICES.md`. [PR #6](https://github.com/mark-torres10/kova/pull/6)

## 2026-06-12

1. Added a v1 LLM-as-a-judge evaluation layer under `app/evaluation/` with registered criteria, behavior, and safety prompts, plus `LLMJudge`, transcript formatting, concurrent evaluation runner, and structured report output. [PR #4](https://github.com/mark-torres10/kova/pull/4)
2. Wired the evaluation layer into the Chainlit chat demo as a conversation score card: facilitators pick checks in Chat Settings, run a supervision review from the chat, and get a scrollable inline results table scored across criteria, behaviors, and safety. [PR #4](https://github.com/mark-torres10/kova/pull/4)

## 2026-06-11

1. Added a Summarization Agent that parses PDFs via LlamaParse and writes structured summaries to `knowledge_base/agents/summarization_agent/summaries/`. [PR #1](https://github.com/mark-torres10/kova/pull/1)
2. Added an Insights Agent that reads the Convene MVP summary and proposed plan, synthesizes 1–2 unique feature ideas, and posts them to Slack via `slack_dm` with an `[Insights Agent]` prefix. [PR #2](https://github.com/mark-torres10/kova/pull/2)
3. Added AgentCore deploy experiment: insights agent on Bedrock AgentCore Runtime with CLI, Docker ARM64 packaging, and boto3 deploy/invoke scripts. [PR #3](https://github.com/mark-torres10/kova/pull/3)
