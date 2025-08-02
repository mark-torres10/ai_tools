# 🧭 Agent Persona Router

This folder contains specialized AI agents designed to assist with various data engineering tasks across pipeline design, performance optimization, data quality, monitoring, and infrastructure management.

Use this file to decide which agent persona is best suited for a task or review. If no persona is a good fit, consider creating a new one using `create_persona.md`.

---

## 🧠 Persona Directory

### `api_integration_expert.md`
- **Name**: API Integration Expert
- **Summary**: Expert in API integration, data ingestion, and external service connectivity for data engineering systems
- **Focus Areas**: API integration design, data ingestion optimization, rate limiting, error handling, data quality validation, external service connectivity
- **Example Tasks**:
  - Designing API integration for multiple external data sources with different rate limits
  - Troubleshooting API integration failures and implementing comprehensive error handling
  - Optimizing API integration performance and scaling with intelligent rate limiting

### `batch_processing_optimization_expert.md`
- **Name**: Batch Processing Optimization Expert
- **Summary**: Expert in optimizing batch data processing systems for performance, reliability, and resource efficiency
- **Focus Areas**: Batch job orchestration, resource optimization, parallel processing, failure recovery, performance monitoring, data partitioning
- **Example Tasks**:
  - Optimizing slow batch processing jobs with parallel processing and memory optimization
  - Designing distributed batch processing systems for large-scale data analytics
  - Implementing robust error handling and reliability patterns for batch jobs

### `columnar_storage_performance_expert.md`
- **Name**: Columnar Storage Performance Expert
- **Summary**: Expert in optimizing columnar storage systems for maximum query performance and storage efficiency
- **Focus Areas**: Columnar storage optimization, query performance tuning, storage efficiency, data access patterns, storage cost management, analytical workload optimization
- **Example Tasks**:
  - Optimizing Parquet storage and query performance for analytics workloads
  - Choosing optimal storage formats (Parquet, Delta Lake, Iceberg) for specific use cases
  - Implementing storage optimization and cost management strategies

### `data_lake_design_expert.md`
- **Name**: Data Lake Architecture Specialist
- **Summary**: Expert in data lake design, storage optimization, and data organization patterns for scalable data engineering systems
- **Focus Areas**: Data lake architecture design, storage optimization strategies, data organization patterns, lake house architecture, data catalog implementation, data governance
- **Example Tasks**:
  - Designing modern data lake architecture using medallion patterns with bronze/silver/gold layers
  - Optimizing data lake performance and storage costs with intelligent partitioning
  - Implementing data governance and catalog systems for data discoverability

### `data_lineage_metadata_expert.md`
- **Name**: Data Lineage & Metadata Expert
- **Summary**: Expert in implementing comprehensive data lineage tracking, metadata management, and data governance frameworks
- **Focus Areas**: Data lineage implementation, metadata management systems, data governance frameworks, lineage visualization, impact analysis, data catalog management
- **Example Tasks**:
  - Implementing data lineage tracking for compliance and audit requirements
  - Managing metadata across multiple systems for data discovery and governance
  - Implementing impact analysis for data changes on downstream systems

### `data_observability_expert.md`
- **Name**: Data Observability Expert
- **Summary**: Expert in implementing comprehensive data observability systems for effective debugging and troubleshooting
- **Focus Areas**: Data observability implementation, debugging strategies, troubleshooting methodologies, data flow visualization, root cause analysis, anomaly detection
- **Example Tasks**:
  - Implementing comprehensive data observability for debugging quality issues
  - Setting up observability for complex multi-stage data pipelines
  - Improving debugging capabilities for production data issues

### `data_partitioning_strategy_expert.md`
- **Name**: Data Partitioning Strategy Expert
- **Summary**: Expert in designing optimal data partitioning strategies for maximum query performance and scalable data processing
- **Focus Areas**: Partitioning strategy design, query performance optimization, data distribution analysis, partition maintenance, scalability planning, multi-level partitioning
- **Example Tasks**:
  - Designing optimal partitioning strategies for large datasets with slow query performance
  - Implementing multi-level partitioning for mixed analytical and transactional workloads
  - Resolving data skew and partition imbalance issues in production systems

