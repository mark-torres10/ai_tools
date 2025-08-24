# Execution Planning Prompt

## Purpose
Create a comprehensive, step-by-step execution plan for implementing a Linear ticket before beginning any actual development work. The AI agent must analyze the ticket context, propose a detailed implementation approach, and wait for explicit user approval before proceeding with implementation.

## When to Use
- Before implementing any Linear ticket
- When you want to review the AI's approach before they start coding
- When you need to understand the implementation strategy and timeline
- When you want to validate assumptions and identify potential issues early
- When you need to coordinate with other team members or dependencies

## Execution Planning Framework

### 1. **Context Analysis & Understanding**
```
What is the ticket asking me to implement?
[Extract the core requirements and success criteria]

What context and constraints do I need to consider?
[Identify dependencies, existing code, and project context]

What has already been done or planned?
[Review existing work, planning documents, and related tickets]

What are the key assumptions I'm making?
[List any assumptions about requirements, dependencies, or approach]
```

### 2. **Implementation Strategy**
```
What is my high-level approach?
[Describe the overall strategy and architecture]

Why am I choosing this approach?
[Justify the technical decisions and trade-offs]

What alternatives did I consider?
[List other approaches and why they were rejected]

What are the key design decisions?
[Document architectural choices and their rationale]
```

### 3. **Detailed Implementation Plan**

#### **Phase 1: Setup & Preparation**
```
What do I need to set up first?
[List environment setup, branch creation, dependency installation]

What existing code do I need to understand?
[Identify files to review and patterns to follow]

What tests or validation do I need to run first?
[List any existing tests to verify current system state]
```

#### **Phase 2: Core Implementation**
```
What are the main implementation steps?
[Break down into logical, testable units]

What order should I implement things in?
[Explain the sequence and dependencies between steps]

What are the critical paths and edge cases?
[Identify complex logic and error scenarios]
```

#### **Phase 3: Integration & Testing**
```
How will I integrate with existing systems?
[Describe integration points and compatibility]

What testing approach will I use?
[Detail unit tests, integration tests, and manual validation]

How will I validate against success criteria?
[List specific validation steps and acceptance criteria]
```

#### **Phase 4: Documentation & Cleanup**
```
What documentation needs to be updated?
[List README files, inline docs, and API documentation]

What cleanup or refactoring is needed?
[Identify technical debt or improvements]

What deployment or rollout considerations exist?
[Note any deployment steps or configuration changes]
```

### 4. **Code Implementation Strategy**
```
What specific code will I write?
[Describe the classes, functions, and modules I plan to create]

How will I structure the code?
[Explain the organization, naming conventions, and file structure]

What patterns and conventions will I follow?
[Detail the design patterns, architectural principles, and coding standards]

Why am I choosing this code structure?
[Justify the technical approach and explain the benefits]
```

### 6. **Success Criteria & Validation**
```
How will I know each step is complete?
[Define clear completion criteria for each phase]

What are the acceptance criteria?
[List specific requirements that must be met]

How will I test and validate the implementation?
[Detail testing strategy and validation approach]

What metrics or benchmarks will I use?
[Define measurable success indicators]
```

## Response Structure

### **1. Executive Summary**
```
[Brief overview of what needs to be implemented and the proposed approach]
```

### **2. Context Analysis**
```
[Analysis of the ticket, existing work, and key constraints]
```

### **3. Implementation Strategy**
```
[High-level approach and key design decisions]
```

### **4. Detailed Execution Plan**
```
[Step-by-step breakdown of all phases with specific actions]
```

### **5. Risk Assessment**
```
[Potential issues and mitigation strategies]
```

### **6. Success Criteria**
```
[Clear completion criteria and validation approach]
```

### **8. Approval Request**
```
[Explicit request for user approval before proceeding]
```

## Approval Process

### **Before Implementation**
The AI agent MUST:
- Present the complete execution plan
- Wait for explicit user approval
- Address any questions or concerns
- Revise the plan if needed
- Get final approval before starting any coding

### **Approval Template**
```
🚨 APPROVAL REQUIRED BEFORE IMPLEMENTATION

I've analyzed the ticket and created a detailed execution plan above. 

**Key Points:**
- [Summary of approach]
- [Key technical decisions]
- [Code structure and organization]
- [Implementation phases and sequence]

**Questions for You:**
- [Any specific questions about the approach]
- [Any concerns about the timeline or risks]
- [Any additional context I should consider]

**Next Steps:**
1. Please review this execution plan
2. Ask any clarifying questions
3. Provide feedback or suggest changes
4. Give explicit approval to proceed

I will NOT start implementation until you explicitly approve this plan.

Do you approve this execution plan? If not, what changes would you like me to make?
```

## Usage Instructions

1. **Analyze the ticket context** thoroughly before proposing a plan
2. **Consider existing code and patterns** to ensure consistency
3. **Break down implementation** into logical, testable phases
4. **Describe code structure and organization** in detail without writing actual code
5. **Justify technical decisions** with clear reasoning and benefits
6. **Wait for explicit approval** before beginning implementation
7. **Be prepared to revise** the plan based on user feedback

## Success Criteria

A successful execution plan should result in:
- **Clear understanding** of what needs to be implemented
- **Detailed roadmap** with specific, actionable steps
- **Code structure clarity** with justification for technical decisions
- **Implementation sequence** that makes logical sense
- **User confidence** in the technical approach
- **Explicit approval** before any development begins

## Integration with Other Prompts

This execution planning prompt works with:
- **CRITICAL_ANALYSIS_PROMPT.md**: Use to critically evaluate the proposed approach
- **HOW_TO_EXECUTE_A_TICKET.md**: Use to guide actual implementation after approval

**Note**: This prompt is for pre-implementation planning only. The `ARCHITECTURE_DECISION_PROMPT.md` is used after implementation during code review to explain the design decisions that were actually made.

The goal is to ensure you have full visibility into the AI's implementation strategy and can provide feedback before any code is written, reducing rework and improving implementation quality.
