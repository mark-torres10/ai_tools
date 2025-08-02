# 🤖 Create Next Agent Prompt

This prompt is designed to generate a comprehensive prompt for the next agent in the workflow, incorporating the current Linear ticket context and any relevant information from the current conversation.

---

## 🎯 Purpose

When you reach the end of a ticket implementation, use this prompt to create a detailed, contextual prompt for the next agent. This ensures seamless handoff and maintains project continuity by providing all necessary context, requirements, and implementation details.

---

## 📝 Prompt Template

```
You are an expert AI agent tasked with implementing the next ticket in our project workflow. I've just completed a ticket and need to hand off to you with all the necessary context.

## Current Project Context

**Project Path**: `projects/<project_slug>/`
**Project README**: Please read the README.md file in the project directory to understand:
- Project overview and goals
- Technology stack and architecture
- Development setup and environment requirements
- Coding standards and conventions
- Testing requirements and patterns
- Deployment and operational considerations

## Linear Ticket to Implement

**Ticket ID**: [INSERT_LINEAR_TICKET_ID]
**Title**: [INSERT_TICKET_TITLE]
**Description**: [INSERT_TICKET_DESCRIPTION]
**Priority**: [INSERT_PRIORITY_LEVEL]
**Assignee**: [INSERT_ASSIGNEE]
**Due Date**: [INSERT_DUE_DATE]
**Labels**: [INSERT_LABELS]
**Related Issues**: [INSERT_RELATED_ISSUES]

## Implementation Context from Previous Work

### What Was Just Completed
- **Previous Ticket**: [INSERT_PREVIOUS_TICKET_DETAILS]
- **Key Changes Made**: [INSERT_MAJOR_CHANGES_OR_IMPLEMENTATIONS]
- **Files Modified**: [INSERT_RELEVANT_FILE_PATHS]
- **New Dependencies**: [INSERT_ANY_NEW_DEPENDENCIES_ADDED]
- **Breaking Changes**: [INSERT_ANY_BREAKING_CHANGES_OR_MIGRATIONS_NEEDED]

### Current State of the Codebase
- **Working Branch**: [INSERT_CURRENT_BRANCH_NAME]
- **Last Commit**: [INSERT_LAST_COMMIT_HASH_AND_MESSAGE]
- **Environment Status**: [INSERT_ANY_ENVIRONMENT_CHANGES_OR_REQUIREMENTS]
- **Test Status**: [INSERT_CURRENT_TEST_STATUS]

### Technical Decisions Made
- **Architecture Changes**: [INSERT_ANY_ARCHITECTURAL_DECISIONS]
- **Patterns Established**: [INSERT_ANY_NEW_PATTERNS_OR_CONVENTIONS]
- **Performance Considerations**: [INSERT_ANY_PERFORMANCE_IMPLICATIONS]
- **Security Implications**: [INSERT_ANY_SECURITY_CONSIDERATIONS]

## Relevant Conversation Context

### Key Insights from Current Session
[INSERT_RELEVANT_INSIGHTS_FROM_CURRENT_CONVERSATION]

### Challenges Encountered
[INSERT_ANY_CHALLENGES_OR_ISSUES_THAT_MIGHT_AFFECT_NEXT_TICKET]

### Solutions Implemented
[INSERT_ANY_SOLUTIONS_OR_WORKAROUNDS_THAT_MIGHT_BE_RELEVANT]

### Questions for Next Agent
[INSERT_ANY_QUESTIONS_OR_UNCERTAINTIES_THAT_NEXT_AGENT_SHOULD_ADDRESS]

## Your Task

1. **Read the Project README**: Start by reading the README.md in the project directory to understand the full context
2. **Analyze the Linear Ticket**: Review all ticket details and requirements
3. **Consider Previous Context**: Take into account the implementation context from the previous work
4. **Plan Your Approach**: Based on the project patterns and previous work, plan your implementation strategy
5. **Execute the Ticket**: Follow the standard ticket execution process as outlined in `HOW_TO_EXECUTE_A_TICKET.md`

## Success Criteria

- [ ] Ticket requirements are fully implemented
- [ ] Code follows project conventions and patterns established in previous work
- [ ] All tests pass and new tests are written as needed
- [ ] Documentation is updated if required
- [ ] Code review is ready with clear commit messages
- [ ] Any dependencies or environment changes are documented

## Additional Notes

[INSERT_ANY_ADDITIONAL_CONTEXT_OR_SPECIAL_INSTRUCTIONS]

---

**Remember**: You are inheriting a project in progress. Maintain consistency with the established patterns, conventions, and architectural decisions while implementing your specific ticket requirements.
```

---

## 🔄 Usage Instructions

### When to Use This Prompt

1. **Ticket Completion**: After successfully implementing a ticket and before moving to the next one
2. **Handoff Scenarios**: When transferring work between different agents or team members
3. **Context Preservation**: When you want to ensure all relevant context is passed forward
4. **Project Continuity**: To maintain consistency across multiple ticket implementations

### How to Use

1. **Fill in the Template**: Replace all `[INSERT_...]` placeholders with actual values
2. **Gather Context**: Collect all relevant information from:
   - Current Linear ticket details
   - Previous ticket implementation
   - Current conversation insights
   - Codebase changes made
3. **Customize as Needed**: Add or remove sections based on project-specific requirements
4. **Validate Completeness**: Ensure all critical information is included
5. **Pass to Next Agent**: Use this prompt with the next agent in your workflow

### Information Sources

- **Linear Ticket**: Use Linear MCP to fetch complete ticket details
- **Git History**: Check recent commits and branch status
- **Project README**: Always reference the project's README.md for context
- **Current Conversation**: Extract relevant insights and decisions
- **Codebase State**: Document any significant changes or patterns established

---

## 📋 Checklist for Complete Handoff

- [ ] Linear ticket details are complete and accurate
- [ ] Previous work context is documented
- [ ] Technical decisions and patterns are explained
- [ ] Environment and dependency changes are noted
- [ ] Project README reference is included
- [ ] Success criteria are clearly defined
- [ ] Any blockers or challenges are documented
- [ ] Questions for the next agent are articulated

---

## 🎯 Best Practices

1. **Be Comprehensive**: Include all relevant context, even if it seems obvious
2. **Be Specific**: Use concrete examples and file paths rather than general descriptions
3. **Be Consistent**: Follow the established patterns and conventions
4. **Be Proactive**: Anticipate questions the next agent might have
5. **Be Honest**: Document any challenges, uncertainties, or incomplete work
6. **Be Organized**: Structure the information logically and clearly

This prompt ensures that each agent has the complete context needed to continue the project effectively and maintain high-quality implementation standards. 