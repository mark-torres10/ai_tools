# How to Run Experiments and Testing

## Overview

This guide provides a systematic approach for running experiments, testing new setups, verifying configurations, and breaking down testing strategies for tickets. Use this framework whenever you need to investigate something, test a new app setup, verify infrastructure configurations, or create comprehensive test plans for development tickets.

## When to Use This Guide

- **Infrastructure Testing**: Redis setup verification, database configuration testing, API endpoint validation
- **New App Setup**: Testing new application configurations, framework setups, deployment pipelines
- **Feature Testing**: Breaking down how to test new features or tickets
- **Performance Testing**: Load testing, capacity testing, optimization validation
- **Integration Testing**: Testing connections between services, APIs, or components
- **Debugging**: Systematic investigation of issues or unexpected behaviors

## Step 0: System State Analysis

Before generating hypotheses or test plans, conduct a comprehensive analysis of the current system state and desired functionality:

### Ideal System Design
- Define what the complete system should look like when functioning correctly
- Identify the expected data flow, component interactions, and user workflows
- Document the intended architecture, APIs, and integration points
- For database-related issues: analyze existing schema and identify required modifications
- **Important**: Never implement database changes independently - discuss all schema modifications before proceeding

### Current System Assessment
- Analyze the existing codebase to understand current implementation
- Identify gaps between ideal and current system states
- Document specific areas where functionality differs from expectations
- Map out the actual data flow and component interactions

### Clarification Process
- If any aspect of the ideal system design is unclear, ask specific clarifying questions
- Ensure alignment on architectural decisions and implementation priorities
- Validate assumptions about system requirements and constraints

## Step 1: Testing Environment Setup

### Create Testing Directory Structure
Before proceeding with any testing, establish the proper directory structure for organizing all testing assets:

1. **Identify Linear Ticket Reference**
   - Use the Linear MCP to fetch the current ticket details
   - Extract the ticket reference (e.g., MET-27, ABC-123)
   - If no Linear ticket is associated, use a descriptive name (e.g., `testing_redis_optimization`)

2. **Create Testing Directory**
   ```bash
   mkdir -p projects/<project_slug>/testing_<Linear_ticket_reference>/
   ```

3. **Create Initial README.md**
   Create a comprehensive README.md file in the testing directory:

   ```markdown
   # Testing: [Feature/Component Name]

   **Linear Ticket**: [Linear ticket reference]  
   **Date**: [YYYY-MM-DD]  
   **Tester**: [Agent/User name]

   ## What Was Built
   [1-2 paragraphs describing the implementation that will be tested. Include:
   - Main functionality implemented
   - Key components and their purpose
   - Technologies and frameworks used
   - Any specific requirements or constraints]

   ## What Will Be Tested
   [1-2 paragraphs describing the testing scope. Include:
   - Primary testing objectives
   - Key areas of focus (performance, functionality, security, etc.)
   - Expected outcomes and success criteria
   - Any specific scenarios or edge cases to validate]

   ## Testing Progress
   - [ ] Step 0: System State Analysis
   - [ ] Step 1: Testing Environment Setup
   - [ ] Step 2: High-Level Strategy Proposal
   - [ ] Step 3: Multi-Phase Test Plan
   - [ ] Step 4: Testing Tools and Methods
   - [ ] Step 5: Success Criteria Framework
   - [ ] Step 6: Script Generation
   - [ ] Step 7: Progress Tracking
   - [ ] Step 8: Reporting and Analysis

   ## Files in This Directory
   - `README.md` - This file
   - `01_configuration_audit.py` - [Description of script]
   - `02_performance_test.py` - [Description of script]
   - `testing_report.md` - Final testing report
   - `logs/` - Testing logs and output files
   ```

### Directory Structure
All testing assets should be organized as follows:

