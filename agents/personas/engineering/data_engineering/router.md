# 🧭 Agent Persona Router

This folder contains specialized AI agents designed to assist with comprehensive data engineering tasks across three key areas: task-specific expertise, tool-specific optimization, and domain-specific applications.

Use this file to decide which agent persona is best suited for a task or review. If no persona is a good fit, consider creating a new one using `create_persona.md`.

---

## 📁 Directory Structure

### `task_specific/` - Core Data Engineering Tasks
Specialized agents for fundamental data engineering tasks like pipeline design, data quality, monitoring, and infrastructure management.

### `tool_specific/` - Technology-Specific Optimization
Expert agents for optimizing specific tools and technologies like Apache Spark, PostgreSQL, Redis, FastAPI, and more.

### `domain_specific/` - Industry-Specific Applications
Domain-focused agents for real-time analytics and social media data processing.

---

## 🧠 Persona Directory

## Task-Specific Personas

### `task_specific/api_integration_expert.md`
- **Name**: API Integration Expert
- **Summary**: Expert in API integration, data ingestion, and external service connectivity
- **Focus Areas**: API integration design, data ingestion optimization, rate limiting, error handling, data quality validation
- **Example Tasks**: Designing API integration for multiple external data sources, troubleshooting API integration failures

### `task_specific/batch_processing_optimization_expert.md`
- **Name**: Batch Processing Optimization Expert
- **Summary**: Expert in optimizing batch data processing systems for performance and reliability
- **Focus Areas**: Batch job orchestration, resource optimization, parallel processing, failure recovery, performance monitoring
- **Example Tasks**: Optimizing slow batch processing jobs, designing distributed batch processing systems

### `task_specific/columnar_storage_performance_expert.md`
- **Name**: Columnar Storage Performance Expert
- **Summary**: Expert in optimizing columnar storage systems for maximum query performance
- **Focus Areas**: Columnar storage optimization, query performance tuning, storage efficiency, data access patterns
- **Example Tasks**: Optimizing Parquet storage and query performance, choosing optimal storage formats

### `task_specific/data_lake_design_expert.md`
- **Name**: Data Lake Architecture Specialist
- **Summary**: Expert in data lake design, storage optimization, and data organization patterns
- **Focus Areas**: Data lake architecture design, storage optimization strategies, data organization patterns, lake house architecture
- **Example Tasks**: Designing modern data lake architecture using medallion patterns, optimizing data lake performance

### `task_specific/data_lineage_metadata_expert.md`
- **Name**: Data Lineage & Metadata Expert
- **Summary**: Expert in implementing comprehensive data lineage tracking and metadata management
- **Focus Areas**: Data lineage implementation, metadata management systems, data governance frameworks, lineage visualization
- **Example Tasks**: Implementing data lineage tracking for compliance, managing metadata across multiple systems

### `task_specific/data_observability_expert.md`
- **Name**: Data Observability Expert
- **Summary**: Expert in implementing comprehensive data observability systems for debugging
- **Focus Areas**: Data observability implementation, debugging strategies, troubleshooting methodologies, data flow visualization
- **Example Tasks**: Implementing comprehensive data observability for debugging quality issues, setting up observability for complex pipelines

### `task_specific/data_partitioning_strategy_expert.md`
- **Name**: Data Partitioning Strategy Expert
- **Summary**: Expert in designing optimal data partitioning strategies for maximum query performance
- **Focus Areas**: Partitioning strategy design, query performance optimization, data distribution analysis, partition maintenance
- **Example Tasks**: Designing optimal partitioning strategies for large datasets, implementing multi-level partitioning

### `task_specific/data_pipeline_infrastructure_expert.md`
- **Name**: Data Pipeline Infrastructure Specialist
- **Summary**: Expert in data pipeline infrastructure, ETL optimization, and data flow orchestration
- **Focus Areas**: ETL pipeline design, data flow optimization, pipeline monitoring, data quality infrastructure
- **Example Tasks**: Designing robust data pipeline infrastructure, troubleshooting pipeline failures

### `task_specific/data_pipeline_monitoring_expert.md`
- **Name**: Data Pipeline Monitoring Expert
- **Summary**: Expert in designing comprehensive monitoring systems for data pipelines
- **Focus Areas**: Pipeline monitoring architecture, data flow tracking, performance metrics collection, alerting systems
- **Example Tasks**: Building comprehensive monitoring systems for data pipelines, tracking data flow across multiple stages

