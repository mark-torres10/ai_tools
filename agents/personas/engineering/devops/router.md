# 🧭 DevOps Agent Persona Router

This folder contains specialized AI agents designed to assist with various DevOps and Site Reliability Engineering (SRE) tasks across infrastructure automation, monitoring, security, performance optimization, container orchestration, and operational excellence.

Use this file to decide which agent persona is best suited for a task or review. The personas are organized into specialized categories, each with their own detailed routing logic.

---

## 📁 Persona Categories

### 🔧 **Task-Specific Personas** (`task_specific/`)
Specialized agents focused on specific operational domains:
- **SRE Incident Response Expert** - Incident management, alerting, on-call procedures
- **SRE Performance Engineering Expert** - Performance optimization, load testing, capacity planning
- **SRE Reliability Engineering Expert** - Fault tolerance, disaster recovery, chaos engineering
- **CI/CD Pipeline Expert** - Automated deployment, testing integration, release management
- **Network Security Expert** - Network security, firewall configuration, traffic analysis
- **Container Security Expert** - Container security, image scanning, runtime protection

### 🛠️ **Tool-Specific Personas** (`tool_specific/`)
Technology-focused agents for specific DevOps tools:
- **Terraform Infrastructure as Code Expert** - Infrastructure automation and state management
- **Redis Monitoring Specialist** - Redis performance monitoring and optimization
- **Prometheus Metrics Design Expert** - Metrics collection and monitoring systems
- **Hetzner Cloud Infrastructure Expert** - Cloud infrastructure design and optimization
- **Grafana Dashboard Design Specialist** - Monitoring dashboard creation and optimization
- **Docker Security Specialist** - Container security hardening and vulnerability assessment
- **Docker Performance Optimization Expert** - Container performance and build optimization
- **Docker Compose Orchestration Specialist** - Multi-service container orchestration

### 🎯 **Generic Personas** (`generic/`)
General-purpose DevOps agents:
- **DevOps Engineer** - Docker, containerization, production deployment

---

## 🧠 Persona Directory

### Task-Specific Personas

#### `task_specific/sre_incident_response_expert.md`
- **Name**: SRE Incident Response Expert
- **Summary**: Specializes in incident management, alerting systems, on-call procedures, and post-incident analysis
- **Focus Areas**: incident management, alert fatigue, on-call procedures, post-incident analysis, runbook automation
- **Example Tasks**: Implement incident management frameworks, design intelligent alerting systems, set up on-call rotations

#### `task_specific/sre_performance_engineering_expert.md`
- **Name**: SRE Performance Engineering Expert
- **Summary**: Specializes in system performance optimization, load testing, capacity planning, and bottleneck identification
- **Focus Areas**: performance analysis, load testing, capacity planning, bottleneck identification, scalability testing
- **Example Tasks**: Conduct performance profiling, design load testing scenarios, implement performance monitoring

#### `task_specific/sre_reliability_engineering_expert.md`
- **Name**: SRE Reliability Engineering Expert
- **Summary**: Specializes in system reliability, fault tolerance, disaster recovery, and resilience engineering
- **Focus Areas**: fault tolerance, circuit breakers, disaster recovery, chaos engineering, high availability
- **Example Tasks**: Implement circuit breaker patterns, design disaster recovery strategies, set up chaos engineering

#### `task_specific/cicd_expert.md`
- **Name**: CI/CD Pipeline Expert
- **Summary**: Specializes in automated deployment, testing integration, release management, and pipeline optimization
- **Focus Areas**: pipeline design, automated testing, release management, deployment strategies, quality gates
- **Example Tasks**: Design CI/CD pipelines, implement automated testing frameworks, configure deployment strategies

#### `task_specific/network_security_expert.md`
- **Name**: Network Security Expert
- **Summary**: Specializes in network security, firewall configuration, traffic analysis, and infrastructure protection
- **Focus Areas**: network security architecture, firewall management, traffic analysis, VPN infrastructure, DDoS protection
- **Example Tasks**: Design secure network topologies, implement DDoS protection, configure VPN solutions

#### `task_specific/container_security_expert.md`
- **Name**: Container Security Expert
- **Summary**: Specializes in container security, image scanning, runtime protection, and security policy enforcement
- **Focus Areas**: vulnerability scanning, runtime security, image signing, container hardening, security policies
- **Example Tasks**: Conduct vulnerability scans, implement runtime security monitoring, set up image signing

### Tool-Specific Personas

#### `tool_specific/terraform_iac_expert.md`
- **Name**: Terraform Infrastructure as Code Expert
- **Summary**: Specializes in designing, implementing, and managing infrastructure using Terraform
- **Focus Areas**: Terraform modules, state management, configuration drift, infrastructure testing, CI/CD integration
- **Example Tasks**: Migrate to Terraform automation, fix configuration drift, implement infrastructure testing

#### `tool_specific/redis_monitoring_expert.md`
- **Name**: Redis Monitoring Specialist
- **Summary**: Specializes in Redis performance monitoring, optimization, and troubleshooting
- **Focus Areas**: Redis performance monitoring, memory optimization, connection pools, persistence monitoring
- **Example Tasks**: Diagnose Redis memory issues, set up Redis monitoring, fix connection pool exhaustion

#### `tool_specific/prometheus_metrics_design_expert.md`
- **Name**: Prometheus Metrics Design Expert
- **Summary**: Specializes in designing efficient, scalable metrics collection systems using Prometheus
- **Focus Areas**: PromQL optimization, cardinality management, custom metrics, recording rules, alerting rules
- **Example Tasks**: Optimize slow Prometheus queries, design custom metrics, optimize alerting rules

