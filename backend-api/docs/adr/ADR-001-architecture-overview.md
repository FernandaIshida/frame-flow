# ADR-001: Architecture Overview

## Status

Accepted

## Context

FrameFlow is designed as a distributed video processing platform focused on asynchronous processing, scalability, and independent evolution of its components.

The system must support future growth toward a microservices-oriented architecture while maintaining simplicity, maintainability, and clear boundaries during early development.

The project is organized as a monorepo containing independent services that communicate through well-defined contracts and abstractions.

## Decision

FrameFlow adopts a distributed service architecture composed of the following components:

* **backend-api**: Responsible for external communication, API endpoints, job management, persistence, and client notifications.
* **media-service**: Responsible for media processing workflows, file handling, and AI-related processing capabilities.
* **worker-go**: Responsible for asynchronous job orchestration, background processing, and coordination between system components.

The architecture follows these core principles:

* Event-driven communication between services whenever asynchronous processing is required.
* Low coupling and high cohesion between components.
* Dependency inversion through abstractions and interfaces.
* Infrastructure independence through ports and adapters.
* PostgreSQL as the source of truth for persistent application state.
* Incremental evolution toward microservices based on real domain boundaries and system requirements.

External infrastructure components, such as message brokers and object storage providers, must be accessed through abstractions to allow future replacement with minimal impact on business logic.

All significant architectural decisions must be documented through Architecture Decision Records (ADRs).

## Consequences

### Positive

* Services can evolve independently.
* Infrastructure components can be replaced with reduced impact.
* The architecture supports asynchronous processing and future scalability.
* Architectural decisions remain explicit and traceable.
* The system can evolve incrementally without premature complexity.

### Negative

* Distributed architectures introduce additional complexity compared to a traditional monolithic application.
* Communication failures, retries, and consistency challenges must be explicitly handled.
* Additional effort is required for observability and operational concerns.

### Future Considerations

* Further decomposition into dedicated microservices when justified by domain complexity.
* Introduction of advanced distributed tracing and observability solutions.
* Expansion of messaging infrastructure as system requirements evolve.
