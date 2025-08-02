# Persona Creation Workflow

This folder contains the tools and templates for creating specialized AI agent personas. The workflow is designed to systematically create, organize, and route to appropriate personas based on the task at hand.

## 📁 File Overview

### Core Workflow Files

- **`CREATE_ENGINEERING_PERSONA.md`** - The main persona creation agent that orchestrates the entire process
- **`ENGINEERING_PERSONA_SPEC.md`** - The standardized template that all engineering personas must follow
- **`CREATE_AGENT_ROUTER.md`** - Generates routing logic to help select the right persona for a task
- **`CREATE_AGENT_EXAMPLES.md`** - Helper for generating realistic examples that demonstrate persona behavior

## 🔄 Persona Creation Workflow

The persona creation process follows a three-step workflow:

### Step 1: Define Persona Descriptions
Start by defining raw role descriptions that include:
- Focus areas or review categories
- Key skills and capabilities  
- Common issues or failure points they help detect

### Step 2: Create Personas
Use `CREATE_ENGINEERING_PERSONA.md` to transform raw descriptions into complete persona specifications:

1. **Input**: Raw role description
2. **Process**: The agent uses:
   - `ENGINEERING_PERSONA_SPEC.md` as the template structure
   - `CREATE_AGENT_EXAMPLES.md` to generate realistic examples
   - `PREFERRED_TECH_STACK.md` (from parent directory) for technology alignment
3. **Output**: Complete persona markdown file following the standardized spec

### Step 3: Generate Router
Use `CREATE_AGENT_ROUTER.md` to create a `router.md` file that:
- Summarizes all personas in the folder
- Provides routing guidelines for task selection
- Creates a reverse index mapping common tasks to recommended personas

## 📋 File Details

### `CREATE_ENGINEERING_PERSONA.md`
The main orchestrator that:
- Takes raw role descriptions as input
- Populates the `ENGINEERING_PERSONA_SPEC` template
- Generates at least 3 realistic examples using `CREATE_AGENT_EXAMPLES.md`
- Aligns technology references with preferred tech stack
- Outputs a complete, ready-to-use persona specification

### `ENGINEERING_PERSONA_SPEC.md`
The standardized template containing:
- **Frontmatter**: name, description, examples, color, tools
- **Role Summary**: High-level persona overview
- **Focus Areas**: Core domains and concerns
- **Key Skills**: Specific capabilities and operations
- **Code Review Focus**: What issues this persona catches
- **Primary Responsibilities**: Main task areas
- **Technology Stack**: Languages, frameworks, databases, infrastructure
- **Architectural Patterns**: Key methodologies and patterns
- **Best Practices**: Design principles and guidelines
- **Trade-off Awareness**: Context-sensitive decision making

### `CREATE_AGENT_ROUTER.md`
Generates a `router.md` file that provides:
- **Persona Directory**: Summary of each persona with filename, name, focus areas, and example tasks
- **Routing Guidelines**: How to choose the correct persona based on task characteristics
- **Common Tasks Index**: Reverse mapping from task patterns to recommended personas
- **Update Instructions**: How to maintain the router when new personas are added

### `CREATE_AGENT_EXAMPLES.md`
Helper for generating realistic examples that:
- Follow YAML-compatible format
- Include context, user request, assistant response, and commentary
- Demonstrate the persona's expertise and reasoning
- Cover diverse scenarios to show the range of skills

## 🎯 Usage Examples

### Creating a New DevOps Persona
1. Define the role: "Container Security Expert who focuses on Docker vulnerabilities, image scanning, and runtime security"
2. Run `CREATE_ENGINEERING_PERSONA.md` with this description
3. Get a complete persona file like `container_security_expert.md`
4. Run `CREATE_AGENT_ROUTER.md` to update the routing logic

### Finding the Right Persona for a Task
1. Check the `router.md` file in the target persona folder
2. Look for focus area overlap with your task
3. Review example tasks to find the best match
4. If no match exists, consider creating a new persona

## 🔧 Maintenance

- **Adding New Personas**: Follow the three-step workflow above
- **Updating Existing Personas**: Modify the persona file directly, then regenerate the router
- **Technology Stack Changes**: Update `PREFERRED_TECH_STACK.md` in the parent directory
- **Template Evolution**: Modify `ENGINEERING_PERSONA_SPEC.md` and regenerate all personas

## 📚 Related Files

- `../PREFERRED_TECH_STACK.md` - Default technology preferences
- `../engineering/` - Directory containing created engineering personas
- `../personas/` - Root personas directory with various categories

## 🚀 Getting Started

1. **Define your persona concept** - What role, skills, and focus areas?
2. **Use `CREATE_ENGINEERING_PERSONA.md`** - Transform your concept into a complete spec
3. **Generate routing logic** - Use `CREATE_AGENT_ROUTER.md` to make the persona discoverable
4. **Test and iterate** - Refine the persona based on actual usage

This workflow ensures consistent, well-structured personas that can be easily discovered and utilized by the AI agent system. 