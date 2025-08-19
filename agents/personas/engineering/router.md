# 🧭 Engineering Agent Persona Router

This folder contains specialized AI agents designed to assist with various engineering tasks across backend development, data engineering, DevOps, frontend development, machine learning, and system architecture.

Use this file to decide which agent persona is best suited for a task or review. If no persona is a good fit, consider creating a new one using the persona creation templates.

---

## 🧠 Persona Directory

### `backend/`
- **Name**: Backend Development
- **Summary**: Specializes in backend system design, API development, and infrastructure architecture
- **Focus Areas**: system architecture, API design, database design, performance optimization
- **Example Tasks**:
  - Designing scalable backend services with FastAPI
  - Implementing authentication and authorization systems
  - Optimizing database queries and API performance

### `data_engineering/`
- **Name**: Data Engineering
- **Summary**: Specializes in data pipelines, ETL processes, and data infrastructure
- **Focus Areas**: ETL pipelines, data warehousing, real-time analytics, data quality
- **Example Tasks**:
  - Building real-time data processing pipelines
  - Designing data warehouse architectures
  - Implementing data quality monitoring systems

### `devops/`
- **Name**: DevOps & Infrastructure
- **Summary**: Specializes in CI/CD, infrastructure automation, and operational excellence
- **Focus Areas**: CI/CD pipelines, infrastructure as code, monitoring, security
- **Example Tasks**:
  - Setting up automated deployment pipelines
  - Implementing infrastructure monitoring and alerting
  - Optimizing container orchestration and security

### `frontend/`
- **Name**: Frontend Development
- **Summary**: Specializes in user interface design, component architecture, and frontend performance
- **Focus Areas**: UI/UX design, component architecture, performance optimization, accessibility
- **Example Tasks**:
  - Building responsive component libraries
  - Optimizing frontend performance and user experience
  - Implementing accessibility features and testing

### `machine_learning/`
- **Name**: Machine Learning
- **Summary**: Specializes in ML model development, evaluation, and optimization
- **Focus Areas**: algorithm selection, model evaluation, feature engineering, interpretability
- **Example Tasks**:
  - Building and optimizing classification models
  - Implementing model interpretability with SHAP and LIME
  - Designing validation strategies and monitoring systems

### `system_architect/`
- **Name**: System Architecture
- **Summary**: Specializes in high-level system design and architectural decision-making
- **Focus Areas**: system design, scalability, integration, technology selection
- **Example Tasks**:
  - Designing distributed system architectures
  - Making technology stack decisions
  - Planning system integration strategies

### Individual Personas
- **`ai_engineer.md`**: AI and machine learning system development
- **`frontend_developer.md`**: Frontend development and UI/UX optimization
- **`rapid_prototyper.md`**: Quick prototyping and MVP development

---

## 📌 Routing Guidelines

To determine which persona to use:

1. **Identify the primary domain** of your task:
   - **Backend/API work** → `backend/` personas
   - **Data processing/pipelines** → `data_engineering/` personas
   - **Infrastructure/operations** → `devops/` personas
   - **User interface/frontend** → `frontend/` personas
   - **ML model development** → `machine_learning/` personas
   - **System design decisions** → `system_architect/` personas

2. **Check the specific subdomain router** for detailed persona selection within that domain

3. **For cross-domain tasks**, consider using multiple personas or the general engineering personas

4. **If no persona matches**, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Agent(s) |
|--------------|-------------------|
| API development and backend services | `backend/` personas |
| Data pipeline design and ETL processes | `data_engineering/` personas |
| CI/CD setup and infrastructure automation | `devops/` personas |
| User interface and frontend optimization | `frontend/` personas |
| Machine learning model development | `machine_learning/` personas |
| System architecture and design decisions | `system_architect/` personas |
| Cross-domain system integration | Multiple relevant personas |
| Quick prototyping and MVP development | `rapid_prototyper.md` |
| AI system development | `ai_engineer.md` |

---

## 🛠️ Subdomain Routers

For detailed persona selection within each domain, refer to these specialized routers:

- **[Backend Router](backend/router.md)** - Backend development and API design
- **[Data Engineering Router](data_engineering/router.md)** - Data pipelines and analytics
- **[DevOps Router](devops/router.md)** - Infrastructure and operations
- **[Frontend Router](frontend/router.md)** - User interface and frontend development
- **[Machine Learning Router](machine_learning/router.md)** - ML model development and optimization

---

## 🛠️ Update Instructions

After adding new personas to any subdomain folder, update the corresponding subdomain router. For new subdomains, add them to this main router.

---

## Notes

- Each subdomain has its own specialized router with detailed persona information
- General engineering personas are available for cross-domain or general tasks
- Consider combining multiple personas for complex, multi-domain projects
- The system is designed to be extensible - new domains and personas can be added as needed
