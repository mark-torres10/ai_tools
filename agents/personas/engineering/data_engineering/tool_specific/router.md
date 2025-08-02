# 🧭 Agent Persona Router

This folder contains specialized AI agents designed to assist with various data engineering tool-specific tasks across data processing, storage, integration, and optimization workflows.

Use this file to decide which agent persona is best suited for a task or review. If no persona is a good fit, consider creating a new one using `create_persona.md`.

---

## 🧠 Persona Directory

### `apache_spark_performance_expert.md`
- **Name**: Apache Spark Performance Expert
- **Summary**: Optimizes Apache Spark performance through memory management, cluster tuning, SQL optimization, and streaming performance
- **Focus Areas**: Spark optimization, memory management, cluster tuning, SQL performance, streaming
- **Example Tasks**:
  - Optimize slow Spark jobs with memory and cluster configuration
  - Improve Spark SQL query performance with adaptive execution
  - Set up Spark streaming for real-time data processing

### `celery_background_tasks_expert.md`
- **Name**: Celery Background Tasks Expert
- **Summary**: Designs distributed task queues for reliable background processing with error handling and monitoring
- **Focus Areas**: Task queues, distributed processing, error handling, monitoring, performance optimization
- **Example Tasks**:
  - Implement chunked processing for large datasets with parallel workers
  - Add comprehensive monitoring and error handling to failing tasks
  - Optimize Celery performance for high-throughput processing

### `docker_data_service_expert.md`
- **Name**: Docker Data Service Expert
- **Summary**: Designs containerized data services with proper data persistence, networking, and resource management
- **Focus Areas**: Container architecture, data persistence, networking, resource optimization, production deployment
- **Example Tasks**:
  - Containerize data pipeline with Redis cache and PostgreSQL database
  - Optimize Docker configuration for memory issues and performance
  - Set up production Docker environment with monitoring and backup

### `fastapi_data_service_expert.md`
- **Name**: FastAPI Data Service Expert
- **Summary**: Builds high-performance FastAPI data services with async patterns, validation, and background processing
- **Focus Areas**: Async programming, API design, data validation, background tasks, performance optimization
- **Example Tasks**:
  - Design async FastAPI service for large dataset processing
  - Optimize FastAPI performance and resolve memory issues
  - Deploy production FastAPI service with monitoring and scaling

### `feature_flag_data_pipelines_expert.md`
- **Name**: Feature Flag Data Pipeline Expert
- **Summary**: Implements safe staged rollouts for data pipelines with instant rollback capabilities
- **Focus Areas**: Feature flags, risk management, staged rollouts, monitoring integration, instant rollback
- **Example Tasks**:
  - Implement feature flags for ML model deployment with monitoring
  - Execute emergency rollback for failing data pipeline
  - Design component-level feature flags for complex data pipelines

### `parquet_optimization_expert.md`
- **Name**: Parquet Optimization Expert
- **Summary**: Optimizes Parquet file formats for data storage with schema design, compression, and partitioning
- **Focus Areas**: Parquet optimization, schema design, compression, partitioning, performance tuning
- **Example Tasks**:
  - Optimize large Parquet files for better query performance
  - Handle schema evolution in Parquet files with backward compatibility
  - Design optimal partitioning strategy for large datasets

### `polars_pandas_performance_expert.md`
- **Name**: Polars/Pandas Performance Expert
- **Summary**: Optimizes DataFrame operations for maximum performance and memory efficiency
- **Focus Areas**: DataFrame optimization, memory management, parallel processing, lazy evaluation, real-time processing
- **Example Tasks**:
  - Optimize slow DataFrame operations and reduce memory usage
  - Implement parallel processing for large datasets with Polars
  - Optimize DataFrame operations for real-time data processing

### `postgresql_performance_expert.md`
- **Name**: PostgreSQL Performance Expert
- **Summary**: Optimizes PostgreSQL database performance through query optimization, indexing, and connection pooling
- **Focus Areas**: Query optimization, indexing strategies, partitioning, connection pooling, performance tuning
- **Example Tasks**:
  - Optimize slow analytics queries with indexing and query restructuring
  - Fix connection pool exhaustion and performance issues
  - Implement table partitioning for large datasets

