# 🧭 Agent Persona Router

This folder contains specialized AI agents designed to assist with various DevOps tool-specific tasks across infrastructure automation, monitoring, security, performance optimization, and container orchestration.

Use this file to decide which agent persona is best suited for a task or review. If no persona is a good fit, consider creating a new one using `create_persona.md`.

---

## 🧠 Persona Directory

### `terraform_iac_expert.md`
- **Name**: Terraform Infrastructure as Code Expert
- **Summary**: Specializes in designing, implementing, and managing infrastructure using Terraform with focus on automation, state management, and infrastructure testing
- **Focus Areas**: Terraform modules, state management, configuration drift, infrastructure testing, CI/CD integration, multi-environment management, security compliance
- **Example Tasks**:
  - Migrating from manual infrastructure to Terraform automation
  - Fixing configuration drift and infrastructure inconsistencies
  - Implementing infrastructure testing and validation strategies

### `redis_monitoring_expert.md`
- **Name**: Redis Monitoring Specialist
- **Summary**: Specializes in Redis performance monitoring, optimization, and troubleshooting with focus on memory management and connection pool optimization
- **Focus Areas**: Redis performance monitoring, memory optimization, connection pools, persistence monitoring, cluster health, security hardening, backup strategies
- **Example Tasks**:
  - Diagnosing Redis memory issues and slow performance
  - Setting up comprehensive Redis monitoring for production environments
  - Fixing connection pool exhaustion and cluster performance issues

### `prometheus_metrics_design_expert.md`
- **Name**: Prometheus Metrics Design Expert
- **Summary**: Specializes in designing efficient, scalable metrics collection systems using Prometheus with focus on query optimization and cardinality management
- **Focus Areas**: PromQL optimization, cardinality management, custom metrics, recording rules, alerting rules, configuration optimization, monitoring architecture
- **Example Tasks**:
  - Optimizing slow Prometheus queries and high cardinality issues
  - Designing custom metrics for business KPIs and application performance
  - Optimizing Prometheus configuration and alerting rules

### `hetzner_cloud_infrastructure_expert.md`
- **Name**: Hetzner Cloud Infrastructure Expert
- **Summary**: Specializes in designing, implementing, and optimizing infrastructure solutions on Hetzner Cloud platform with focus on cost optimization and performance
- **Focus Areas**: VM optimization, networking configuration, storage management, cost optimization, high availability, disaster recovery, monitoring
- **Example Tasks**:
  - Setting up cost-effective infrastructure for web applications
  - Optimizing VM performance and storage configuration
  - Implementing secure networking and firewall rules

### `grafana_dashboard_design_expert.md`
- **Name**: Grafana Dashboard Design Specialist
- **Summary**: Specializes in creating intuitive, performant, and actionable Grafana dashboards with focus on user experience and visualization optimization
- **Focus Areas**: Dashboard layout, visualization design, template variables, performance optimization, alert visualization, user experience, data query optimization
- **Example Tasks**:
  - Creating comprehensive monitoring dashboards for microservices
  - Optimizing slow dashboard load times and poor user experience
  - Designing business-focused dashboards with KPI visualizations

### `docker_security_expert.md`
- **Name**: Docker Security Specialist
- **Summary**: Specializes in container security hardening, vulnerability assessment, and runtime protection with focus on defense-in-depth strategies
- **Focus Areas**: Vulnerability assessment, runtime monitoring, image signing, container hardening, escape prevention, secure builds, compliance auditing
- **Example Tasks**:
  - Scanning Docker images for vulnerabilities before deployment
  - Hardening Redis containers running with excessive privileges
  - Implementing secure multi-stage builds with image signing

### `docker_performance_expert.md`
- **Name**: Docker Performance Optimization Expert
- **Summary**: Specializes in container performance optimization, build efficiency, and resource utilization with focus on identifying and resolving bottlenecks
- **Focus Areas**: Performance optimization, build cache, resource utilization, multi-architecture builds, startup time optimization, memory efficiency, network performance
- **Example Tasks**:
  - Optimizing slow Docker builds and large image sizes
  - Profiling Redis container resource consumption and optimization
  - Reducing container startup time for auto-scaling requirements

