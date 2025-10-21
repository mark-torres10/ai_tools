# 🧭 Backend Agent Persona Router

This folder contains specialized AI agents for backend development, focusing on architecture, concurrency, and language-specific expertise.

Use this file to decide which agent persona is best suited for backend development tasks. If no persona is a good fit, consider creating a new one using the persona creation templates.

---

## 🧠 Persona Directory

### `backend_architect.md`
- **Name**: Backend Architect
- **Summary**: Master backend architect specializing in scalable server-side systems, API design, and database architecture
- **Focus Areas**: API design, microservices, database architecture, authentication, scalability, system design
- **Example Tasks**:
  - Designing RESTful APIs with proper versioning
  - Creating database schemas with efficient indexing
  - Implementing OAuth2 authentication systems
  - Architecting microservices with clear boundaries
  - Building scalable backend systems
  - Optimizing database query performance

### `concurrent_programming_expert.md`
- **Name**: Concurrent Programming Models Expert
- **Summary**: Deep expertise in concurrency paradigms including CSP, Actor model, STM, and async patterns
- **Focus Areas**: concurrency models, synchronization primitives, deadlock prevention, race conditions, goroutines, channels, async/await, parallel execution
- **Key Expertise**:
  - CSP (Communicating Sequential Processes) with Go channels
  - Actor model (Erlang/OTP, Akka)
  - Software Transactional Memory (STM)
  - Async/await patterns across languages
  - Detecting and preventing deadlocks, race conditions, livelocks
  - Memory ordering and atomic operations
- **Example Tasks**:
  - Implementing worker pool pattern with Go channels
  - Debugging deadlock in concurrent system
  - Designing actor-based message passing architecture
  - Optimizing async/await patterns for performance
  - Preventing race conditions with proper synchronization
  - Implementing lock-free data structures

### `go_expert.md`
- **Name**: Go Programming Language Expert
- **Summary**: Pragmatic Go expert grounded in Go's philosophy of simplicity, explicitness, and idiomatic patterns
- **Focus Areas**: Go idioms, goroutines, channels, error handling, interface design, testing, profiling, performance optimization
- **Key Expertise**:
  - Idiomatic Go patterns ("Accept interfaces, return structs")
  - Goroutine and channel patterns (worker pools, fan-out/fan-in)
  - Context package for cancellation and timeouts
  - Table-driven testing and benchmarks
  - Profiling with pprof (CPU, memory, goroutine leaks)
  - Error handling as values with wrapping
- **Example Tasks**:
  - Building concurrent web scraper with goroutine pools
  - Implementing proper error handling with context wrapping
  - Optimizing Go program using pprof analysis
  - Designing idiomatic Go interfaces and package structure
  - Writing table-driven tests with comprehensive coverage
  - Debugging goroutine leaks and memory issues

---

## 📌 Routing Guidelines

To determine which persona to use:

### Use **Backend Architect** when:
- ✅ Designing overall system architecture
- ✅ Making database schema and technology choices
- ✅ Building RESTful or GraphQL APIs
- ✅ Implementing authentication/authorization systems
- ✅ Architecting microservices or monoliths
- ✅ General backend development questions
- ✅ Choosing between different backend approaches

### Use **Concurrent Programming Expert** when:
- ✅ Implementing concurrent or parallel systems
- ✅ Debugging deadlocks, race conditions, or synchronization issues
- ✅ Choosing between concurrency models (CSP vs Actor vs STM)
- ✅ Implementing complex synchronization patterns
- ✅ Optimizing parallel execution performance
- ✅ Understanding memory ordering and atomics
- ✅ **Language-agnostic** concurrency questions

### Use **Go Expert** when:
- ✅ Writing idiomatic Go code
- ✅ Implementing Go-specific concurrency (goroutines, channels, context)
- ✅ Debugging Go performance issues with pprof
- ✅ Following Go best practices and conventions
- ✅ Testing Go code with table-driven tests
- ✅ **Go language-specific** questions
- ✅ Choosing Go patterns and ecosystem libraries

### Use **Go Expert + Concurrent Programming Expert** when:
- ✅ Complex concurrency problems in Go requiring both Go idioms and deep concurrency theory
- ✅ Start with Go Expert for idiomatic approach, consult Concurrent Programming Expert for advanced patterns

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Agent(s) |
|--------------|-------------------|
| "Design API for user authentication" | `backend_architect.md` |
| "Optimize database queries for scale" | `backend_architect.md` |
| "Build microservices architecture" | `backend_architect.md` |
| "Fix deadlock in concurrent system" | `concurrent_programming_expert.md` |
| "Implement actor-based message system" | `concurrent_programming_expert.md` |
| "Choose between CSP vs Actor model" | `concurrent_programming_expert.md` |
| "Write idiomatic Go HTTP handler" | `go_expert.md` |
| "Debug goroutine leak with pprof" | `go_expert.md` |
| "Implement worker pool in Go" | `go_expert.md` (for idiomatic Go) or `concurrent_programming_expert.md` (for patterns) |
| "Build concurrent web scraper in Go" | `go_expert.md` + `concurrent_programming_expert.md` |
| "Design Go package structure" | `go_expert.md` |
| "Implement distributed system in Go" | `backend_architect.md` (architecture) + `go_expert.md` (implementation) |

---

## 🎯 Decision Tree

```
Backend Task
│
├─ Language-specific? 
│  └─ Go → go_expert.md
│
├─ Concurrency/parallelism focus?
│  ├─ Language-agnostic theory → concurrent_programming_expert.md
│  └─ Go-specific implementation → go_expert.md
│
├─ System architecture/design?
│  └─ backend_architect.md
│
└─ General backend development?
   └─ backend_architect.md
```

---

## 🛠️ Update Instructions

After adding new personas to this folder, rerun the router generation to update this file.

---

## Notes

- **Backend Architect**: Best starting point for general backend tasks, system design, and API development
- **Concurrent Programming Expert**: Deep theoretical knowledge across all concurrency models (CSP, Actor, STM, async/await)
- **Go Expert**: Idiomatic Go patterns, testing, profiling, and Go ecosystem best practices
- For Go concurrency: Start with Go Expert for idiomatic patterns, escalate to Concurrent Programming Expert for advanced theory
- All personas can work together on complex backend systems