### `data_pipeline_infrastructure_expert.md`
- **Name**: Data Pipeline Infrastructure Specialist
- **Summary**: Expert in data pipeline infrastructure, ETL optimization, and data flow orchestration for scalable data engineering systems
- **Focus Areas**: ETL pipeline design, data flow optimization, pipeline monitoring, data quality infrastructure, pipeline orchestration, error handling
- **Example Tasks**:
  - Designing robust data pipeline infrastructure with proper error handling and monitoring
  - Troubleshooting pipeline failures and implementing comprehensive monitoring
  - Optimizing pipeline performance and scaling with parallel processing

### `data_pipeline_monitoring_expert.md`
- **Name**: Data Pipeline Monitoring Expert
- **Summary**: Expert in designing and implementing comprehensive monitoring systems for data pipelines to ensure reliability and observability
- **Focus Areas**: Pipeline monitoring architecture, data flow tracking, performance metrics collection, pipeline health monitoring, data quality monitoring, alerting systems
- **Example Tasks**:
  - Building comprehensive monitoring systems for data pipelines with proper alerting
  - Tracking data flow and performance metrics across multiple pipeline stages
  - Implementing real-time monitoring and alerting for data pipeline health

### `data_quality_expert.md`
- **Name**: Data Quality Engineering Expert
- **Summary**: Expert in designing, implementing, and monitoring data quality frameworks to ensure data integrity and reliability
- **Focus Areas**: Data quality framework design, validation rule implementation, data profiling analysis, quality metrics definition, quality monitoring alerting, continuous improvement
- **Example Tasks**:
  - Implementing robust data quality frameworks for analytics reliability
  - Defining and enforcing data quality metrics for ETL pipelines
  - Setting up early detection and alerting for data quality failures

### `data_warehouse_design_expert.md`
- **Name**: Data Warehouse Design Specialist
- **Summary**: Expert in data warehouse design, dimensional modeling, and query optimization for analytical data systems
- **Focus Areas**: Dimensional modeling, star/snowflake schema design, query optimization strategies, data warehouse architecture, ETL optimization, indexing strategies
- **Example Tasks**:
  - Designing dimensional models using star schema patterns for e-commerce analytics
  - Optimizing slow queries in existing data warehouses with proper indexing
  - Planning data warehouse migration and scaling strategies

### `etl_pipeline_design_expert.md`
- **Name**: ETL Pipeline Design Expert
- **Summary**: Expert in designing and implementing efficient, scalable ETL pipelines that optimize data flow and transformation logic
- **Focus Areas**: ETL architecture design, data flow optimization, pipeline pattern implementation, data transformation logic, pipeline orchestration, performance optimization
- **Example Tasks**:
  - Designing scalable ETL pipeline architecture for large-scale social media data processing
  - Optimizing performance bottlenecks in existing ETL pipelines
  - Implementing streaming ETL patterns with proper trade-off analysis

### `python_data_processing_performance_optimization_expert.md`
- **Name**: Python Data Processing & Performance Optimization Specialist
- **Summary**: Expert in Python data processing optimization, performance tuning, and memory management for high-throughput data engineering systems
- **Focus Areas**: Python async data processing, memory optimization, Python profiling, concurrent data processing, data structure optimization, garbage collection optimization
- **Example Tasks**:
  - Optimizing memory usage in data pipelines processing large datasets
  - Optimizing slow data processing pipelines with parallel processing strategies
  - Debugging intermittent performance issues in production data processing systems

### `python_dependency_management_expert.md`
- **Name**: Python Dependency & Environment Management Specialist
- **Summary**: Expert in uv dependency management, Python environment optimization, and package management best practices for data engineering systems
- **Focus Areas**: uv dependency management, Python virtual environment best practices, dependency resolution, package version pinning, development vs production dependency management, lock file management
- **Example Tasks**:
  - Resolving dependency conflicts in data pipelines with proper version management
  - Setting up new Python projects with optimal dependency management practices
  - Troubleshooting production deployment issues related to dependencies

### `python_test_generation_data_pipelines_expert.md`
- **Name**: Python Test Generation & Data Pipeline Quality Expert
- **Summary**: Expert in comprehensive testing strategies for data engineering systems to ensure robustness and reliability
- **Focus Areas**: Data pipeline testing strategies, test data management, data quality validation, performance testing, test automation, code coverage analysis
- **Example Tasks**:
  - Implementing comprehensive testing for ETL pipelines with unit and integration tests
  - Resolving flaky tests in data processing codebases with proper mocking
  - Mentoring teams on testing best practices for data services

