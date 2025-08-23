# 🚀 How to Execute a Linear Ticket

This document provides a comprehensive, step-by-step guide for executing Linear tickets from initial analysis through implementation to PR creation and completion. This process ensures high-quality, test-driven development that follows all established coding standards, project management workflows, and GitHub operations protocols.

---

## 📋 Pre-Execution Phase

### 1. **Ticket Analysis & Context Gathering**

#### Retrieve Ticket Information
- Use the Linear MCP to fetch the complete ticket details by ID
- Extract all required information:
  - **Title**: The specific task to be implemented
  - **Context & Motivation**: Business goals and user stories
  - **Detailed Requirements**: Functional and non-functional requirements
  - **Success Criteria**: Definition of "done"
  - **Test Plan**: Required test cases and coverage
  - **Dependencies**: Blocking tickets and external requirements
  - **Suggested Implementation Plan**: High-level approach (if provided)

#### Gather Related Context
- **Review Related PRs**: Search for previous PRs related to the ticket's feature area
  - Use GitHub CLI: `gh pr list --search "<feature_keywords>"`
  - Analyze implementation patterns, code structure, and testing approaches
  - Note any architectural decisions or conventions established
- **Check Project Planning**: Review `/planning/<projectId_prefix>_<project_name>/plan_<feature>.md` for:
  - Overall project context and dependencies
  - Related subtasks and their status
  - Technical decisions and constraints
- **Examine Codebase**: Understand the current state of relevant files
  - Identify affected modules and components
  - Review existing patterns and conventions
  - Check for potential conflicts or refactoring needs

#### Validate Dependencies
- **Check Blocking Tickets**: Verify all dependencies are resolved
  - Use Linear MCP to check status of blocking tickets
  - If dependencies are incomplete, document blockers and escalate
- **External Dependencies**: Verify access to required services, APIs, or resources
- **Environment Setup**: Ensure development environment is properly configured per `CODING_REPO_CONVENTIONS.md`

### 2. **Implementation Planning**

#### Break Down the Task
- Decompose complex tickets into logical implementation steps
- Each step should be focused and testable
- Document steps in `/planning/<projectId_prefix>_<project_name>/plan_<feature>.md`

#### Estimate Effort
- Use historical data from similar tasks
- Consider complexity, testing requirements, and integration needs
- Update Linear ticket with refined estimates if needed

#### Identify Risk Areas
- Highlight potential technical challenges
- Plan mitigation strategies for high-risk components
- Document assumptions and constraints

---

## 🛠️ Implementation Phase

### 3. **Development Setup**

#### Branch Creation
Follow `GITHUB_OPERATIONS.md` for branch naming and creation:
```bash
# Create feature branch with Linear issue prefix
git checkout main && git pull
git checkout -b feature/<issueId_prefix>_<feature_snippet>
```

YOU MUST ALWAYS CREATE A NEW BRANCH IF ONE DOESN'T EXIST. DO THIS before starting a ticket.