#### `tool_specific/hetzner_cloud_infrastructure_expert.md`
- **Name**: Hetzner Cloud Infrastructure Expert
- **Summary**: Specializes in designing, implementing, and optimizing infrastructure solutions on Hetzner Cloud
- **Focus Areas**: VM optimization, networking configuration, storage management, cost optimization, high availability
- **Example Tasks**: Set up cost-effective infrastructure, optimize VM performance, implement secure networking

#### `tool_specific/grafana_dashboard_design_expert.md`
- **Name**: Grafana Dashboard Design Specialist
- **Summary**: Specializes in creating intuitive, performant, and actionable Grafana dashboards
- **Focus Areas**: Dashboard layout, visualization design, template variables, performance optimization, alert visualization
- **Example Tasks**: Create monitoring dashboards, optimize dashboard performance, design KPI visualizations

#### `tool_specific/docker_security_expert.md`
- **Name**: Docker Security Specialist
- **Summary**: Specializes in container security hardening, vulnerability assessment, and runtime protection
- **Focus Areas**: Vulnerability assessment, runtime monitoring, image signing, container hardening, escape prevention
- **Example Tasks**: Scan Docker images for vulnerabilities, harden containers, implement secure builds

#### `tool_specific/docker_performance_expert.md`
- **Name**: Docker Performance Optimization Expert
- **Summary**: Specializes in container performance optimization, build efficiency, and resource utilization
- **Focus Areas**: Performance optimization, build cache, resource utilization, multi-architecture builds, startup time
- **Example Tasks**: Optimize slow Docker builds, profile container resource consumption, reduce startup time

#### `tool_specific/docker_compose_orchestration_expert.md`
- **Name**: Docker Compose Orchestration Specialist
- **Summary**: Expert in multi-service container orchestration, networking, and service integration
- **Focus Areas**: Multi-service orchestration, container networking, service discovery, volume management, health checks
- **Example Tasks**: Troubleshoot service communication, set up health checks, manage environment variables

### Generic Personas

#### `generic/devops_engineer.md`
- **Name**: DevOps Engineer
- **Summary**: General-purpose DevOps engineer specializing in Docker, containerization, and production deployment
- **Focus Areas**: Docker, Docker Compose, container orchestration, infrastructure as code, production deployment
- **Example Tasks**: Container security, resource optimization, deployment best practices

---

## 📌 Routing Guidelines

To determine which persona to use:

### 1. **Identify the Primary Category**
- **Operational Tasks** (incidents, performance, reliability) → Task-Specific Personas
- **Technology-Specific Tasks** (Terraform, Redis, Docker, etc.) → Tool-Specific Personas
- **General DevOps Tasks** → Generic Personas

### 2. **Match Task Characteristics**
- **Incidents & Alerts** → SRE Incident Response Expert
- **Performance & Scalability** → SRE Performance Engineering Expert
- **Reliability & Resilience** → SRE Reliability Engineering Expert
- **Deployment & Pipelines** → CI/CD Pipeline Expert
- **Network Security** → Network Security Expert
- **Container Security** → Container Security Expert
- **Specific Tools** → Corresponding Tool-Specific Expert
- **General Container/Deployment** → DevOps Engineer

### 3. **Consider Complexity**
- **Simple, tool-specific tasks** → Use the relevant Tool-Specific persona
- **Complex operational tasks** → Use the relevant Task-Specific persona
- **General DevOps guidance** → Use DevOps Engineer
- **Multi-domain tasks** → Consider multiple personas or the most relevant primary persona

### 4. **If No Match Found**
Return: **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| Incident response and alert management | `task_specific/sre_incident_response_expert.md` |
| Performance optimization and load testing | `task_specific/sre_performance_engineering_expert.md` |
| System reliability and fault tolerance | `task_specific/sre_reliability_engineering_expert.md` |
| CI/CD pipeline setup and optimization | `task_specific/cicd_expert.md` |
| Network security and firewall configuration | `task_specific/network_security_expert.md` |
| Container security and vulnerability scanning | `task_specific/container_security_expert.md` |
| Terraform infrastructure automation | `tool_specific/terraform_iac_expert.md` |
| Redis performance and monitoring | `tool_specific/redis_monitoring_expert.md` |
| Prometheus metrics and monitoring | `tool_specific/prometheus_metrics_design_expert.md` |
| Hetzner Cloud infrastructure | `tool_specific/hetzner_cloud_infrastructure_expert.md` |
| Grafana dashboard design | `tool_specific/grafana_dashboard_design_expert.md` |
| Docker security hardening | `tool_specific/docker_security_expert.md` |
| Docker performance optimization | `tool_specific/docker_performance_expert.md` |
| Docker Compose orchestration | `tool_specific/docker_compose_orchestration_expert.md` |
| General container and deployment tasks | `generic/devops_engineer.md` |
| Multi-tool infrastructure projects | Multiple relevant personas |
| DevOps strategy and best practices | `generic/devops_engineer.md` |

---

## 📚 Detailed Routing References

For more detailed routing logic within each category, refer to:
- **Task-Specific Routing**: `task_specific/router.md`
- **Tool-Specific Routing**: `tool_specific/router.md`

---

## 🛠️ Update Instructions

After adding new personas to any subdirectory:
1. Update the relevant subdirectory router (`task_specific/router.md` or `tool_specific/router.md`)
2. Update this main router to include the new persona
3. Regenerate routing tables and guidelines

---

## Notes

- Each persona specializes in specific DevOps domains with deep expertise in their respective areas
- Many complex tasks may benefit from multiple personas working together
- All personas follow the engineering persona specification and are designed for practical, production-ready implementations
- Consider the stage of your project (MVP, Growth, Enterprise) when selecting personas
- For comprehensive solutions, consider combining task-specific and tool-specific personas 