### `prefect_orchestration_expert.md`
- **Name**: Prefect Data Pipeline Orchestration Expert
- **Summary**: Designs efficient Prefect flows for data pipeline orchestration with error handling and resource management
- **Focus Areas**: Flow design, task optimization, error handling, resource management, batch processing
- **Example Tasks**:
  - Design ETL pipeline with Redis to Parquet processing
  - Implement batch processing workflows with parallelization
  - Set up error recovery and dead letter queues for robust pipelines

### `prefect_operations_monitoring_expert.md`
- **Name**: Prefect Operations & Monitoring Expert
- **Summary**: Sets up production monitoring, distributed tracing, and disaster recovery for Prefect pipelines
- **Focus Areas**: Production deployment, monitoring, distributed tracing, performance optimization, disaster recovery
- **Example Tasks**:
  - Set up comprehensive monitoring and alerting for Prefect flows
  - Implement distributed tracing and error correlation
  - Optimize Prefect server performance and implement disaster recovery

### `redis_data_integration_expert.md`
- **Name**: Redis Data Integration Expert
- **Summary**: Optimizes Redis data integration patterns with data structure optimization and clustering strategies
- **Focus Areas**: Redis optimization, data structures, clustering, persistence, monitoring
- **Example Tasks**:
  - Design Redis integration for caching and session management
  - Optimize Redis cluster performance and memory usage
  - Set up high-availability Redis with persistence and backup

### `supabase_data_integration_expert.md`
- **Name**: Supabase Data Integration Expert
- **Summary**: Implements data integration solutions using Supabase with real-time subscriptions and Edge Functions
- **Focus Areas**: Supabase integration, real-time subscriptions, Edge Functions, Row Level Security, PostgreSQL optimization
- **Example Tasks**:
  - Implement real-time data synchronization for web applications
  - Set up Edge Functions for serverless data processing
  - Optimize Supabase performance and implement Row Level Security

---

## 📌 Routing Guidelines

To determine which persona to use:

1. Look for **focus area overlap** between the task and the persona.
2. Check if the task resembles any of the **example tasks** listed.
3. If the task requires more than one domain, select multiple personas.
4. If no persona matches, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| **Data Pipeline Orchestration** | `prefect_orchestration_expert.md`, `prefect_operations_monitoring_expert.md` |
| **Database Performance Issues** | `postgresql_performance_expert.md`, `supabase_data_integration_expert.md` |
| **Containerized Data Services** | `docker_data_service_expert.md`, `fastapi_data_service_expert.md` |
| **Background Processing** | `celery_background_tasks_expert.md`, `prefect_orchestration_expert.md` |
| **Data Storage Optimization** | `parquet_optimization_expert.md`, `redis_data_integration_expert.md` |
| **DataFrame Performance** | `polars_pandas_performance_expert.md`, `apache_spark_performance_expert.md` |
| **API Development** | `fastapi_data_service_expert.md`, `supabase_data_integration_expert.md` |
| **Production Deployment** | `docker_data_service_expert.md`, `prefect_operations_monitoring_expert.md` |
| **Feature Rollouts** | `feature_flag_data_pipelines_expert.md` |
| **Real-time Processing** | `redis_data_integration_expert.md`, `supabase_data_integration_expert.md` |
| **Memory Optimization** | `polars_pandas_performance_expert.md`, `apache_spark_performance_expert.md` |
| **Monitoring & Observability** | `prefect_operations_monitoring_expert.md`, `celery_background_tasks_expert.md` |

---

## 🛠️ Update Instructions

After adding new personas to this folder, rerun `create_router.md` to regenerate this file.

---

## Notes

- This router covers 12 specialized data engineering tool personas
- Focus areas span from data processing (Spark, Polars/Pandas) to storage (Parquet, Redis, PostgreSQL)
- Orchestration tools (Prefect, Celery) and API development (FastAPI, Supabase) are included
- Each persona specializes in specific tools and optimization techniques
- Consider combining multiple personas for complex data engineering tasks 