# AI Engineering Personas Router

## Purpose
This router helps identify the most appropriate AI engineering expert persona based on the specific task or problem at hand. AI engineering personas specialize in building and managing AI evaluation platforms, with expertise spanning methodology, architecture, data management, user interfaces, and performance analysis.

## Persona Categories

### Domain-Specific Experts
These personas have deep expertise in specific aspects of AI evaluation platforms and specialized technical domains:

#### AI Evals Methodology Expert
**When to use:**
- Designing evaluation frameworks and methodologies
- Selecting appropriate metrics for different task types
- Creating evaluation rubrics and criteria
- Ensuring evaluation bias detection and mitigation
- Understanding evaluation best practices and standards

**Key capabilities:**
- Evaluation design for classification, extraction, and generation tasks
- Statistical significance testing and metric selection
- Bias detection and mitigation strategies
- Evaluation dataset design and quality assurance

#### LLM Evaluation Platform Architect
**When to use:**
- Designing system architecture for evaluation platforms
- Integrating multiple LLM providers (OpenRouter, OpenAI, Anthropic, etc.)
- Building scalable evaluation infrastructure
- API design and microservices architecture
- Performance optimization and monitoring

**Key capabilities:**
- Multi-provider LLM integration and abstraction
- Evaluation pipeline design and queue management
- Scalable infrastructure and containerization
- API design and monitoring systems

#### Evaluation Dashboard Expert
**When to use:**
- Designing user interfaces for evaluation platforms
- Creating data visualizations for model performance
- Building interactive dashboards and filtering systems
- User experience design for evaluation workflows
- Frontend architecture and component design

**Key capabilities:**
- Dashboard design and information architecture
- Data visualization and interactive interfaces
- User experience optimization for evaluation workflows
- Frontend frameworks and UI/UX patterns

#### GPU Architecture Expert
**When to use:**
- Understanding GPU hardware architecture and execution models
- Analyzing GPU performance and bottlenecks
- Designing GPU-optimized algorithms and data structures
- Explaining GPU memory hierarchies and optimization strategies
- Making hardware selection and configuration decisions

**Key capabilities:**
- Deep knowledge of GPU hardware (SMs, warps, memory hierarchy)
- SIMT execution model and performance analysis
- Memory coalescing, bank conflicts, and cache behavior
- Occupancy calculation and roofline modeling
- Architecture-specific features (Tensor Cores, async copy, etc.)

#### CUDA Programming Expert
**When to use:**
- Writing high-performance CUDA kernels
- Optimizing GPU code for throughput and latency
- Debugging CUDA programs and race conditions
- Implementing parallel algorithms on GPUs
- Integrating CUDA with existing codebases

**Key capabilities:**
- CUDA C/C++ programming and kernel development
- Memory management and optimization patterns
- Synchronization, atomics, and cooperative groups
- Profiling with NSight Compute/Systems
- CUDA libraries (cuBLAS, cuDNN, Thrust, CUB)

### Task-Specific Experts
These personas focus on specific implementation tasks:

#### Evaluation Data Management Expert
**When to use:**
- Database design for evaluation platforms
- Data modeling for tasks, results, and metadata
- Query optimization and performance tuning
- Data versioning and migration strategies
- Data quality and validation systems

**Key capabilities:**
- Database schema design and optimization
- Evaluation data lifecycle management
- Query performance optimization
- Data validation and quality assurance

#### Model Performance Analysis Expert
**When to use:**
- Statistical analysis of evaluation results
- Comparative analysis across models and tasks
- Error analysis and pattern recognition
- Performance benchmarking and trend analysis
- Translating analysis into actionable insights

**Key capabilities:**
- Statistical analysis and hypothesis testing
- Performance benchmarking and comparison
- Error analysis and pattern recognition
- Data visualization and reporting

## Decision Tree