### `task_specific/data_quality_expert.md`
- **Name**: Data Quality Engineering Expert
- **Summary**: Expert in designing, implementing, and monitoring data quality frameworks
- **Focus Areas**: Data quality framework design, validation rule implementation, data profiling analysis, quality metrics definition
- **Example Tasks**: Implementing robust data quality frameworks, defining and enforcing data quality metrics

### `task_specific/data_warehouse_design_expert.md`
- **Name**: Data Warehouse Design Specialist
- **Summary**: Expert in data warehouse design, dimensional modeling, and query optimization
- **Focus Areas**: Dimensional modeling, star/snowflake schema design, query optimization strategies, data warehouse architecture
- **Example Tasks**: Designing dimensional models using star schema patterns, optimizing slow queries in data warehouses

### `task_specific/etl_pipeline_design_expert.md`
- **Name**: ETL Pipeline Design Expert
- **Summary**: Expert in designing and implementing efficient, scalable ETL pipelines
- **Focus Areas**: ETL architecture design, data flow optimization, pipeline pattern implementation, data transformation logic
- **Example Tasks**: Designing scalable ETL pipeline architecture, optimizing performance bottlenecks in ETL pipelines

### `task_specific/python_data_processing_performance_optimization_expert.md`
- **Name**: Python Data Processing & Performance Optimization Specialist
- **Summary**: Expert in Python data processing optimization, performance tuning, and memory management
- **Focus Areas**: Python async data processing, memory optimization, Python profiling, concurrent data processing
- **Example Tasks**: Optimizing memory usage in data pipelines, optimizing slow data processing pipelines

### `task_specific/python_dependency_management_expert.md`
- **Name**: Python Dependency & Environment Management Specialist
- **Summary**: Expert in uv dependency management, Python environment optimization, and package management
- **Focus Areas**: uv dependency management, Python virtual environment best practices, dependency resolution, package version pinning
- **Example Tasks**: Resolving dependency conflicts in data pipelines, setting up new Python projects with optimal dependency management

### `task_specific/python_test_generation_data_pipelines_expert.md`
- **Name**: Python Test Generation & Data Pipeline Quality Expert
- **Summary**: Expert in comprehensive testing strategies for data engineering systems
- **Focus Areas**: Data pipeline testing strategies, test data management, data quality validation, performance testing
- **Example Tasks**: Implementing comprehensive testing for ETL pipelines, resolving flaky tests in data processing codebases

### `task_specific/schema_management_expert.md`
- **Name**: Schema Management Expert
- **Summary**: Expert in designing and managing data schema evolution, versioning, and compatibility
- **Focus Areas**: Schema evolution strategies, schema versioning, schema validation testing, schema migration planning
- **Example Tasks**: Evolving data schemas while maintaining backward compatibility, managing schema versions across microservices

### `task_specific/storage_infrastructure_expert.md`
- **Name**: Storage Infrastructure Specialist
- **Summary**: Expert in storage optimization, I/O performance analysis, and storage scaling strategies
- **Focus Areas**: Storage performance optimization, I/O pattern analysis, storage scaling strategies, backup and recovery
- **Example Tasks**: Optimizing Parquet write performance and I/O patterns, planning storage infrastructure for new data lakes

## Tool-Specific Personas

### `tool_specific/apache_spark_performance_expert.md`
- **Name**: Apache Spark Performance Expert
- **Summary**: Optimizes Apache Spark performance through memory management, cluster tuning, SQL optimization
- **Focus Areas**: Spark optimization, memory management, cluster tuning, SQL performance, streaming
- **Example Tasks**: Optimize slow Spark jobs with memory and cluster configuration, improve Spark SQL query performance

### `tool_specific/celery_background_tasks_expert.md`
- **Name**: Celery Background Tasks Expert
- **Summary**: Designs distributed task queues for reliable background processing with error handling
- **Focus Areas**: Task queues, distributed processing, error handling, monitoring, performance optimization
- **Example Tasks**: Implement chunked processing for large datasets, add comprehensive monitoring and error handling

### `tool_specific/docker_data_service_expert.md`
- **Name**: Docker Data Service Expert
- **Summary**: Designs containerized data services with proper data persistence, networking, and resource management
- **Focus Areas**: Container architecture, data persistence, networking, resource optimization, production deployment
- **Example Tasks**: Containerize data pipeline with Redis cache and PostgreSQL, optimize Docker configuration for performance

