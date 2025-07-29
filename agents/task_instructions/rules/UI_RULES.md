# What makes a great project management ticket?

## ✅ As an Expert AI Engineer: 5 Criteria for Great Prompts
These ensure that the LLM behaves predictably, reliably, and usefully when writing tickets.

### Clear Role and Context
The prompt clearly defines the LLM’s role (e.g., “You are a technical project manager writing Linear tickets for a SaaS product”) and includes the relevant product/team context.

### Explicit Output Format
The prompt specifies the structure (e.g., title, description, acceptance criteria, priority, labels) so outputs are immediately usable in Linear.

### Concrete and Constrained Task
The prompt has a focused objective with clear boundaries: “Write a ticket to fix a bug in the login flow” is better than “Write a ticket.”

### Representative Examples (Few-shot prompting)
Good prompts often include a high-quality example or two to teach the model what a "good" ticket looks like, especially in your house style.

### Determinism and Controllability
Prompt uses control language (“always include X,” “avoid Y,” “use bullet points”) to reduce variance and align with Linear norms or team preferences.

## ✅ As an Expert Product Manager: 5 Criteria for Great Product Tickets
These ensure the ticket communicates the why and what of the work clearly.

### Clear User Problem and Business Context
The ticket ties the task to a user need or business goal. E.g., “Users are dropping off at the signup page due to confusing copy.”

### Defined Scope and Outcomes
Clear, narrow scope (what is and is not in scope) with expected outcome (“conversion rate should improve by X%”).

### Measurable Success Criteria
Contains acceptance criteria or metrics to know when the ticket is done and successful.

#### Prioritized and Time-Aware
Ticket reflects urgency/priority (e.g., tied to a milestone or sprint) and acknowledges dependencies or blockers.

### Collaborative Clarity
It invites cross-functional clarity: includes designs, links to research, stakeholder notes, or flags where clarification is needed.

## ✅ As a Staff Engineer: 5 Criteria for Great Engineering Tickets

These ensure the ticket is buildable, debuggable, and testable.

### Precise Technical Scope

The ticket describes exactly what systems are affected, what changes are needed, and any relevant interfaces.

### Reasoned Constraints and Assumptions

Flags known edge cases, performance concerns, data models, or third-party API limits that might impact the solution.

### Dependencies and Impact Awareness

Lists upstream/downstream effects (e.g., “this change affects caching logic in /auth/verify”).

### Reproducible and Observable

- For bugs: includes how to reproduce it, expected vs actual behavior, and logging/output context.
- For features: suggests how to log/test success.

### Linked Context
Includes relevant tickets (epics, related bugs), PRs, design docs, and diagrams for fast onboarding by other devs.