```
projects/<project_slug>/testing_<Linear_ticket_reference>/
├── README.md                    # Testing overview and progress
├── 01_[test_name].py           # Testing scripts (numbered)
├── 02_[test_name].py           # Additional testing scripts
├── testing_report.md           # Final comprehensive report
├── logs/                       # Testing logs and output
│   ├── test_run_001.log
│   ├── performance_metrics.json
│   └── error_logs.txt
├── data/                       # Test data and fixtures
│   ├── test_dataset.json
│   └── expected_results.json
└── screenshots/                # UI testing screenshots (if applicable)
    ├── before_test.png
    └── after_test.png
```

## Step 2: High-Level Strategy Proposal

After creating the testing environment, propose a high-level series of steps that you suggest for the investigation or testing. This should include:

### Proposed Approach
- **Primary Objective**: Clear statement of what we're trying to achieve
- **Key Hypotheses**: What we think might be the issue or what we want to validate
- **Risk Assessment**: Potential challenges or areas of concern
- **Success Criteria**: How we'll know when we've succeeded
- **Estimated Timeline**: Rough time estimate for the investigation

### Example High-Level Strategy
```
## Proposed Testing Strategy for Redis Optimization

**Primary Objective**: Validate Redis configuration and performance for Bluesky data pipeline buffer use case

**Key Hypotheses**:
1. Redis is not optimally configured for buffer operations
2. Performance may not meet MET-001 requirements
3. Memory management needs optimization

**Risk Assessment**:
- Production data safety during testing
- Performance impact on existing operations
- Configuration changes may require restart

**Success Criteria**:
- Redis meets all MET-001 performance requirements
- Buffer capacity validated for 8-hour data retention
- Configuration optimized for buffer use case

**Estimated Timeline**: 4-6 hours
```

**Await user approval before proceeding to detailed planning.**

## Step 3: Multi-Phase Test Plan

Once approved, create a detailed multi-step plan with clear phases and definitive success criteria:

### Phase Structure
Each phase should have:
- **Clear Objective**: What this phase aims to accomplish
- **Prerequisites**: What needs to be in place before starting
- **Steps**: Detailed step-by-step instructions
- **Success Criteria**: Specific, measurable outcomes
- **Dependencies**: What this phase depends on
- **Estimated Duration**: Time estimate for the phase

### Step Structure
Each step should include:
- **Objective**: What this specific step accomplishes
- **Actions**: Detailed instructions with checkboxes
- **Expected Outcomes**: What should happen when successful
- **Failure Indicators**: What indicates the step failed
- **Dependencies**: What needs to be completed first
- **Script/Code**: If applicable, provide testing scripts

## Step 4: Testing Tools and Methods

### API Testing
- **Tool**: Postman or similar API testing tool
- **Requirements**: 
  - Clear endpoint documentation
  - Test data preparation
  - Expected response validation
  - Error case testing

### Web Application Testing
- **Manual Testing Instructions**:
  - Specific URLs to visit
  - Exact UI elements to click/interact with
  - Expected page content and behavior
  - Browser console monitoring
  - Network request validation

### Infrastructure Testing
- **Scripts**: Automated testing scripts (Python, Bash, etc.)
- **Monitoring**: Performance metrics, logs, system resources
- **Validation**: Configuration verification, connectivity testing

### Database Testing
- **Schema Validation**: Verify table structures and relationships
- **Data Integrity**: Test data consistency and constraints
- **Performance**: Query performance and optimization
- **Backup/Recovery**: Test backup and restore procedures

## Step 5: Success Criteria Framework

### Quantitative Criteria
- **Performance Metrics**: Response times, throughput, latency
- **Capacity Limits**: Memory usage, storage, concurrent connections
- **Error Rates**: Success/failure percentages, error counts
- **Resource Utilization**: CPU, memory, network usage

### Qualitative Criteria
- **User Experience**: Smooth interactions, intuitive workflows
- **Error Handling**: Graceful failure modes, helpful error messages
- **Security**: Proper access controls, data protection
- **Reliability**: Consistent behavior, no unexpected failures

### Checklist Format
Use this format for step success criteria:

