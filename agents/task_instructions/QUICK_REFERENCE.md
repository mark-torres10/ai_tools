# Quick Reference Guide

This guide provides decision trees and quick reference information for common scenarios. Use this to quickly navigate to the right documentation and get started efficiently.

---

## 🚀 Quick Start Decision Trees

### **"I need to start a new project"**
```
1. Do you have a project idea or requirement?
   ├─ YES → Go to "Project Management" section
   └─ NO → Use HOW_TO_BRAINSTORM.md

2. Do you have a clear specification?
   ├─ YES → Use HOW_TO_WRITE_LINEAR_PROJECT.md
   └─ NO → Use HOW_TO_WRITE_A_SPEC.md

3. Ready to create tickets?
   ├─ YES → Use HOW_TO_WRITE_LINEAR_TICKET.md
   └─ NO → Review WHAT_MAKES_A_GREAT_TICKET.md
```

### **"I have a ticket to implement"**
```
1. Is the ticket well-defined?
   ├─ YES → Go to "Execution" section
   └─ NO → Review WHAT_MAKES_A_GREAT_TICKET.md

2. Ready to start coding?
   ├─ YES → Use HOW_TO_EXECUTE_A_TICKET.md
   └─ NO → Use TASK_PLANNING_AND_PRIORITIZATION.md

3. Need to test the implementation?
   ├─ YES → Use HOW_TO_RUN_EXPERIMENTS_TESTING.md
   └─ NO → Proceed to PR creation
```

### **"I need to debug something"**
```
1. Is it a code bug?
   ├─ YES → Use HOW_TO_DEBUG.md
   └─ NO → Continue to next question

2. Is it a process or workflow issue?
   ├─ YES → Use LLM_REFLECTION_DEBUGGING_RULES.md
   └─ NO → Continue to next question

3. Is it a system configuration issue?
   ├─ YES → Use HOW_TO_RUN_EXPERIMENTS_TESTING.md
   └─ NO → Escalate to user
```

### **"I need to create a persona or agent"**
```
1. What type of persona do you need?
   ├─ Engineering → Go to "Create Personas" section
   ├─ Design → Go to "Design" section
   ├─ Routing → Go to "Route Personas" section
   └─ Other → Use CREATE_ENGINEERING_PERSONA.md as template
```

---

## 📋 Project Management Quick Reference

### **Starting a New Project**
**Primary Guide**: `HOW_TO_START_NEW_PROJECT.md`

**Quick Steps**:
1. Write spec using `HOW_TO_WRITE_A_SPEC.md`
2. Review with `WHAT_MAKES_A_GREAT_SPEC.md`
3. Create Linear project with `HOW_TO_WRITE_LINEAR_PROJECT.md`
4. Write tickets with `HOW_TO_WRITE_LINEAR_TICKET.md`

**Key Templates**:
- Spec template: See `HOW_TO_WRITE_A_SPEC.md` section 3
- Project template: See `HOW_TO_WRITE_LINEAR_PROJECT.md` section 2
- Ticket template: See `HOW_TO_WRITE_LINEAR_TICKET.md` section 3

### **Planning and Prioritization**
**Primary Guide**: `TASK_PLANNING_AND_PRIORITIZATION.md`

**Quick Steps**:
1. Decompose into subtasks (5-7 max per day)
2. Estimate effort using benchmarks
3. Prioritize using scoring system (Impact + Risk + Urgency)
4. Create plan in `/projects/<projectId_prefix>_<project_name>/plan_<feature>.md`

**Scoring System**:
- Impact: 1-5 points (user value)
- Risk: 1-5 points (complexity/uncertainty)
- Urgency: 1-5 points (time sensitivity)
- Execute higher scores first

### **Brainstorming and Ideation**
**Primary Guide**: `HOW_TO_BRAINSTORM.md`

**Quick Techniques**:
- Mind mapping for feature exploration
- User story mapping for requirements
- Technical feasibility assessment
- Stakeholder alignment check

---

## 🛠️ Execution Quick Reference

### **Implementing a Ticket**
**Primary Guide**: `HOW_TO_EXECUTE_A_TICKET.md`

**Quick Steps**:
1. **Pre-Execution**: Analyze ticket, gather context, validate dependencies
2. **Setup**: Create branch, activate environment, verify setup
3. **Development**: Write tests first, implement, validate
4. **Testing**: Run comprehensive testing (optional but recommended)
5. **PR Creation**: Create PR, handle reviews, merge

**Key Commands**:
```bash
# Branch creation
git checkout -b feature/<issueId_prefix>_<feature_snippet>

# Environment setup
conda activate bluesky-research  # Python
npm install                     # JavaScript

# Testing
pytest tests/ -v --cov=src      # Python
npm test -- --coverage          # JavaScript
```

### **Comprehensive Testing**
**Primary Guide**: `HOW_TO_RUN_EXPERIMENTS_TESTING.md`

**Quick Steps**:
1. Create testing directory: `projects/<project_slug>/testing_<Linear_ticket_reference>/`
2. Write README.md describing what was built and what will be tested
3. Follow systematic testing framework (Steps 0-8)
4. Generate automated scripts for validation
5. Create comprehensive testing report

**Testing Types**:
- **API Testing**: Postman + Python scripts
- **Web Testing**: Selenium + manual instructions
- **Infrastructure**: Configuration validation scripts
- **Performance**: Load testing and benchmarking

### **Agent Review and Retrospectives**
**Primary Guide**: `AGENT_REVIEW_TICKET.md`