#### Environment Activation
- **Python Projects**: Activate conda environment (e.g., `conda activate bluesky-research`)
- **JavaScript Projects**: Install dependencies with `npm install` or `yarn install` (if needed).
- **Verify Setup**: Run existing tests to ensure environment is working (and work with the user to confirm in case tests don't pass, which might be OK depending on the setup).

### 4. **Test-Driven Development**

#### Write Tests First
Following `CODING_RULES.md` testing standards:
- **Unit Tests**: Write tests for each function/component before implementation
- **Integration Tests**: Test critical paths and component interactions
- **Test Coverage**: Aim for >90% line coverage, >80% branch coverage
- **Test Naming**: Use descriptive names that explain the scenario
- **Expected Results**: Write expected output to variables for clear assertions

#### Test Structure
```python
# Example test structure for Python
def test_feature_behavior():
    # Arrange
    input_data = {...}
    expected_result = {...}
    
    # Act
    actual_result = function_under_test(input_data)
    
    # Assert
    assert actual_result == expected_result
```

### 5. **Implementation**

#### Code Quality Standards
Follow `CODING_RULES.md` for all implementation:
- **Single Responsibility**: Each function/class has one clear purpose
- **Type Hints**: All public APIs must have complete type annotations
- **Function Length**: Keep functions under 20 lines, methods under 50
- **Meaningful Names**: Variables and functions should be self-documenting
- **Early Returns**: Reduce nesting with guard clauses
- **Error Handling**: Fail fast with meaningful exceptions

#### Implementation Steps
1. **Core Logic**: Implement the main functionality
2. **Error Handling**: Add proper exception handling and validation
3. **Logging**: Implement structured logging with correlation IDs
4. **Documentation**: Add docstrings and inline comments
5. **Refactoring**: Clean up code and improve readability

#### Code Style Compliance
- Follow `CODING_REPO_CONVENTIONS.md`.

### 6. **Testing & Validation**

#### Run Test Suite
```bash
# Python with pytest
pytest tests/ -v --cov=src --cov-report=html

# JavaScript with Jest
npm test -- --coverage
```

#### Manual Testing
- Test all user flows and edge cases
- Verify error handling and validation
- Check performance characteristics
- Validate against success criteria

#### Integration Testing
- Test with real dependencies where possible
- Verify end-to-end functionality
- Check for regression issues

### 7. **Comprehensive Testing & Experimentation**

#### Proactive Testing Offer
After completing implementation and basic testing, proactively offer comprehensive testing:

**Prompt to User:**
```
✅ Implementation Complete

I've successfully implemented [feature description] and completed basic testing. 

Would you like me to conduct comprehensive testing using our systematic experimentation framework? This would include:

🔍 **System State Analysis**: Deep dive into current vs. ideal system state
📋 **Multi-Phase Test Plan**: Structured testing with clear success criteria  
🧪 **Automated Scripts**: Generate testing scripts for validation
📊 **Progress Tracking**: Detailed checklist with status updates
📈 **Performance Analysis**: Benchmarking and optimization validation

**Estimated Time**: [X] hours
**Scope**: [Specific areas to test]

This would ensure the implementation is production-ready and meets all requirements thoroughly.

Would you like me to proceed with comprehensive testing?
```

#### Comprehensive Testing Process
If the user agrees, follow the complete framework from `HOW_TO_RUN_EXPERIMENTS_TESTING.md`:

**Step 1: System State Analysis**
- Analyze current implementation against ideal system design
- Identify gaps between expected and actual functionality
- Document specific areas requiring validation
- Clarify any unclear requirements or assumptions

**Step 2: High-Level Strategy Proposal**
- Propose testing approach with clear objectives
- Identify key hypotheses to validate
- Assess risks and success criteria
- Provide timeline estimate for user approval

**Step 3: Multi-Phase Test Plan**
- Create detailed phases with specific objectives
- Define step-by-step testing procedures
- Establish clear success criteria with checkboxes
- Generate automated testing scripts where applicable

**Step 4: Execution & Progress Tracking**
- Execute each phase systematically
- Track progress with status indicators (✅ COMPLETED, 🔄 IN PROGRESS, ⏳ PENDING)
- Document findings and issues discovered
- Update Linear ticket with testing progress

**Step 5: Results Analysis & Recommendations**
- Compile comprehensive testing report
- Document all findings, performance metrics, and issues
- Provide actionable recommendations for improvements
- Update implementation if critical issues are found

#### Testing Scripts Generation
For applicable scenarios, create automated testing scripts following the templates and examples provided in `HOW_TO_RUN_EXPERIMENTS_TESTING.md`:

- **API Testing Scripts**: Use the Python script template for comprehensive API endpoint testing
- **Web Application Testing Scripts**: Use the Selenium-based template for UI testing
- **Infrastructure Testing Scripts**: Use the infrastructure testing examples for database, cache, and service validation
- **Performance Testing Scripts**: Use the performance testing framework for load and capacity testing

All scripts should include proper error handling, logging, and comprehensive reporting as outlined in the testing guide.

#### Testing Report Integration
- Create testing report in `/planning/<projectId_prefix>_<project_name>/testing_reports/`
- Update Linear ticket with testing findings and status
- Add testing scripts to the repository
- Document any issues found and resolutions applied
- Update implementation if critical issues discovered

#### Success Criteria Validation
Ensure all testing validates against the original ticket success criteria:
- [ ] All functional requirements tested and validated
- [ ] Performance requirements met and benchmarked
- [ ] Error handling scenarios covered
- [ ] Security considerations validated
- [ ] User experience flows tested
- [ ] Integration points verified
- [ ] Documentation updated with testing results

---

## 🔄 Version Control & Collaboration

### 8. **Incremental Commits**

Follow `GITHUB_OPERATIONS.md` for commit practices:
- **Small, Focused Commits**: Each commit addresses one logical change
- **Descriptive Messages**: Use format `[<type>] <description> (Linear <issue_identifier>)`
- **Linear Integration**: Include Linear issue URL in commit footer

```bash
# Example commit
git commit -m "[feat] Implement user authentication endpoint (Linear MET-123)

See: https://linear.app/metresearch/issue/MET-123"
```

### 9. **Code Review Preparation**

#### Self-Review Checklist
- [ ] All tests pass with >90% coverage
- [ ] Code follows style guidelines
- [ ] Documentation is complete and accurate
- [ ] Error handling is comprehensive
- [ ] Performance considerations addressed
- [ ] Security implications reviewed
- [ ] Success criteria met

#### Manual Code Review Offer
After completing self-review, proactively offer manual code review to the user:

**Prompt to User:**
```
✅ Self-Review Complete

I've completed my implementation and self-review. All tests pass and the code meets our quality standards.

Would you like me to prepare for a manual code review? This would include:

🔍 **Architecture Decision Explanation**: Detailed explanation of my design choices and reasoning
📋 **Code Review Context**: Comprehensive context for thorough review using our established checklist
📊 **Implementation Summary**: Clear overview of what was built and why

**Estimated Time**: 15-30 minutes
**Scope**: Complete implementation explanation and review preparation

This would ensure you have full visibility into my implementation decisions and can conduct a thorough review.

Would you like me to proceed with code review preparation?
```

#### Code Review Preparation Process
If the user agrees to manual code review, follow this structured approach:

**Step 1: Architecture Decision Explanation**
- Use `ARCHITECTURE_DECISION_PROMPT.md` to explain your implementation decisions
- Provide comprehensive context on design choices, alternatives considered, and trade-offs
- Document how your solution integrates with existing patterns and architecture

**Step 2: Code Review Context Preparation**
- Use `COMPREHENSIVE_CODE_REVIEW_CHECKLIST.md` to prepare review context
- Provide key files and review order with clear reasoning
- Highlight critical sections, pitfalls, and cross-cutting concerns
- Document testing coverage and identify any missing scenarios

**Step 3: Review Documentation**
- Create a comprehensive review package combining both prompts
- Ensure all explanations align with actual implementation
- Prepare for user questions and validation of design decisions

#### Documentation Updates
- Update relevant README files
- Add inline documentation
- Update API documentation if applicable
- Document any new patterns or conventions

---

## 📤 Pull Request Creation

### 10. **PR Creation Process**

Follow `GITHUB_OPERATIONS.md` for PR creation.

#### PR Title Format
```
(<issueId_prefix>) <feature_snippet>
```

#### PR Description Template
```markdown
Implements [feature description] as per Linear [issue_identifier].

**Linear Links**:
- Issue: https://linear.app/metresearch/issue/[issue_identifier]
- Project: https://linear.app/metresearch/project/[project_identifier]

**Changes**:
- [List of major changes]
- [Implementation details]
- [Testing approach]

**Subtasks Completed**:
- [x] [Subtask 1]
- [x] [Subtask 2]
- [ ] [Pending subtask]

**Tests**:
- Unit tests cover [X]% of functionality
- Integration tests cover critical paths
- Manual testing completed for [specific scenarios]

**Breaking Changes**:
- [List any breaking changes or migration notes]

**Screenshots** (if applicable):
[Add screenshots for UI changes]
```

#### Create PR with GitHub CLI
```bash
gh pr create \
  --title "(<issueId_prefix>) <feature_snippet>" \
  --body "<description>" \
  --base main \
  --assignee @<user> \
  --label feature,needs-review
```

### 11. **PR Management**

#### Monitor PR Status
- Track review comments and feedback
- Address review suggestions promptly
- Update PR description if needed
- Re-request review after changes

#### Handle Review Feedback
```bash
# Make additional commits for review feedback
git commit -m "[fix] Address review comments (Linear <issue_identifier>)"
git push

# Notify for re-review
gh pr comment <pr_number> --body "Updated based on feedback, please re-review"
```

---

## ✅ Completion & Cleanup

### 12. **Task Completion**

#### Wait for PR Approval
- Monitor PR status using `gh pr view <pr_number> --json state,reviewDecision,mergedAt`
- Only mark ticket complete after PR approval and merge

#### Update Linear Status
- Set Linear issue `state` to `Completed` via Linear MCP
- Update `/planning/<projectId_prefix>_<project_name>/todo.md` to `[x]`
- Log completion in `/planning/<projectId_prefix>_<project_name>/logs.md`

#### Cleanup
```bash
# Archive feature branch after merge
gh pr merge <pr_number> --delete-branch
git branch -d feature/<issueId_prefix>_<feature_snippet>
```

### 13. **Post-Completion Tasks**

#### Documentation
- Update project documentation if needed
- Add implementation notes to `/planning/<projectId_prefix>_<project_name>/lessons_learned.md`
- Document any new patterns or conventions discovered

#### Metrics & Reflection
- Log actual vs. estimated effort in `lessons_learned.md`
- Update effort estimates for similar future tasks
- Record any process improvements or challenges

#### Knowledge Sharing
- Share implementation insights with team
- Update coding standards if new patterns emerge
- Document any architectural decisions made

### 14. **Agent Retrospective**

#### Trigger Retrospective Process
- Initiate new AI agent with retrospective prompt
- Provide ticket context and execution history
- Begin three-phase retrospective process

#### Three-Phase Retrospective
1. **Agent Self-Assessment**
   - Agent analyzes ticket execution based on available context
   - Fills out basic assessment sections
   - Identifies potential areas for user input

2. **Guided User Input**
   - Agent provides structured questions for user reflection
   - User provides detailed insights and pain points
   - Agent captures user responses for synthesis

3. **Synthesis and Documentation**
   - Agent combines self-assessment and user input
   - Creates final retrospective markdown file
   - Formats for Linear ticket comment

#### File Creation and Integration
- Create `projects/<project_slug>/retrospective/{ticket}.md`
- Add retrospective file to PR
- Add retrospective as comment to Linear ticket
- Update ticket status to complete

---

## 🚨 Error Handling & Recovery

### Debugging Process

When encountering bugs, errors, or implementation challenges, follow the systematic debugging approach outlined in `HOW_TO_DEBUG.md`. Follow that approach exactly.

#### When to Use Debugging Process
- **User Reports Bugs**: When the user reports specific errors or unexpected behavior
- **Repeated Failures**: When the same issue occurs multiple times during implementation
- **Test Failures**: When tests consistently fail and the root cause is unclear
- **Integration Issues**: When components don't work together as expected
- **Performance Problems**: When the implementation doesn't meet performance requirements

#### Integration with Ticket Execution
- Document debugging findings in the Linear ticket
- Update implementation plan based on root cause analysis
- Add debugging insights to `/planning/<projectId_prefix>_<project_name>/lessons_learned.md`
- Consider if the debugging reveals broader architectural or process improvements

### Common Issues & Solutions

#### Implementation Challenges
- **Complex Requirements**: Break down into smaller subtasks
- **Technical Blockers**: Research alternatives or escalate to user
- **Performance Issues**: Profile and optimize critical paths
- **Integration Problems**: Mock dependencies for isolated testing

#### Git/GitHub Issues
- **Merge Conflicts**: Resolve locally and push updated commits
- **PR Problems**: Follow retry logic with exponential backoff

#### Linear Integration Issues
- **API Failures**: Retry with exponential backoff (1s, 2s, 4s)
- **Sync Problems**: Manually update Linear status if needed
- **Permission Issues**: Verify team access and escalate if needed

### Escalation Process
1. **Document the Issue**: Log in `/planning/<projectId_prefix>_<project_name>/logs.md`
2. **Research Solutions**: Check documentation and similar issues
3. **Propose Solution**: Present options to user with impact analysis
4. **Escalate if Needed**: Use template: `Error: <issue>. Impact: <effect>. Solution: <fix>. ETA: <time>.`

---

## 📊 Quality Assurance

### Success Metrics
- **Code Quality**: All linting and style checks pass
- **Test Coverage**: >90% line coverage, >80% branch coverage
- **Performance**: Meets specified performance requirements
- **Security**: No security vulnerabilities introduced
- **Documentation**: Complete and accurate documentation
- **User Acceptance**: Meets all success criteria from ticket

### Continuous Improvement
- **Process Feedback**: Update this guide based on lessons learned
- **Tool Improvements**: Suggest improvements to development tools
- **Knowledge Sharing**: Share insights with team members
- **Standards Updates**: Propose updates to coding standards

---

## 🔗 Related Documentation

- **Project Management**: `HOW_TO_WRITE_LINEAR_TICKET.md`, `TASK_PLANNING_AND_PRIORITIZATION.md`
- **GitHub Operations**: `GITHUB_OPERATIONS.md`
- **Coding Standards**: `CODING_RULES.md`, `CODING_REPO_CONVENTIONS.md`
- **UI Development**: `UI_RULES.md`
- **Agent Workflow**: `AGENT_WORKFLOW.md`, `LLM_REFLECTION_DEBUGGING_RULES.md`
- **Testing & Experimentation**: `HOW_TO_RUN_EXPERIMENTS_TESTING.md`
- **Debugging**: `HOW_TO_DEBUG.md`

---

This guide ensures consistent, high-quality ticket execution that follows all established standards and processes. Always refer to the specific rules documents for detailed requirements and best practices. 