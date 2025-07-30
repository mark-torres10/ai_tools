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
gh repo sync
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

---

## 🔄 Version Control & Collaboration

### 7. **Incremental Commits**

Follow `GITHUB_OPERATIONS.md` for commit practices:
- **Small, Focused Commits**: Each commit addresses one logical change
- **Descriptive Messages**: Use format `[<type>] <description> (Linear <issue_identifier>)`
- **Linear Integration**: Include Linear issue URL in commit footer

```bash
# Example commit
git commit -m "[feat] Implement user authentication endpoint (Linear MET-123)

See: https://linear.app/metresearch/issue/MET-123"
```

### 8. **Code Review Preparation**

#### Self-Review Checklist
- [ ] All tests pass with >90% coverage
- [ ] Code follows style guidelines
- [ ] Documentation is complete and accurate
- [ ] Error handling is comprehensive
- [ ] Performance considerations addressed
- [ ] Security implications reviewed
- [ ] Success criteria met

#### Documentation Updates
- Update relevant README files
- Add inline documentation
- Update API documentation if applicable
- Document any new patterns or conventions

---

## 📤 Pull Request Creation

### 9. **PR Creation Process**

Follow `GITHUB_OPERATIONS.md` for PR creation:

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

### 10. **PR Management**

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

### 11. **Task Completion**

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

### 12. **Post-Completion Tasks**

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

---

## 🚨 Error Handling & Recovery

### Common Issues & Solutions

#### Implementation Challenges
- **Complex Requirements**: Break down into smaller subtasks
- **Technical Blockers**: Research alternatives or escalate to user
- **Performance Issues**: Profile and optimize critical paths
- **Integration Problems**: Mock dependencies for isolated testing

#### Git/GitHub Issues
- **Merge Conflicts**: Resolve locally and push updated commits
- **Branch Issues**: Use `gh repo sync` to ensure clean state
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

---

This guide ensures consistent, high-quality ticket execution that follows all established standards and processes. Always refer to the specific rules documents for detailed requirements and best practices. 