**Quick Process**:
1. Self-assessment of ticket execution
2. User input collection with structured questions
3. Synthesis and documentation
4. Integration with Linear ticket

---

## 🎨 Design Quick Reference

### **User Experience Design**
**Primary Guide**: `design/README.md`

**Quick Approaches**:
- **Core Flows**: Use `prompt_core_flows_mvp.md` for MVP design
- **Edge Cases**: Use `prompt_edge_case_discovery.md` for comprehensive coverage
- **User Goals**: Use `user_goal_flow_prompt.md` for goal-oriented design

### **Design Process**
**Quick Steps**:
1. Define user goals and core flows
2. Identify edge cases and error scenarios
3. Create MVP wireframes and prototypes
4. Validate with user testing
5. Iterate based on feedback

---

## 👥 Personas Quick Reference

### **Creating Engineering Personas**
**Primary Guide**: `create_personas/CREATE_ENGINEERING_PERSONA.md`

**Quick Steps**:
1. Define persona role and expertise
2. Specify technical skills and experience
3. Create communication style and approach
4. Define problem-solving methodology
5. Test with sample scenarios

### **Agent Routing**
**Primary Guide**: `route_personas/ROUTER_AGENT.md`

**Quick Decision Tree**:
```
What type of task?
├─ Frontend/UI → Frontend expert persona
├─ Backend/API → Backend expert persona
├─ Data/Analytics → Data engineering persona
├─ DevOps/Infrastructure → DevOps expert persona
└─ General/Unknown → General engineering persona
```

---

## ⚙️ Rules Quick Reference

### **Coding Standards**
**Primary Guide**: `rules/CODING_RULES.md`

**Quick Checklist**:
- [ ] Single responsibility principle
- [ ] >90% test coverage
- [ ] Type hints on public APIs
- [ ] Functions <20 lines, methods <50 lines
- [ ] Meaningful variable names
- [ ] Early returns, reduce nesting

### **Repository Conventions**
**Primary Guide**: `rules/CODING_REPO_CONVENTIONS.md`

**Quick Setup**:
- Pre-commit hooks configured
- Package management tools set up
- Formatting standards enforced
- Environment variables documented

### **UI Design Rules**
**Primary Guide**: `rules/UI_RULES.md`

**Quick Principles**:
- Clarity over cleverness
- Accessibility first
- Business value communication
- Consistent design patterns

### **Server Operations**
**Primary Guide**: `rules/RUN_SERVERS.md`

**Quick Commands**:
```bash
# Start development server
npm run dev          # Frontend
python app.py        # Backend

# Production deployment
docker-compose up    # Containerized
npm run build        # Static build
```

---

## 🔧 Engineering Quick Reference

### **Technology Stack**
**Primary Guide**: `engineering/PREFERRED_TECH_STACK.md`

**Quick Stack Overview**:
- **Frontend**: React/Next.js, TypeScript, Tailwind CSS
- **Backend**: Python/FastAPI, Node.js/Express
- **Database**: PostgreSQL, Redis
- **Infrastructure**: Docker, Railway, Supabase

---

## 🚨 Emergency Procedures

### **When Things Go Wrong**
1. **Immediate**: Stop current operation, assess impact
2. **Document**: Log error in appropriate logs file
3. **Debug**: Use `HOW_TO_DEBUG.md` systematic approach
4. **Recover**: Follow error recovery procedures
5. **Learn**: Update lessons learned database

### **Common Error Scenarios**
- **Linear API failures**: Retry with exponential backoff
- **Git conflicts**: Resolve locally, update PR
- **Test failures**: Check environment, validate assumptions
- **Performance issues**: Profile, optimize, benchmark

---

## 📊 Progress Tracking

### **Daily Check-in**
- [ ] Review active tickets in Linear
- [ ] Update progress in `/projects/*/todo.md`
- [ ] Check for blocking dependencies
- [ ] Validate estimates vs. actual effort
- [ ] Update lessons learned

### **Weekly Review**
- [ ] Complete retrospective for finished tickets
- [ ] Update roadmap and priorities
- [ ] Review and update dependencies
- [ ] Plan next sprint priorities
- [ ] Update performance metrics

---

## 🔗 Cross-References

### **Document Dependencies**
- **Project Management** → **Execution** → **Testing** → **Review**
- **Design** → **Engineering** → **Rules** → **Execution**
- **Personas** → **Routing** → **Execution** → **Review**

### **Tool Integration**
- **Linear** ↔ **GitHub** ↔ **Local Files**
- **Testing Scripts** → **Linear Tickets** → **PRs**
- **Personas** → **Task Assignment** → **Execution**

---

## 📝 Quick Templates

### **Ticket Template**
```markdown
# [Title]

## Context & Motivation
[Business goals and user stories]

## Detailed Requirements
- [ ] Functional requirement 1
- [ ] Functional requirement 2
- [ ] Non-functional requirement 1

## Success Criteria
- [ ] Criterion 1
- [ ] Criterion 2

## Test Plan
- [ ] Test case 1
- [ ] Test case 2

## Dependencies
- [ ] Dependency 1
- [ ] Dependency 2
```

### **Testing Report Template**
```markdown
# Testing Report: [Feature]

## Executive Summary
[High-level results and recommendations]

## Detailed Findings
[Comprehensive analysis of each phase]

## Performance Metrics
[Quantitative results and comparisons]

## Issues and Resolutions
[Problems found and how they were solved]

## Recommendations
[Next steps and improvements]
```

---

**Remember**: This quick reference is a starting point. Always refer to the detailed documentation for comprehensive guidance and specific procedures.
