# Architecture Decision Records (ADRs)

This directory contains the **Architecture Decision Records (ADRs)** for the FrameFlow project.

ADRs capture significant architectural decisions, the context in which they were made, the rationale behind them, and their consequences. They serve as a permanent record of the project's architectural evolution and provide historical context for future changes.

---

## Purpose

The goal of ADRs is to:

* Document important architectural decisions.
* Preserve architectural knowledge.
* Explain the reasoning behind technical choices.
* Improve collaboration and maintainability.
* Support the project's long-term evolution.

---

## ADR Lifecycle

Each ADR follows one of the following statuses:

| Status     | Description              |
| ---------- | ------------------------ |
| Proposed   | Under discussion.        |
| Accepted   | Approved and adopted.    |
| Superseded | Replaced by a newer ADR. |

ADRs are never deleted. When a decision changes, a new ADR supersedes the previous one.

---

# ADR Index

## Foundation

| ID      | Title                 | Status |
| ------- | --------------------- | ------ |
| ADR-001 | Architecture Overview |        |
| ADR-018 | Repository Structure  |        |
| ADR-020 | Evolution Roadmap     |        |

---

## Communication

| ID      | Title                      | Status |
| ------- | -------------------------- | ------ |
| ADR-002 | Event-Driven Communication |        |
| ADR-003 | Broker Abstraction         |        |
| ADR-006 | Event Model and Contracts  |        |
| ADR-022 | Event Schema Versioning    |        |

---

## Domain

| ID      | Title                                 | Status |
| ------- | ------------------------------------- | ------ |
| ADR-004 | Storage Abstraction                   |        |
| ADR-005 | Job Lifecycle                         |        |
| ADR-009 | Asset Lifecycle and Deletion Strategy |        |
| ADR-021 | Object Storage Strategy               |        |

---

## Reliability & Observability

| ID      | Title                               | Status |
| ------- | ----------------------------------- | ------ |
| ADR-007 | Correlation ID, Event ID and Job ID |        |
| ADR-008 | Worker Pool Architecture            |        |
| ADR-010 | Idempotency and Retry Strategy      |        |
| ADR-011 | Logging and Observability           |        |

---

## Engineering Practices

| ID      | Title                                     | Status |
| ------- | ----------------------------------------- | ------ |
| ADR-012 | Dependency Injection Strategy             |        |
| ADR-013 | Configuration Management                  |        |
| ADR-014 | API Design Guidelines                     |        |
| ADR-015 | Versioning Strategy                       |        |
| ADR-016 | Error Handling Strategy                   |        |
| ADR-017 | Testing Strategy                          |        |
| ADR-019 | Security Principles                       |        |
| ADR-023 | Authentication and Authorization Strategy |        |

---

## ADR Template

Every ADR follows the same structure:

```
# Title

# Status

# Context

# Decision

# Consequences

## Positive

## Negative

## Future Considerations
```

---

## Guiding Principles

FrameFlow follows a pragmatic architecture based on the following principles:

* Event-Driven Design
* Low Coupling
* High Cohesion
* SOLID Principles
* Ports & Adapters (Hexagonal Architecture)
* Dependency Inversion
* Infrastructure Abstraction
* Observability by Design
* Idempotent Event Processing
* Incremental Architectural Evolution

Technologies, patterns, and abstractions are introduced only when they solve a real architectural problem.

The architecture is intentionally designed to evolve incrementally toward a production-grade distributed system while maintaining simplicity and readability.
