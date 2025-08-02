# Execution Directory Overview

This directory contains the canonical guides and processes for executing and completing Linear tickets from initial analysis through implementation to delivery. Use this README to understand the execution workflow and locate the right guide for each phase of ticket implementation.

---

## Execution Workflow Overview

The execution process follows a systematic approach that ensures high-quality, test-driven development while maintaining project continuity and knowledge transfer.

**Execution Phases:**
1. **Pre-Execution**: Analysis, context gathering, and planning
   - `HOW_TO_EXECUTE_A_TICKET.md` (Pre-Execution Phase)
2. **Implementation**: Development, testing, and quality assurance
   - `HOW_TO_EXECUTE_A_TICKET.md` (Implementation Phase)
3. **Completion**: PR creation, review, and handoff
   - `HOW_TO_EXECUTE_A_TICKET.md` (Completion Phase)
   - `CREATE_NEXT_AGENT_PROMPT.md`

---

## File Summaries & Usage

### HOW_TO_EXECUTE_A_TICKET.md
**Purpose:** The master guide that provides a comprehensive, step-by-step approach to executing Linear tickets from initial analysis through implementation to PR creation and completion. This ensures high-quality, test-driven development that follows all established coding standards, project management workflows, and GitHub operations protocols.

**Key Sections:**
- **Pre-Execution Phase**: Ticket analysis, context gathering, dependency validation, and implementation planning
- **Implementation Phase**: Development setup, test-driven development, code implementation, and quality assurance
- **Completion Phase**: PR creation, code review, and project handoff

**References:** Integrates with `GITHUB_OPERATIONS.md`, `CODING_RULES.md`, and `CREATE_NEXT_AGENT_PROMPT.md`.
**When to use:** Use for every ticket implementation to ensure consistent, high-quality execution following established patterns and standards.

### CREATE_NEXT_AGENT_PROMPT.md
**Purpose:** A comprehensive prompt template designed to generate detailed, contextual prompts for the next agent in the workflow. This ensures seamless handoff and maintains project continuity by providing all necessary context, requirements, and implementation details from the current work.

**Key Features:**
- **Project Context Section**: Explicitly instructs the next agent to read the project's README.md for full context
- **Linear Ticket Integration**: Structured to include all relevant Linear ticket details
- **Implementation Context**: Captures what was just completed and the current state of the codebase
- **Conversation Context**: Preserves insights, challenges, and solutions from the current session
- **Clear Task Instructions**: Provides step-by-step guidance for the next agent
- **Success Criteria**: Defines clear completion standards

**References:** Builds upon `HOW_TO_EXECUTE_A_TICKET.md` and integrates with project README.md files.
**When to use:** Use at the end of a ticket implementation to create a comprehensive handoff prompt for the next agent in the workflow.

---

## Quick Start Recommendations

### For New Ticket Implementation
1. **Start with:** `HOW_TO_EXECUTE_A_TICKET.md` to understand the complete execution workflow
2. **Follow the phases:** Pre-Execution → Implementation → Completion
3. **Use handoff prompt:** `CREATE_NEXT_AGENT_PROMPT.md` when finishing a ticket

### For Ticket Handoffs
- **Completing a ticket?** Use `CREATE_NEXT_AGENT_PROMPT.md` to generate the next agent's prompt
- **Receiving a handoff?** Use the generated prompt to understand context and requirements
- **Need project context?** Always reference the project's README.md as instructed in the handoff prompt

### For Quality Assurance
- **Following standards?** Ensure adherence to `CODING_RULES.md` and `GITHUB_OPERATIONS.md`
- **Test coverage?** Follow test-driven development principles outlined in `HOW_TO_EXECUTE_A_TICKET.md`
- **Code review?** Use the completion phase guidelines for PR creation and review

---

## Integration with Other Directories

This execution directory integrates with other task instruction directories:

- **Project Management Directory:** References `GITHUB_OPERATIONS.md` and project planning workflows
- **Rules Directory:** Follows `CODING_RULES.md`, `UI_RULES.md`, and repository conventions
- **Engineering Directory:** Connects to technical implementation and architecture guidelines
- **Personas Directory:** May reference specific agent personas for specialized tasks

### Cross-Reference Dependencies

When executing tickets, always ensure you are following all relevant standards:

- **GitHub Operations:** Reference `GITHUB_OPERATIONS.md` for branching, PRs, and Linear integration
- **Coding Standards:** Follow `CODING_RULES.md` for code quality, testing, and documentation
- **Project Context:** Read the project's README.md for architecture, conventions, and setup
- **Quality Standards:** Use `WHAT_MAKES_A_GREAT_TICKET.md` to validate ticket completion

---

## Best Practices for Execution

### Pre-Execution Phase
1. **Thorough Analysis**: Always retrieve complete Linear ticket details using Linear MCP
2. **Context Gathering**: Review related PRs, project planning documents, and codebase state
3. **Dependency Validation**: Ensure all blocking tickets are resolved before starting
4. **Implementation Planning**: Break down complex tickets into logical, testable steps

### Implementation Phase
1. **Test-Driven Development**: Write tests before implementation following established patterns
2. **Code Quality**: Follow project conventions and coding standards consistently
3. **Documentation**: Update documentation as needed during implementation
4. **Quality Assurance**: Run all tests and ensure code review readiness

### Completion Phase
1. **PR Creation**: Follow GitHub operations guidelines for proper PR structure
2. **Code Review**: Ensure all requirements are met and code is ready for review
3. **Knowledge Transfer**: Use `CREATE_NEXT_AGENT_PROMPT.md` for comprehensive handoff
4. **Project Continuity**: Maintain consistency with established patterns and decisions

### Handoff Process
1. **Context Preservation**: Document all relevant implementation details and decisions
2. **State Documentation**: Capture current codebase state, dependencies, and environment changes
3. **Challenge Documentation**: Note any issues, workarounds, or considerations for the next agent
4. **Clear Instructions**: Provide specific guidance and success criteria for the next ticket

---

## Quality Assurance Checklist

Before completing any ticket execution, ensure:

- [ ] All ticket requirements are fully implemented
- [ ] Code follows project conventions and established patterns
- [ ] All tests pass with appropriate coverage
- [ ] Documentation is updated if required
- [ ] PR is ready with clear commit messages
- [ ] Dependencies and environment changes are documented
- [ ] Handoff prompt is generated for the next agent
- [ ] Project README.md context is referenced
- [ ] All coding standards and rules are followed
- [ ] GitHub operations guidelines are adhered to

This execution directory ensures that every ticket implementation maintains high quality, consistency, and project continuity while facilitating seamless knowledge transfer between agents.