### `tool_specific/fastapi_data_service_expert.md`
- **Name**: FastAPI Data Service Expert
- **Summary**: Builds high-performance FastAPI data services with async patterns, validation, and background processing
- **Focus Areas**: Async programming, API design, data validation, background tasks, performance optimization
- **Example Tasks**: Design async FastAPI service for large dataset processing, optimize FastAPI performance and resolve memory issues

### `tool_specific/feature_flag_data_pipelines_expert.md`
- **Name**: Feature Flag Data Pipeline Expert
- **Summary**: Implements safe staged rollouts for data pipelines with instant rollback capabilities
- **Focus Areas**: Feature flags, risk management, staged rollouts, monitoring integration, instant rollback
- **Example Tasks**: Implement feature flags for ML model deployment, execute emergency rollback for failing data pipeline

### `tool_specific/parquet_optimization_expert.md`
- **Name**: Parquet Optimization Expert
- **Summary**: Optimizes Parquet file formats for data storage with schema design, compression, and partitioning
- **Focus Areas**: Parquet optimization, schema design, compression, partitioning, performance tuning
- **Example Tasks**: Optimize large Parquet files for better query performance, handle schema evolution in Parquet files

### `tool_specific/polars_pandas_performance_expert.md`
- **Name**: Polars/Pandas Performance Expert
- **Summary**: Optimizes DataFrame operations for maximum performance and memory efficiency
- **Focus Areas**: DataFrame optimization, memory management, parallel processing, lazy evaluation, real-time processing
- **Example Tasks**: Optimize slow DataFrame operations and reduce memory usage, implement parallel processing for large datasets

### `tool_specific/postgresql_performance_expert.md`
- **Name**: PostgreSQL Performance Expert
- **Summary**: Optimizes PostgreSQL database performance through query optimization, indexing, and connection pooling
- **Focus Areas**: Query optimization, indexing strategies, partitioning, connection pooling, performance tuning
- **Example Tasks**: Optimize slow analytics queries with indexing, fix connection pool exhaustion and performance issues

### `tool_specific/prefect_orchestration_expert.md`
- **Name**: Prefect Data Pipeline Orchestration Expert
- **Summary**: Designs efficient Prefect flows for data pipeline orchestration with error handling and resource management
- **Focus Areas**: Flow design, task optimization, error handling, resource management, batch processing
- **Example Tasks**: Design ETL pipeline with Redis to Parquet processing, implement batch processing workflows with parallelization

### `tool_specific/prefect_operations_monitoring_expert.md`
- **Name**: Prefect Operations & Monitoring Expert
- **Summary**: Sets up production monitoring, distributed tracing, and disaster recovery for Prefect pipelines
- **Focus Areas**: Production deployment, monitoring, distributed tracing, performance optimization, disaster recovery
- **Example Tasks**: Set up comprehensive monitoring and alerting for Prefect flows, implement distributed tracing and error correlation

### `tool_specific/redis_data_integration_expert.md`
- **Name**: Redis Data Integration Expert
- **Summary**: Optimizes Redis data integration patterns with data structure optimization and clustering strategies
- **Focus Areas**: Redis optimization, data structures, clustering, persistence, monitoring
- **Example Tasks**: Design Redis integration for caching and session management, optimize Redis cluster performance

### `tool_specific/supabase_data_integration_expert.md`
- **Name**: Supabase Data Integration Expert
- **Summary**: Implements data integration solutions using Supabase with real-time subscriptions and Edge Functions
- **Focus Areas**: Supabase integration, real-time subscriptions, Edge Functions, Row Level Security, PostgreSQL optimization
- **Example Tasks**: Implement real-time data synchronization for web applications, set up Edge Functions for serverless data processing

## Domain-Specific Personas

### `domain_specific/real_time_analytics_expert.md`
- **Name**: Real-time Analytics Expert
- **Summary**: Specializes in designing and optimizing real-time analytics systems, streaming data pipelines, and interactive dashboards
- **Focus Areas**: Streaming data processing, real-time analytics dashboards, time-series data management, real-time data quality
- **Example Tasks**: Building real-time dashboards with sub-second latency, diagnosing performance issues in real-time inventory tracking

### `domain_specific/social_media_data_expert.md`
- **Name**: Social Media Data Expert
- **Summary**: Specializes in integrating, processing, and analyzing social media data from multiple platforms
- **Focus Areas**: Multi-platform API integration, social media data patterns, data normalization, rate limiting, social media analytics
- **Example Tasks**: Integrating data from Twitter, Instagram, LinkedIn, and TikTok, resolving data inconsistencies in social media tools

---

## 📌 Routing Guidelines

To determine which persona to use:

1. **Identify the primary focus area**:
   - **Task-specific**: Core data engineering tasks (pipeline design, data quality, monitoring, etc.)
   - **Tool-specific**: Technology optimization (Spark, PostgreSQL, Redis, etc.)
   - **Domain-specific**: Industry applications (real-time analytics, social media)

2. **Look for focus area overlap** between the task and the persona's expertise domains

3. **Check if the task resembles any of the example tasks** listed for each persona

4. **Consider the primary concern** - is it performance, reliability, design, monitoring, or optimization?

5. **If the task requires multiple domains**, select multiple personas for comprehensive coverage

6. **If no persona matches**, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| **Data Pipeline Design & Architecture** | `task_specific/etl_pipeline_design_expert.md`, `task_specific/data_pipeline_infrastructure_expert.md` |
| **Database Performance Issues** | `tool_specific/postgresql_performance_expert.md`, `tool_specific/supabase_data_integration_expert.md` |
| **Containerized Data Services** | `tool_specific/docker_data_service_expert.md`, `tool_specific/fastapi_data_service_expert.md` |
| **Background Processing** | `tool_specific/celery_background_tasks_expert.md`, `task_specific/batch_processing_optimization_expert.md` |
| **Data Storage Optimization** | `tool_specific/parquet_optimization_expert.md`, `tool_specific/redis_data_integration_expert.md` |
| **DataFrame Performance** | `tool_specific/polars_pandas_performance_expert.md`, `tool_specific/apache_spark_performance_expert.md` |
| **API Development** | `tool_specific/fastapi_data_service_expert.md`, `task_specific/api_integration_expert.md` |
| **Production Deployment** | `tool_specific/docker_data_service_expert.md`, `tool_specific/prefect_operations_monitoring_expert.md` |
| **Feature Rollouts** | `tool_specific/feature_flag_data_pipelines_expert.md` |
| **Real-time Processing** | `domain_specific/real_time_analytics_expert.md`, `tool_specific/redis_data_integration_expert.md` |
| **Memory Optimization** | `tool_specific/polars_pandas_performance_expert.md`, `task_specific/python_data_processing_performance_optimization_expert.md` |
| **Monitoring & Observability** | `task_specific/data_pipeline_monitoring_expert.md`, `task_specific/data_observability_expert.md` |
| **Data Quality & Validation** | `task_specific/data_quality_expert.md`, `task_specific/python_test_generation_data_pipelines_expert.md` |
| **Data Lake & Warehouse Design** | `task_specific/data_lake_design_expert.md`, `task_specific/data_warehouse_design_expert.md` |
| **Schema Management** | `task_specific/schema_management_expert.md`, `task_specific/data_lineage_metadata_expert.md` |
| **Social Media Data Processing** | `domain_specific/social_media_data_expert.md` |

---

## 🎯 Specialized Combinations

For complex data engineering tasks, consider combining multiple personas:

- **New Data Platform Design**: `task_specific/data_lake_design_expert.md` + `task_specific/data_warehouse_design_expert.md` + `task_specific/data_lineage_metadata_expert.md`
- **High-Performance ETL Pipeline**: `task_specific/etl_pipeline_design_expert.md` + `task_specific/python_data_processing_performance_optimization_expert.md` + `tool_specific/apache_spark_performance_expert.md`
- **Production Data System**: `task_specific/data_pipeline_monitoring_expert.md` + `task_specific/data_quality_expert.md` + `tool_specific/prefect_operations_monitoring_expert.md`
- **Real-time Social Media Analytics**: `domain_specific/real_time_analytics_expert.md` + `domain_specific/social_media_data_expert.md` + `tool_specific/redis_data_integration_expert.md`
- **Containerized Data Services**: `tool_specific/docker_data_service_expert.md` + `tool_specific/fastapi_data_service_expert.md` + `task_specific/api_integration_expert.md`
- **Storage & Performance Optimization**: `task_specific/storage_infrastructure_expert.md` + `tool_specific/parquet_optimization_expert.md` + `task_specific/data_partitioning_strategy_expert.md`

---

## 🛠️ Update Instructions

After adding new personas to any subdirectory, rerun `create_router.md` to regenerate this file.

---

## Notes

- This router covers 32 specialized data engineering personas across three categories
- Task-specific personas focus on core data engineering concepts and methodologies
- Tool-specific personas provide deep expertise in specific technologies and frameworks
- Domain-specific personas address industry-specific challenges and requirements
- Consider combining multiple personas for complex data engineering projects
- All personas follow the established engineering persona specification format 