```
### Step 1: Configuration Audit ✅ COMPLETED
- **Status**: ✅ COMPLETED
- **Date**: YYYY-MM-DD
- **Script**: `01_configuration_audit.py`
- **Objective**: Audit current configuration against requirements
- **Actions Completed**:
  - ✅ Action 1 description
  - ✅ Action 2 description
  - ✅ Action 3 description
- **Actions Pending**: None
- **Findings**:
  - ✅ Finding 1
  - ✅ Finding 2
  - ❌ Issue 1 (if any)
```

## Step 6: Script Generation

### When to Create Scripts
- **Automated Testing**: For repetitive or complex test scenarios
- **Data Generation**: Creating test datasets
- **Performance Testing**: Load testing and benchmarking
- **Configuration Validation**: Checking system settings
- **Monitoring**: Continuous validation of system state

### Script Requirements
- **Clear Documentation**: Purpose, usage, expected outputs
- **Error Handling**: Graceful failure with informative messages
- **Logging**: Detailed logs for debugging and analysis
- **Configurability**: Environment variables or config files
- **Safety**: No destructive operations without confirmation

### Script Template

All testing scripts should be saved in the testing directory: `projects/<project_slug>/testing_<Linear_ticket_reference>/`

If testing in Python, use the following script:
```python
#!/usr/bin/env python3
"""
[Script Name] - [Brief Description]

This script [detailed description of what it does].

Usage:
    python [script_name].py [parameters]

Requirements:
    - [List of dependencies]
    - [Environment variables needed]
"""

import [required_modules]
from typing import [type hints]
from datetime import datetime

class [ClassName]:
    """[Class description]."""
    
    def __init__(self, [parameters]):
        """Initialize the [class name]."""
        [initialization code]
    
    def [method_name](self):
        """[Method description]."""
        [implementation]
    
    def run_test(self):
        """Run the complete test."""
        [test implementation]

def main():
    """Main function."""
    [main execution logic]

if __name__ == "__main__":
    [execution code]
```

If testing Typescript, write a similar Node script.

## Step 7: Progress Tracking

### Status Tracking
- **✅ COMPLETED**: Step finished successfully
- **🔄 IN PROGRESS**: Currently working on this step
- **⏳ PENDING**: Not yet started
- **❌ FAILED**: Step failed, needs investigation
- **⚠️ BLOCKED**: Waiting for dependencies or external factors

### Progress Documentation
- **Date Tracking**: When each step was completed
- **Findings Summary**: Key discoveries and results
- **Issues Log**: Problems encountered and resolutions
- **Next Steps**: What comes after each phase

## Step 8: Reporting and Analysis

### Final Report Structure
- **Executive Summary**: High-level results and recommendations
- **Detailed Findings**: Comprehensive analysis of each phase
- **Performance Metrics**: Quantitative results and comparisons
- **Issues and Resolutions**: Problems found and how they were solved
- **Recommendations**: Next steps and improvements
- **Appendices**: Scripts, logs, and detailed data

### Report File Location
Save the final testing report as `testing_report.md` in the testing directory:
```
projects/<project_slug>/testing_<Linear_ticket_reference>/testing_report.md
```

### Key Metrics to Track
- **Success Rate**: Percentage of tests passed
- **Performance Improvements**: Before/after comparisons
- **Time Savings**: Efficiency gains from optimizations
- **Risk Mitigation**: Issues identified and resolved
- **Resource Utilization**: System efficiency improvements

## Example: Redis Optimization Testing

### Phase 1: Configuration Analysis & Baseline ✅ COMPLETED

#### Step 1: Configuration Audit ✅ COMPLETED
- **Status**: ✅ COMPLETED
- **Date**: 2025-08-07
- **Script**: `01_configuration_audit.py`
- **Objective**: Audit current Redis configuration against MET-001 requirements
- **Actions Completed**:
  - ✅ Connected to Redis and retrieved current configuration
  - ✅ Analyzed memory configuration (maxmemory, maxmemory-policy)
  - ✅ Analyzed persistence configuration (AOF settings)
  - ✅ Analyzed performance configuration (timeout, tcp-backlog, etc.)
  - ✅ Identified configuration gaps and generated recommendations
  - ✅ Generated comprehensive audit report
