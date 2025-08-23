# Code Generation Context Prompt

## Purpose
Provide comprehensive context to AI agents before they generate code, ensuring the output follows your project's established patterns, architecture, and constraints.

## When to Use
- Before asking an AI to write new code
- When onboarding an AI to your project
- Before implementing new features or modules
- When refactoring existing code

## Context Template

### 1. Project Overview
```
Project Name: [Project Name]
Project Type: [Web App, API, Library, etc.]
Primary Language: [Python, TypeScript, etc.]
Framework: [Django, FastAPI, React, etc.]
Architecture Pattern: [MVC, Clean Architecture, Microservices, etc.]
```

### 2. Technical Stack & Dependencies
```
Core Technologies:
- Backend: [List main backend technologies]
- Frontend: [List main frontend technologies]
- Database: [List databases and ORMs]
- Caching: [List caching solutions]
- Message Queues: [List queue systems]
- Infrastructure: [List deployment/infra tools]

Key Dependencies:
- [List critical third-party packages with versions]
- [Note any specific version constraints]
- [List internal packages/modules this code will depend on]
```

### 3. Code Organization & Patterns
```
Project Structure:
[Describe the main directory structure and organization]

Naming Conventions:
- Files: [e.g., snake_case, kebab-case]
- Functions: [e.g., snake_case, camelCase]
- Classes: [e.g., PascalCase]
- Constants: [e.g., UPPER_SNAKE_CASE]
- Variables: [e.g., snake_case]

Code Patterns:
- Error Handling: [How errors are handled and logged]
- Logging: [Logging patterns and levels]
- Configuration: [How config is managed]
- Testing: [Testing framework and patterns]
- Documentation: [Documentation standards]
```

### 4. Architecture Constraints & Decisions
```
Performance Requirements:
- [Response time limits, throughput requirements]
- [Memory/CPU constraints]
- [Scalability considerations]

Security Requirements:
- [Authentication/authorization patterns]
- [Data validation requirements]
- [Input sanitization needs]

Integration Points:
- [APIs this code will interact with]
- [Database schemas and relationships]
- [External service dependencies]
- [Event/message patterns]
```

### 5. Existing Code Examples
```
Similar Patterns:
[Provide 2-3 examples of similar functionality in your codebase]

Key Classes/Modules:
[Reference the main classes/modules this code should integrate with]

Database Models:
[Show relevant database schemas or model definitions]
```

### 6. Specific Requirements
```
Functional Requirements:
- [What the code should do]
- [Input/output specifications]
- [Business logic requirements]

Non-Functional Requirements:
- [Performance benchmarks]
- [Error handling scenarios]
- [Edge cases to consider]
- [Testing requirements]
```

### 7. Constraints & Limitations
```
Technical Constraints:
- [Version compatibility requirements]
- [Platform limitations]
- [Resource constraints]

Business Constraints:
- [Compliance requirements]
- [Audit trail needs]
- [Data retention policies]
```

## Usage Instructions

1. **Fill out the context template** with your project's specific details
2. **Provide concrete examples** from your existing codebase
3. **Specify the exact functionality** you want implemented
4. **Include any specific patterns** you want followed or avoided
5. **Reference existing code** that the new code should be consistent with

## Example Context

```
Project Name: E-commerce API
Project Type: REST API
Primary Language: Python
Framework: FastAPI
Architecture Pattern: Clean Architecture

Core Technologies:
- Backend: FastAPI, SQLAlchemy, PostgreSQL
- Caching: Redis
- Message Queues: Celery + RabbitMQ
- Infrastructure: Docker, AWS

Code Patterns:
- Error Handling: Custom exception classes with structured logging
- Logging: Structured JSON logging with correlation IDs
- Testing: pytest with factory_boy for test data
- Documentation: OpenAPI/Swagger with detailed docstrings

Similar Patterns:
- See `services/product_service.py` for service layer pattern
- See `models/order.py` for database model pattern
- See `api/v1/orders.py` for endpoint pattern

Specific Requirements:
- Create a new inventory management service
- Must integrate with existing product and warehouse models
- Should handle concurrent inventory updates with optimistic locking
- Must emit events for inventory changes
```

## Tips for Effective Context

- **Be specific** about patterns and conventions
- **Provide real examples** from your codebase
- **Include edge cases** and error scenarios
- **Specify performance requirements** when relevant
- **Reference existing documentation** or architecture decisions
- **Update context** as your project evolves
