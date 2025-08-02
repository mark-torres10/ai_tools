# 🧾 Spec: Agent Retrospective System

## 1. Problem Statement
Currently, ticket execution learnings are captured ad-hoc in `lessons_learned.md` files, making it difficult to systematically improve workflows and train AI agents. We need a structured retrospective system that captures insights after each ticket completion to enable pattern recognition, workflow optimization, and AI agent training.

**Who is affected?** The user (immediate learning), future user (pattern recognition), and AI agents (training data)
**Why now?** Systematic learning capture is needed to improve workflows and enable data-driven optimization
**Strategic link:** Supports continuous improvement cycle and enables AI agent training

## 2. Desired Outcomes & Metrics
- Every completed ticket has a structured retrospective captured
- Three-phase process (agent self-assessment → user input → synthesis) works smoothly
- Data is consistently stored and can be aggregated for pattern analysis
- Workflow improvements are made based on retrospective insights

**Success metrics:**
- 100% completion rate of retrospectives for completed tickets
- Consistent template usage across all retrospectives
- Ability to identify patterns across multiple tickets/projects
- Time to complete retrospective process < 15 minutes

## 3. In Scope / Out of Scope

**In Scope:**
- Three-phase retrospective process (agent → user → synthesis)
- Template with checkboxes and narrative sections
- File storage in `projects/<project_slug>/retrospective/{ticket}.md`
- Integration with Linear ticket completion workflow
- PR inclusion and merge process
- Linear ticket comment addition

**Out of Scope:**
- Automated analysis of retrospectives (for now)
- Real-time feedback during ticket execution
- Integration with external analytics tools
- Automated workflow improvements based on retrospectives

## 4. Stakeholders & Dependencies
- **Primary user:** Ticket executor (you)
- **Future user:** Pattern analysis and workflow optimization
- **AI agents:** Training data for workflow improvement
- **Dependencies:** Linear API, GitHub workflow, existing file structure

## 5. Risks / Unknowns
- Risk of retrospectives becoming too time-consuming
- Risk of not capturing the right level of detail
- Need to balance structure vs. flexibility
- Ensuring consistent template usage across different types of tickets

## 6. UX Notes & Accessibility
- Three-phase conversation flow with clear transitions
- Mix of quick checkboxes and detailed narrative sections
- Consistent template format for easy aggregation
- Clear integration with existing workflow

## 7. Technical Notes
- New step in `HOW_TO_EXECUTE_A_TICKET.md` (Step 13)
- New section in `PROJECT_PLANNING_EXECUTION_OUTLINE.md`
- Retrospective prompt template
- File organization: `projects/<project_slug>/retrospective/{ticket}.md`

## 8. Compliance, Cost, GTM
- No additional infrastructure costs
- Minimal time investment per ticket (target: < 15 minutes)
- No compliance or legal implications

## 9. Success Criteria
- Retrospective template is consistently used across all completed tickets
- Three-phase process works smoothly without friction
- Data is stored in organized format for future analysis
- Linear tickets include retrospective comments
- PR workflow includes retrospective files
- User can identify actionable improvements from retrospective data

---

## Workflow Integration

The agent retrospective system integrates with the existing workflow as follows:

- **HOW_TO_EXECUTE_A_TICKET.md**: Step 13 has been added to include the retrospective process
- **PROJECT_PLANNING_EXECUTION_OUTLINE.md**: Phase 3.5 includes creation of the `retrospective/` directory
- **File Organization**: Retrospectives are stored in `projects/<project_slug>/retrospective/{ticket}.md`

## Retrospective Template Structure

```markdown
# Retrospective: [Ticket Title]

## Executive Summary
[Brief overview of ticket execution and key outcomes]

## Quick Assessment (Checkboxes)

### Planning & Analysis
- [ ] Requirements were clear and complete
- [ ] Dependencies were properly identified
- [ ] Effort estimate was accurate
- [ ] Technical approach was well-defined

### Implementation
- [ ] Code quality met standards
- [ ] Testing coverage was adequate
- [ ] Performance requirements were met
- [ ] Error handling was comprehensive

### Process & Workflow
- [ ] Git workflow was smooth
- [ ] PR review process was efficient
- [ ] Documentation was updated appropriately
- [ ] Integration with existing systems was seamless

### Time & Effort
- [ ] Actual time matched estimate
- [ ] Blockers were minimal
- [ ] Context switching was manageable
- [ ] Focus time was sufficient

## Detailed Insights

### What Went Well
[Detailed narrative of positive aspects and successful elements]

### Challenges & Pain Points
[Detailed narrative of difficulties, blockers, and areas of friction]

### Unexpected Discoveries
[Any surprises, learnings, or insights that emerged during execution]

### Process Improvements
[Specific suggestions for improving the workflow or process]

### Technical Learnings
[Technical insights, patterns, or approaches that could be applied elsewhere]

## Action Items
- [ ] [Specific action item with owner and timeline]
- [ ] [Specific action item with owner and timeline]

## Key Metrics
- **Estimated Time:** [X] hours
- **Actual Time:** [X] hours
- **Accuracy:** [X]%
- **Quality Score:** [X]/10
- **Process Efficiency:** [X]/10

## Next Steps
[Any follow-up actions, related tickets, or future considerations]
```

## Retrospective Prompt Template

```markdown
# Agent Retrospective Prompt

You are an AI agent conducting a structured retrospective for a completed ticket. Your goal is to capture learnings and insights that will help improve future workflow execution.

## Context
- **Ticket:** [Ticket Title and ID]
- **Project:** [Project Name]
- **Implementation:** [Brief description of what was implemented]
- **Execution Time:** [Start to completion]
- **PR:** [Link to merged PR]

## Your Role
1. **Phase 1 - Self Assessment:** Analyze the ticket execution based on available context and fill out the basic assessment sections
2. **Phase 2 - Guided Questions:** Ask the user structured questions to gather detailed insights
3. **Phase 3 - Synthesis:** Combine your assessment and user input into a final retrospective document

## Process
1. Start with Phase 1: Conduct your self-assessment based on the ticket context
2. Present your assessment to the user
3. Ask the user the following guiding questions:
   - What aspects of this ticket execution went particularly well?
   - What challenges or pain points did you encounter?
   - Were there any unexpected discoveries or learnings?
   - What process improvements would you suggest for similar tickets?
   - Any technical insights that could be applied to future work?
4. Synthesize the user's responses with your assessment
5. Create the final retrospective markdown file
6. Provide the content for the Linear ticket comment

## Template
Use the retrospective template structure provided above. Focus on actionable insights and specific learnings that can inform future ticket execution.
``` 