- **Actions Pending**: None
- **Findings**:
  - ✅ Redis is already optimally configured for buffer use case
  - ✅ maxmemory: 2GB (matches requirement)
  - ✅ maxmemory-policy: allkeys-lru (matches requirement)
  - ✅ AOF persistence enabled with appendfsync everysec
  - ✅ All performance settings are well-tuned
  - ✅ No configuration changes needed

## Best Practices

### Planning
- **Start Small**: Begin with simple tests before complex scenarios
- **Document Everything**: Record all steps, findings, and decisions
- **Validate Assumptions**: Test your assumptions about system behavior
- **Plan for Failure**: Have fallback plans and error handling

### Execution
- **One Change at a Time**: Make incremental changes and test each
- **Monitor Continuously**: Watch for unexpected side effects
- **Keep Backups**: Always have a way to revert changes
- **Test in Isolation**: Minimize impact on other systems

### Analysis
- **Data-Driven Decisions**: Base conclusions on measurable results
- **Context Matters**: Consider environmental factors and dependencies
- **Document Lessons**: Record what worked and what didn't
- **Share Knowledge**: Communicate findings to the team

### Safety
- **Production Safety**: Never test destructive operations on production
- **Data Protection**: Ensure test data doesn't affect real data
- **Rollback Plans**: Always have a way to undo changes
- **Monitoring**: Watch for unexpected impacts during testing

## Common Testing Scenarios

### Infrastructure Testing
- **Database Setup**: Schema validation, connection testing, performance benchmarking
- **Cache Systems**: Redis, Memcached configuration and performance
- **Message Queues**: RabbitMQ, Kafka setup and message flow testing
- **Load Balancers**: Configuration validation and traffic distribution testing

### Application Testing
- **API Endpoints**: Functionality, performance, error handling
- **User Interfaces**: Workflow testing, responsive design, accessibility
- **Authentication**: Login flows, role-based access, security testing
- **Data Processing**: ETL pipelines, data transformation, validation

### Performance Testing
- **Load Testing**: Concurrent user simulation, throughput measurement
- **Stress Testing**: System behavior under extreme conditions
- **Capacity Testing**: Maximum load handling, resource utilization
- **Scalability Testing**: Performance under increasing load

### Integration Testing
- **Service Communication**: API integration, data flow between services
- **Third-Party Services**: External API integration and error handling
- **Database Integration**: ORM testing, query optimization, transaction handling
- **File Systems**: File upload/download, storage integration

## Troubleshooting Guide

### Common Issues
- **Environment Problems**: Missing dependencies, configuration issues
- **Network Issues**: Connectivity problems, firewall restrictions
- **Data Issues**: Corrupted test data, missing test files
- **Timing Issues**: Race conditions, timeout problems

### Debugging Steps
1. **Isolate the Problem**: Identify the specific component or step causing issues
2. **Check Logs**: Review application and system logs for error messages
3. **Verify Environment**: Ensure all dependencies and configurations are correct
4. **Simplify the Test**: Break down complex tests into simpler components
5. **Compare with Working State**: Identify differences from known good configurations

### Getting Help
- **Document the Issue**: Record exact steps, error messages, and context
- **Gather Evidence**: Collect logs, screenshots, and test results
- **Research Solutions**: Check documentation, forums, and similar issues
- **Escalate Appropriately**: Involve team members or external resources when needed

## Conclusion

This systematic approach to experiments and testing ensures thorough investigation, clear documentation, and actionable results. By following this framework, you can confidently investigate new setups, verify configurations, and create comprehensive test plans that lead to reliable, well-tested systems.

Remember: The goal is not just to test, but to understand. Every experiment should provide insights that improve your system's reliability, performance, and maintainability.
