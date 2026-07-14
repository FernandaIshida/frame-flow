# ADR-003 — Message Broker Abstraction

**Status:** Accepted

**Date:** 2026-07-14

**Supersedes:** None

**Superseded by:** N/A

---

## Context

FrameFlow adopts an Event-Driven Architecture in which services communicate asynchronously through Domain Events.

To support reliable asynchronous communication, the system requires a Message Broker responsible for transporting events between producers and consumers.

Multiple messaging technologies can fulfill this responsibility, each providing different operational characteristics, performance profiles, and delivery guarantees.

Different brokers offer different trade-offs regarding throughput, ordering, durability, delivery guarantees, and operational complexity.

Coupling business logic to a specific messaging technology would make future evolution more difficult and increase the impact of infrastructure changes.

To preserve architectural flexibility and maintain the principles established in ADR-001, messaging infrastructure should remain an implementation detail rather than a domain concern.

---

## Decision

FrameFlow depends on a Message Broker abstraction rather than a specific messaging technology.

Business logic and application services publish and consume Domain Events exclusively through this abstraction. They must not depend directly on vendor-specific APIs, protocols, or implementation details.

The abstraction defines the capabilities required by the application rather than exposing broker-specific features.

Infrastructure adapters are responsible for translating the abstraction into concrete broker implementations.

Redis is the initial Message Broker implementation.

Redis Streams is the preferred messaging mechanism due to its support for reliable event delivery, consumer groups, pending message tracking, acknowledgements, and scalability requirements appropriate for the current stage of the project.

Alternative messaging mechanisms may be adopted in future implementations provided they preserve the capabilities required by the Message Broker abstraction.

Future implementations may include technologies such as RabbitMQ or Kafka without requiring changes to the business logic or application workflows.

The Message Broker is responsible only for transporting Domain Events. It is not the system's Source of Truth. Persistent business state remains stored in PostgreSQL, which serves as the system's Source of Truth.

The choice of Message Broker is considered an infrastructure concern and must remain transparent to the domain layer.

The operational capabilities provided by the broker are considered architectural concerns and must be preserved when replacing implementations.

---

## Consequences

### Positive

- Decouples business logic from messaging infrastructure.
- Supports replacement of the Message Broker with minimal impact on the application.
- Facilitates migration between messaging technologies without modifying the domain model.
- Simplifies testing through mock or in-memory broker implementations.
- Encourages adherence to the Ports and Adapters architectural style.
- Supports incremental architectural evolution as system requirements change.

### Negative

- Introduces an additional abstraction layer.
- Requires adapter implementations for each supported Message Broker.
- Some broker-specific capabilities may not be exposed through the common abstraction.
- The abstraction should remain intentionally minimal to avoid becoming a least-common-denominator interface.
- Additional maintenance is required to keep multiple implementations consistent.

### Future Considerations

Future ADRs will define additional aspects of the messaging infrastructure, including:

- Broker capabilities.
- Delivery guarantees.
- Retry strategies.
- Dead-letter queue (DLQ) support.
- Consumer groups.
- Event ordering.
- Event schema evolution.
- Broker-specific optimizations.