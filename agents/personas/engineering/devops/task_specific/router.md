# 🧭 Agent Persona Router

This folder contains specialized AI agents designed to assist with various DevOps and SRE tasks across incident response, performance engineering, reliability engineering, CI/CD pipelines, network security, and container security.

Use this file to decide which agent persona is best suited for a task or review. If no persona is a good fit, consider creating a new one using `create_persona.md`.

---

## 🧠 Persona Directory

### `sre_incident_response_expert.md`
- **Name**: SRE Incident Response Expert
- **Summary**: Specializes in incident management, alerting systems, on-call procedures, and post-incident analysis for maintaining system reliability
- **Focus Areas**: incident management, alert fatigue, on-call procedures, post-incident analysis, runbook automation, incident communication
- **Example Tasks**:
  - Implement comprehensive incident management frameworks with severity classification and SLAs
  - Design intelligent alerting systems to reduce alert fatigue and improve response times
  - Set up on-call rotations with proper escalation procedures and communication protocols

### `sre_performance_engineering_expert.md`
- **Name**: SRE Performance Engineering Expert
- **Summary**: Specializes in system performance optimization, load testing, capacity planning, and performance bottleneck identification for scalable applications
- **Focus Areas**: performance analysis, load testing, capacity planning, bottleneck identification, scalability testing, performance monitoring
- **Example Tasks**:
  - Conduct comprehensive performance profiling and identify system bottlenecks
  - Design and execute load testing scenarios to validate system capacity
  - Implement performance monitoring and alerting based on SLOs and SLIs

### `sre_reliability_engineering_expert.md`
- **Name**: SRE Reliability Engineering Expert
- **Summary**: Specializes in system reliability, fault tolerance, disaster recovery, and resilience engineering for high-availability applications
- **Focus Areas**: fault tolerance, circuit breakers, disaster recovery, chaos engineering, high availability, resilience testing
- **Example Tasks**:
  - Implement circuit breaker patterns and retry mechanisms to prevent cascading failures
  - Design comprehensive disaster recovery strategies with automated failover procedures
  - Set up chaos engineering programs to proactively test system resilience

### `cicd_expert.md`
- **Name**: CI/CD Pipeline Expert
- **Summary**: Specializes in automated deployment, testing integration, release management, and continuous delivery pipeline optimization
- **Focus Areas**: pipeline design, automated testing, release management, deployment strategies, pipeline optimization, quality gates
- **Example Tasks**:
  - Design comprehensive CI/CD pipelines with proper testing and deployment stages
  - Implement automated testing frameworks and quality gates for code quality assurance
  - Configure deployment strategies with safety mechanisms and automated rollback procedures

### `network_security_expert.md`
- **Name**: Network Security Expert
- **Summary**: Specializes in network security, firewall configuration, traffic analysis, and network infrastructure protection for distributed systems
- **Focus Areas**: network security architecture, firewall management, traffic analysis, VPN infrastructure, DDoS protection, network segmentation
- **Example Tasks**:
  - Design secure network topologies with proper segmentation and access controls
  - Implement DDoS protection strategies with multi-layered defense mechanisms
  - Configure VPN solutions and secure remote access with multi-factor authentication

### `container_security_expert.md`
- **Name**: Container Security Expert
- **Summary**: Specializes in container security, image scanning, runtime protection, and security policy enforcement for containerized applications
- **Focus Areas**: vulnerability scanning, runtime security, image signing, container hardening, security policies, supply chain security
- **Example Tasks**:
  - Conduct comprehensive vulnerability scans of container images and dependencies
  - Implement runtime security monitoring and threat detection for containers
  - Set up image signing and verification workflows for supply chain security

### `network_infrastructure_expert.md`
- **Name**: Network Infrastructure Expert
- **Summary**: Specializes in network infrastructure design, routing, load balancing, and network performance optimization for distributed systems
- **Focus Areas**: network infrastructure design, routing protocols, load balancing, network performance optimization, container networking, high-availability networking
- **Example Tasks**:
  - Design scalable network architectures for microservices with container networking solutions
  - Implement high-availability networking with redundant paths and automatic failover
  - Optimize network performance for global users with CDN strategies and edge locations

---

## 📌 Routing Guidelines

To determine which persona to use:

1. **Look for focus area overlap** between the task and the persona's expertise domains
2. **Check if the task resembles any of the example tasks** listed for each persona
3. **Consider the primary concern** of your task:
   - **Incidents & Alerts** → SRE Incident Response Expert
   - **Performance & Scalability** → SRE Performance Engineering Expert
   - **Reliability & Resilience** → SRE Reliability Engineering Expert
   - **Deployment & Pipelines** → CI/CD Pipeline Expert
   - **Network Security** → Network Security Expert
   - **Container Security** → Container Security Expert
4. **If the task requires multiple domains**, select multiple personas or the most relevant primary persona
5. **If no persona matches**, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| Alert fatigue, incident response, on-call procedures | `sre_incident_response_expert.md` |
| Performance bottlenecks, load testing, capacity planning | `sre_performance_engineering_expert.md` |
| Fault tolerance, disaster recovery, chaos engineering | `sre_reliability_engineering_expert.md` |
| CI/CD pipeline setup, automated testing, deployment strategies | `cicd_expert.md` |
| Network security, firewall configuration, DDoS protection | `network_security_expert.md` |
| Network infrastructure, load balancing, performance optimization | `network_infrastructure_expert.md` |
| Container vulnerabilities, image scanning, runtime security | `container_security_expert.md` |
| System reliability and high availability | `sre_reliability_engineering_expert.md`, `sre_incident_response_expert.md` |
| Security compliance and policy enforcement | `container_security_expert.md`, `network_security_expert.md` |
| Network performance and infrastructure optimization | `network_infrastructure_expert.md`, `sre_performance_engineering_expert.md` |
| Monitoring and observability setup | `sre_performance_engineering_expert.md`, `sre_incident_response_expert.md` |
| Infrastructure automation and deployment | `cicd_expert.md`, `sre_reliability_engineering_expert.md` |

---

## 🛠️ Update Instructions

After adding new personas to this folder, rerun `create_router.md` to regenerate this file.

---

## Notes

- Each persona specializes in specific DevOps and SRE domains with deep expertise in their respective areas
- Many tasks may benefit from multiple personas working together for comprehensive solutions
- All personas follow the engineering persona specification and are designed for practical, production-ready implementations
- Consider the stage of your project (MVP, Growth, Enterprise) when selecting personas, as they provide context-aware recommendations
