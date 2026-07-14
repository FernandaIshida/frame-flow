# ADR-002 — Event-Driven Service Communication

**Status:** Accepted

**Date:** 2026-07-14

**Supersedes:** None

**Superseded by:** N/A

---

## Context

FrameFlow is designed as a distributed video processing platform where most operations are computationally intensive and may require multiple processing stages. Tasks such as media processing, transcoding, thumbnail generation, and future AI-powered analysis should not block user requests or tightly couple services.

As the system evolves toward a microservices-oriented architecture, communication patterns should minimize dependencies between services while allowing components to scale independently.

Different communication mechanisms serve different purposes within the system:

- HTTP provides synchronous request-response interactions.
- Domain Events enable asynchronous workflows across services.
- WebSockets provide real-time notifications to connected clients.

Choosing the appropriate communication mechanism for each scenario helps maintain clear service boundaries, improve resilience, and support incremental architectural evolution.

---

## Decision

FrameFlow adopts an Event-Driven Architecture (EDA) as the primary communication model for internal service interactions.

Business workflows are executed asynchronously through Domain Events published to a Message Broker. Services communicate by producing and consuming Domain Events instead of invoking one another directly.

Services must communicate through Domain Events rather than direct synchronous calls whenever the interaction represents a business workflow rather than an immediate query.

HTTP is reserved for synchronous interactions where an immediate response is required, primarily between external clients and the Backend API.

Typical examples include:

- Creating a new processing job.
- Retrieving job information.
- Listing existing jobs.
- Health checks and operational endpoints.

After a job is created, the Backend API publishes a Domain Event to the Message Broker, allowing downstream services to continue processing independently.

WebSockets are used exclusively for communication between the Backend API and frontend clients. They provide real-time notifications such as job progress, status updates, and processing completion without requiring clients to continuously poll the API.

WebSockets are not used for service-to-service communication.

Domain Events are used to coordinate workflows and propagate state changes across services. Persistent business state remains stored in PostgreSQL, which acts as the system's Source of Truth.

This communication strategy establishes three distinct interaction patterns:

- **HTTP** for synchronous client requests.
- **Domain Events** for asynchronous service communication.
- **WebSockets** for server-to-client notifications.

Each communication mechanism is used only for the scenarios for which it is best suited.

---

## Consequences

### Positive

- Reduces coupling between services.
- Improves service autonomy by allowing producers and consumers to evolve independently.
- Enables independent scaling of processing components.
- Prevents business workflows from blocking client requests.
- Improves system responsiveness.
- Increases resilience by allowing temporary service unavailability without immediately affecting producers.
- Simplifies the introduction of additional consumers for future capabilities.
- Aligns naturally with future worker pools and distributed processing.
- Supports reliable processing strategies such as retries, idempotent consumers, duplicate event handling, and dead-letter queues.
- Facilitates distributed tracing through Correlation IDs propagated across Domain Events.

### Negative

- Increases architectural complexity compared to direct synchronous communication.
- Introduces eventual consistency between services.
- Makes debugging more challenging due to asynchronous execution.
- Requires careful event versioning and schema evolution.
- Introduces operational dependencies on a Message Broker.

### Future Considerations

Future ADRs will define additional aspects of the event-driven infrastructure, including:

- Broker abstraction.
- Event Envelope.
- Event versioning.
- Correlation, Job, and Event identifiers.
- Retry strategies.
- Dead-letter queue (DLQ) support.
- Worker architecture.
- Structured logging.
- Distributed tracing.