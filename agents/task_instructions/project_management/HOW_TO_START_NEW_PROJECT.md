# 📦 How to Start a New Project

This agent is responsible for guiding the user through the full lifecycle of starting a new Linear project. It includes spec creation, project setup, ticket generation, and organization. Follow this exact process.

---

## ✅ Step-by-Step Instructions

### 0. **Make sure setup steps are done correctly**

- Clarify from the user which team this is a part of. There are several teams in Linear depending on the client that the user is working with. First, get the list of teams, and then clarify the user which team this is a part of. Each client is assigned to one team, so the work that you will be doing will depend on the client. Use the Linear MCP to get the list of teams and then verify with the user which team to load.
- Ask the user if there is already an existing conda environment, and if so, what it is called, as this needs to be added in the context of any flows.


### 1. **Create a New Spec (temp_spec.md)**
- Use the prompt and structure defined in [`HOW_TO_WRITE_A_SPEC.md`](HOW_TO_WRITE_A_SPEC.md).
- Walk the user through the 5 stakeholder-aligned phases:
  - Problem definition
  - Success metrics
  - Scope boundaries
  - UX considerations
  - Technical estimability
- Once complete, save the spec to a temporary file named `temp_spec.md`


---

### 2. **Create the Linear Project**
- Use the finalized spec in `temp_spec.md` to generate a Linear **Project**.
- Follow the structure and tone from [`HOW_TO_WRITE_LINEAR_PROJECT.md`](HOW_TO_WRITE_LINEAR_PROJECT.md):
  - Title (Noun + Outcome)
  - Problem Statement
  - Objective & Success Criteria
  - Scope & Deliverables
  - Timeline & Milestones
  - Team & Stakeholders
  - Risks & Mitigations
  - Related Tickets & Projects

---

### 3. **Move the Spec into the Project Folder**
- Once the project is created, move the `temp_spec.md` file into the appropriate folder tied to the project name.
- Example:  
  ```
  projects/<project_slug>/spec.md
  ```

---

### 4. **Generate Tickets from the Spec**
- Break down the work into tickets based on the spec.
- Use the structure in [`HOW_TO_WRITE_LINEAR_TICKET.md`](HOW_TO_WRITE_LINEAR_TICKET.md):
  - Title
  - Context & Motivation
  - Functional & Non-functional Requirements
  - Success Criteria
  - Test Plan
  - Dependencies
  - Suggested Implementation Plan
  - Effort Estimate.
  - Priority & Impact
  - Acceptance Checklist
  - Links & References
- Prioritize scoping tickets in a way that will minimize serial dependence on the tickets being executed in order. Ideally, I want to spawn as many parallel AI agents as possible to implement the tickets, so if there are some that have to be executed serially, it's fine, but ideally, it would be great to be able to execute as many as possible in parallel.
- Update then the project in Linear. This needs to then have links to all the tickets as well as a list of which tickets have to be done in order and which ones can be done in parallel.
  - For example, if Ticket 1 is needed, then Ticket 2 and 3 can be done in parallel, then Ticket 4, then Ticket 5 and 6 in parallel, I want it to look something like this:

    ```plaintext
    Tickets:
    - Ticket 1: <Link to ticket>
    - Can be done in parallel:
      - Ticket 2: <Link to ticket>
      - Ticket 3: <Link to ticket>
    - Ticket 4: <Link to ticket>
    - Can be done in parallel:
      - Ticket 5: <Link to ticket>
      - Ticket 6: <Link to ticket>
    ```

- Later on, as I reference these tickets, make sure to remind me which tickets can be done in parallel, and which tickets this one depends on, and which tickets depend on this one being done.

---

### 5. **Iterate on the Tickets**
- After tickets are created, the team can:
- Refine scope
- Add implementation notes
- Attach links to Figma, PRs, or other resources
- Use guidance from the ticket style guide to ensure tickets are atomic, testable, and complete.

---

## 🧠 Agent Tips

- Always confirm spec completeness before moving to project creation.
- Ensure each phase of the spec has been sufficiently addressed with stakeholder concerns captured.
- Use traceable file references (`HOW_TO_WRITE_A_SPEC.md`, `HOW_TO_WRITE_LINEAR_PROJECT.md`, `HOW_TO_WRITE_LINEAR_TICKET.md`) to enforce structure and quality.

---

## 📁 Final File Organization

```plaintext
projects/
└── project-slug/
  ├── spec.md              ← Finalized spec (renamed from temp_spec.md)
  ├── tickets/
  │   ├── ticket-001.md
  │   └── ticket-002.md
  └── README.md            ← Optional: project overview or dashboard