### `docker_compose_orchestration_expert.md`
- **Name**: Docker Compose Orchestration Specialist
- **Summary**: Expert in multi-service container orchestration, networking, and service integration using Docker Compose for development and production environments
- **Focus Areas**: Multi-service orchestration, container networking, service discovery, volume management, environment configuration, health checks, resource allocation
- **Example Tasks**:
  - Troubleshooting service communication issues in Docker Compose
  - Setting up health checks and service dependencies for microservices
  - Managing environment variables across different deployment environments

### `railway_deployment_expert.md`
- **Name**: Railway Deployment Specialist
- **Summary**: Specializes in Railway platform optimization, deployment strategies, scaling solutions, and production deployment workflows with focus on cost-effective, reliable deployments
- **Focus Areas**: Railway service configuration, environment management, scaling strategies, cost optimization, monitoring and logging, CI/CD integration, performance tuning
- **Example Tasks**:
  - Setting up Railway deployment with proper environment management and auto-scaling
  - Optimizing Railway performance and reducing deployment costs
  - Implementing zero-downtime deployments with automatic rollback capabilities

---

## 📌 Routing Guidelines

To determine which persona to use:

1. **Look for focus area overlap** between the task and the persona's expertise
2. **Check if the task resembles any of the example tasks** listed for each persona
3. **Consider the primary technology or tool** involved in your task:
   - **Terraform**: Use `terraform_iac_expert.md`
   - **Redis**: Use `redis_monitoring_expert.md`
   - **Prometheus**: Use `prometheus_metrics_design_expert.md`
   - **Hetzner Cloud**: Use `hetzner_cloud_infrastructure_expert.md`
   - **Grafana**: Use `grafana_dashboard_design_expert.md`
   - **Docker Security**: Use `docker_security_expert.md`
   - **Docker Performance**: Use `docker_performance_expert.md`
   - **Docker Compose**: Use `docker_compose_orchestration_expert.md`
   - **Railway**: Use `railway_deployment_expert.md`
4. **If the task requires multiple domains**, select multiple personas
5. **If no persona matches**, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| Infrastructure automation and provisioning | `terraform_iac_expert.md` |
| Redis performance issues and monitoring | `redis_monitoring_expert.md` |
| Prometheus query optimization and metrics design | `prometheus_metrics_design_expert.md` |
| Hetzner Cloud infrastructure setup and optimization | `hetzner_cloud_infrastructure_expert.md` |
| Grafana dashboard creation and optimization | `grafana_dashboard_design_expert.md` |
| Docker container security scanning and hardening | `docker_security_expert.md` |
| Docker build performance and resource optimization | `docker_performance_expert.md` |
| Multi-service container orchestration with Docker Compose | `docker_compose_orchestration_expert.md` |
| Railway deployment setup and optimization | `railway_deployment_expert.md` |
| Container vulnerability assessment | `docker_security_expert.md` |
| Infrastructure monitoring and alerting setup | `prometheus_metrics_design_expert.md`, `grafana_dashboard_design_expert.md` |
| Cloud infrastructure cost optimization | `hetzner_cloud_infrastructure_expert.md`, `railway_deployment_expert.md` |
| Container networking and service discovery | `docker_compose_orchestration_expert.md` |
| Infrastructure testing and validation | `terraform_iac_expert.md` |
| Redis cluster management and optimization | `redis_monitoring_expert.md` |
| Monitoring dashboard performance issues | `grafana_dashboard_design_expert.md` |
| Docker image optimization and build efficiency | `docker_performance_expert.md` |
| Infrastructure security compliance | `docker_security_expert.md`, `terraform_iac_expert.md` |
| Railway performance optimization and cost reduction | `railway_deployment_expert.md` |
| Zero-downtime deployment strategies | `railway_deployment_expert.md`, `docker_compose_orchestration_expert.md` |

---

## 🛠️ Update Instructions

After adding new personas to this folder, rerun `create_router.md` to regenerate this file.

---

## Notes

- Each persona specializes in specific DevOps tools and technologies
- Consider combining personas for complex tasks involving multiple tools
- All personas follow the engineering persona specification format
- Focus on the primary technology or tool when selecting a persona