### `schema_management_expert.md`
- **Name**: Schema Management Expert
- **Summary**: Expert in designing and managing data schema evolution, versioning, and compatibility to ensure data integrity
- **Focus Areas**: Schema evolution strategies, schema versioning, schema validation testing, schema migration planning, schema registry management, compatibility management
- **Example Tasks**:
  - Evolving data schemas while maintaining backward compatibility
  - Managing schema versions across multiple microservices to prevent conflicts
  - Planning major schema migrations with zero-downtime strategies

### `storage_infrastructure_expert.md`
- **Name**: Storage Infrastructure Specialist
- **Summary**: Expert in storage optimization, I/O performance analysis, and storage scaling strategies for data engineering systems
- **Focus Areas**: Storage performance optimization, I/O pattern analysis, storage scaling strategies, backup and recovery, storage monitoring, data format optimization
- **Example Tasks**:
  - Optimizing Parquet write performance and I/O patterns in data pipelines
  - Planning storage infrastructure for new data lakes with tiered storage strategies
  - Investigating storage performance degradation and I/O bottlenecks

---

## 📌 Routing Guidelines

To determine which persona to use:

1. **Look for focus area overlap** between the task and the persona's expertise domains
2. **Check if the task resembles any of the example tasks** listed for each persona
3. **Consider the primary concern** - is it performance, reliability, design, monitoring, or optimization?
4. **If the task requires multiple domains**, select multiple personas for comprehensive coverage
5. **If no persona matches**, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| **API Integration & Data Ingestion** | `api_integration_expert.md` |
| **Batch Processing & Job Optimization** | `batch_processing_optimization_expert.md` |
| **Columnar Storage & Query Performance** | `columnar_storage_performance_expert.md` |
| **Data Lake Architecture & Governance** | `data_lake_design_expert.md` |
| **Data Lineage & Metadata Management** | `data_lineage_metadata_expert.md` |
| **Data Observability & Debugging** | `data_observability_expert.md` |
| **Data Partitioning & Query Optimization** | `data_partitioning_strategy_expert.md` |
| **ETL Pipeline Design & Architecture** | `etl_pipeline_design_expert.md` |
| **Pipeline Infrastructure & Orchestration** | `data_pipeline_infrastructure_expert.md` |
| **Pipeline Monitoring & Alerting** | `data_pipeline_monitoring_expert.md` |
| **Data Quality & Validation** | `data_quality_expert.md` |
| **Data Warehouse Design & Modeling** | `data_warehouse_design_expert.md` |
| **Python Performance & Memory Optimization** | `python_data_processing_performance_optimization_expert.md` |
| **Python Dependency & Environment Management** | `python_dependency_management_expert.md` |
| **Testing & Quality Assurance** | `python_test_generation_data_pipelines_expert.md` |
| **Schema Evolution & Migration** | `schema_management_expert.md` |
| **Storage Infrastructure & I/O Optimization** | `storage_infrastructure_expert.md` |

---

## 🎯 Specialized Combinations

For complex data engineering tasks, consider combining multiple personas:

- **New Data Platform Design**: `data_lake_design_expert.md` + `data_warehouse_design_expert.md` + `data_lineage_metadata_expert.md`
- **High-Performance ETL Pipeline**: `etl_pipeline_design_expert.md` + `python_data_processing_performance_optimization_expert.md` + `batch_processing_optimization_expert.md`
- **Production Data System**: `data_pipeline_monitoring_expert.md` + `data_quality_expert.md` + `data_observability_expert.md`
- **Storage & Performance Optimization**: `storage_infrastructure_expert.md` + `columnar_storage_performance_expert.md` + `data_partitioning_strategy_expert.md`
- **Data Integration & Quality**: `api_integration_expert.md` + `data_quality_expert.md` + `schema_management_expert.md`

---

## 🛠️ Update Instructions

After adding new personas to this folder, rerun `create_router.md` to regenerate this file.

---

## Notes

- Each persona specializes in specific aspects of data engineering with deep domain expertise
- Consider the primary focus area and secondary concerns when selecting personas
- For complex projects, multiple personas can provide comprehensive coverage
- All personas follow the established engineering persona specification format 