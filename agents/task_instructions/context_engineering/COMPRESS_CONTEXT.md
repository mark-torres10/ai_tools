# Context Submission Request

I need you to analyze our current conversation and create a comprehensive context summary that will allow me to seamlessly continue this work with a new agent or resume after a break.

## Required Context Elements:

### 1. **Linear Ticket Information**
- **Ticket ID & Title**: [Extract from conversation]
- **Linear URL**: [Direct link to the ticket]
- **Full Description**: [Complete ticket description/requirements]
- **Success Criteria**: [What defines "done"]
- **Current Status**: [Where we are in the implementation process]

### 2. **Implementation Progress**
- **Current Phase**: [Analysis/Planning/Development/Testing/Review/etc.]
- **What's Been Completed**: [Specific tasks, code written, tests created, etc.]
- **What's In Progress**: [What we're currently working on]
- **What's Next**: [Immediate next steps]
- **Blocking Issues**: [Any blockers or dependencies]

### 3. **Technical Context**
- **Current Branch**: [Git branch name if mentioned]
- **Files Being Modified**: [Key files we're working on]
- **Environment Setup**: [Any environment details mentioned]
- **Dependencies**: [External services, APIs, or tools being used]

### 4. **AI Persona Usage**
- **Personas Consulted**: [Which specialized agents we've used]
- **Key Recommendations**: [Important advice or decisions from personas]
- **Why These Personas**: [Reasoning for persona selection]
- **Persona Handoffs**: [Any transitions between different agents]

### 5. **Decision Points & Insights**
- **Key Decisions Made**: [Architectural choices, implementation approaches]
- **Technical Challenges**: [Problems encountered and solutions]
- **Lessons Learned**: [Important insights gained]
- **Alternative Approaches Considered**: [Options we evaluated]

### 6. **Current Focus & Next Actions**
- **Immediate Task**: [What we're working on right now]
- **Next 3 Steps**: [Clear next actions]
- **Goal/Intent**: [What we’re trying to achieve]
- **Success Criteria for Current Task**: [What needs to be achieved]
- **Potential Roadblocks**: [What might slow us down]

## Output Format:

Please provide a structured summary in this exact format:

```markdown
# Work Context Summary

## �� Linear Ticket
- **ID**: [ticket_id]
- **Title**: [ticket_title]
- **URL**: [linear_url]
- **Description**: [full_description]
- **Goal/Intent**: [What we’re trying to achieve]
- **Success Criteria**: [What counts as done — if known]

## 📊 Current Status
- **Phase**: [current_phase]
- **Progress**: [completion_percentage]% complete
- **Current Task**: [what_we're_doing_now]

## ✅ Completed Work
- [List of completed items]

## 🔄 In Progress
- [Current work items]

## 📋 Next Steps
1. [Immediate next action]
2. [Second priority]
3. [Third priority]

## �� AI Personas Used
- **[Persona Name]**: [Key contribution/advice]
- **[Persona Name]**: [Key contribution/advice]

## ��️ Technical Context
- **Branch**: [branch_name]
- **Files**: [key_files]
- **Dependencies**: [external_dependencies]

## 🎯 Key Decisions
- [Important decisions made]

## ⚠️ Blockers/Challenges
- [Any current issues]

## �� Ready to Continue
The next agent should focus on: [specific focus area]
```

Please analyze our conversation and provide this structured summary. Focus on being comprehensive but concise - include all essential context needed for seamless continuation.