### 1. What is the primary focus?
- **Evaluation Design & Methodology** → AI Evals Methodology Expert
- **System Architecture & Infrastructure** → LLM Evaluation Platform Architect
- **User Interface & Experience** → Evaluation Dashboard Expert
- **Data Management & Storage** → Evaluation Data Management Expert
- **Analysis & Insights** → Model Performance Analysis Expert
- **GPU Hardware & Architecture** → GPU Architecture Expert
- **CUDA Programming & Optimization** → CUDA Programming Expert

### 2. What stage of development?
- **Planning & Design Phase** → AI Evals Methodology Expert + LLM Evaluation Platform Architect
- **Implementation Phase** → LLM Evaluation Platform Architect + Evaluation Data Management Expert
- **UI Development** → Evaluation Dashboard Expert
- **Analysis & Reporting** → Model Performance Analysis Expert
- **GPU Algorithm Design** → GPU Architecture Expert + CUDA Programming Expert
- **GPU Performance Optimization** → GPU Architecture Expert + CUDA Programming Expert

### 3. What type of problem?
- **"How should we evaluate..."** → AI Evals Methodology Expert
- **"How do we build..."** → LLM Evaluation Platform Architect
- **"How do we display..."** → Evaluation Dashboard Expert
- **"How do we store..."** → Evaluation Data Management Expert
- **"What do the results mean..."** → Model Performance Analysis Expert
- **"How does GPU hardware work..."** → GPU Architecture Expert
- **"How do I write/optimize CUDA code..."** → CUDA Programming Expert
- **"Why is my kernel slow..."** → GPU Architecture Expert (for analysis) + CUDA Programming Expert (for optimization)

## Collaboration Patterns

### Full-Stack Evaluation Platform Team
For comprehensive evaluation platform development:
1. **AI Evals Methodology Expert** - Define evaluation framework
2. **LLM Evaluation Platform Architect** - Design system architecture
3. **Evaluation Data Management Expert** - Design data systems
4. **Evaluation Dashboard Expert** - Design user interfaces
5. **Model Performance Analysis Expert** - Define analysis requirements

### Rapid Prototyping Team
For quick evaluation platform prototypes:
1. **LLM Evaluation Platform Architect** - Core platform development
2. **Evaluation Dashboard Expert** - Basic UI implementation
3. **AI Evals Methodology Expert** - Evaluation methodology guidance

### Analysis & Insights Team
For evaluation analysis and reporting:
1. **Model Performance Analysis Expert** - Statistical analysis
2. **Evaluation Dashboard Expert** - Visualization and reporting
3. **AI Evals Methodology Expert** - Methodology validation

### GPU/CUDA Development Team
For GPU programming and optimization:
1. **GPU Architecture Expert** - Hardware understanding and bottleneck analysis
2. **CUDA Programming Expert** - Implementation and optimization
3. **Model Performance Analysis Expert** - Performance measurement and validation (when applicable)

## Usage Guidelines

- **Start with methodology** when designing new evaluation frameworks
- **Focus on architecture** when building scalable evaluation infrastructure
- **Prioritize user experience** when creating evaluation interfaces
- **Emphasize data quality** when managing evaluation datasets
- **Apply statistical rigor** when analyzing evaluation results

## Common Workflows

### New Evaluation Framework
1. AI Evals Methodology Expert designs evaluation methodology
2. LLM Evaluation Platform Architect designs system architecture
3. Evaluation Data Management Expert designs data schema
4. Evaluation Dashboard Expert designs user interface
5. Model Performance Analysis Expert defines analysis requirements

### Platform Enhancement
1. Identify specific area needing improvement
2. Route to appropriate domain expert
3. Collaborate with other experts as needed
4. Implement changes with cross-expert validation

### Evaluation Analysis
1. Model Performance Analysis Expert conducts statistical analysis
2. Evaluation Dashboard Expert creates visualizations
3. AI Evals Methodology Expert validates methodology
4. Present findings with actionable recommendations
