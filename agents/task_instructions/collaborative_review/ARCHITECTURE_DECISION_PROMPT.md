# Architecture Decision Explanation Prompt

## Purpose
Understand and validate the design logic and architectural decisions that AI agents used when implementing code, providing transparency into their reasoning process during code review.

## When to Use
- During code review after AI has implemented a solution
- When reviewing complex architectural changes or new features
- When validating that the AI's implementation follows sound design principles
- As a complement to the comprehensive code review checklist
- When you need to understand the AI's technical reasoning and trade-offs

## Implementation Explanation Template

### 1. Problem Statement
```
What problem did I solve?
[AI explains the problem they addressed and its scope]

Why was this problem important?
[Business impact and urgency that drove the solution]

What constraints did I work within?
[Technical, business, and resource constraints that influenced the solution]
```

### 2. Implemented Solution
```
What architecture did I implement?
[High-level design with key components that were built]

How does my solution solve the problem?
[Direct mapping from implemented solution to the problem]

What were my key design decisions?
[List and explain each major decision made during implementation]
```

### 3. Alternative Approaches Considered
```
What alternatives did I consider?
[Other possible solutions that were evaluated]

Why did I reject them?
[Specific reasons for not choosing alternatives]

What are the trade-offs of my chosen approach?
[Pros and cons of the implemented solution]
```

### 4. Technical Justification
```
Why did I choose this technology/pattern?
[Specific reasons for the technical choices made]

How does my implementation integrate with the existing system?
[Integration points and compatibility considerations]

What are the performance implications of my solution?
[Expected performance characteristics and any optimizations]
```

### 5. Risk Assessment
```
What technical risks does my implementation have?
[Potential failure points and how I mitigated them]

What operational risks should be considered?
[Deployment, monitoring, maintenance concerns I identified]

What business risks might arise from my solution?
[Potential impact on users, revenue, compliance]
```

### 6. Implementation Approach
```
How did I implement this solution?
[Step-by-step approach I actually took]

What dependencies did I encounter?
[Prerequisites and blocking factors I had to work around]

How did I approach testing?
[Testing strategy and validation methods I used]
```

### 7. Long-term Considerations
```
How will my solution scale?
[Scalability implications and limits I considered]

How will this be maintained?
[Maintenance requirements and complexity I built in]

How will this evolve?
[Future extensibility and flexibility I designed for]
```

## Integration with Code Review

This prompt is designed to work **in parallel** with your `COMPREHENSIVE_CODE_REVIEW_CHECKLIST.md`. While the checklist focuses on **what** to review, this prompt explains **why** the AI made certain design decisions.

### How to Use Together

1. **AI provides implementation explanation** using this template
2. **You review the code** using the comprehensive checklist
3. **Cross-reference explanations** with actual implementation
4. **Validate that design logic** matches the code quality

### Key Questions to Ask

**Technical Validation:**
- Does the AI's explanation match what you see in the code?
- Are the design decisions actually implemented as described?
- Does the solution follow the patterns the AI claims it follows?

**Integration Validation:**
- Does the integration approach described match the actual code?
- Are the dependencies and assumptions clearly documented?
- Does the performance approach align with the implementation?

**Risk Validation:**
- Are the identified risks actually addressed in the code?
- Does the testing approach match the risk assessment?
- Are the mitigation strategies properly implemented?

## Review Criteria

### Must Validate
- [ ] AI's explanation matches the actual implementation
- [ ] Design decisions are properly implemented in code
- [ ] Integration approach aligns with existing patterns
- [ ] Risk mitigation strategies are actually coded
- [ ] Testing approach covers identified concerns

### Should Validate
- [ ] Performance optimizations are implemented as described
- [ ] Error handling matches the risk assessment
- [ ] Documentation aligns with the technical approach
- [ ] Code quality reflects the design decisions
- [ ] Maintainability features are properly implemented

### Nice to Validate
- [ ] Future extensibility is built into the code
- [ ] Monitoring and observability are implemented
- [ ] Code follows best practices for the chosen approach
- [ ] Performance characteristics match expectations
- [ ] Security considerations are properly addressed

## Example Implementation Explanation

```
Problem: I needed to handle 10x increase in user load during peak hours

Implemented Solution: I implemented a Redis caching layer with write-through strategy

Key Design Decisions:
1. Redis over Memcached: I chose Redis for better persistence and data structures
2. Write-through over write-behind: I implemented write-through for simpler consistency model
3. Cluster mode: I configured cluster mode for horizontal scaling and high availability

Alternatives I Considered:
- Database read replicas: I rejected this due to higher latency and complexity
- Application-level caching: I rejected this due to memory constraints and lack of persistence

Risks I Identified and Mitigated:
- Redis cluster complexity: I implemented comprehensive error handling and fallback logic
- Cache invalidation challenges: I built a TTL-based invalidation system with manual override
- Memory usage growth: I implemented memory monitoring and alerting

Integration Approach:
- I extended the existing service layer caching interface to support Redis
- I maintained backward compatibility with existing cache implementations
- I added Redis health checks to the existing monitoring system
```

## Code Review Workflow

1. **AI implements solution** and provides explanation using this template
2. **You review the code** using `COMPREHENSIVE_CODE_REVIEW_CHECKLIST.md`
3. **Cross-reference explanation** with actual implementation
4. **Validate design logic** matches code quality and patterns
5. **Provide feedback** on both implementation and design reasoning
6. **AI iterates** on both code and explanation if needed

## Tips for Effective Code Review with AI Explanations

- **Compare explanation to code** - ensure they match
- **Validate design decisions** against actual implementation
- **Check that risk mitigation** is properly coded
- **Verify integration approach** matches existing patterns
- **Ensure testing strategy** covers identified concerns
- **Look for consistency** between explanation and code quality
- **Question any discrepancies** between design and implementation
