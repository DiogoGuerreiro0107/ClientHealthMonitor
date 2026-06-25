# ADR - Architecture Decision Record

## Purpose

This document describes the main architecture decisions taken and the reason for those choices.

## Use Django REST Framework

### Context

The project needs a backend API for dashboard users, monitoring agents, alerts, and integrations. The backend should support authentication, database models, admin tools, and structured API development.

### Decision

The backend will be built using Django and Django REST Framework.

### Consequences

Positive:

- Fast backend development
- Built-in admin interface
- Strong ecosystem
- Good fit for business applications

Negative:

- Django can be heavier than smaller frameworks
- The project must be carefuly structured

### Alternatives Considered

FastAPI and ASP.NET where considered, but Django REST Framework was chosen due to its built-in admin, authentication and prior experience with it.

## Use Agent Push Model

### Context

Most client machines will be behind routers, NAT, firewalls or dynamic IP addresses. Requiring the central platform to connect directly to each client machine would make deployment more difficult and less secure. It would be possible to use a VPN, but that would complicate things.

### Decision

The monitoring agent will use an outbound push model.

The agent will periodically send health data to the central API over HTTPS and may ask the server for instructions, which will go together with the answer for said request.

### Consequences

Positive:

- No inbound ports required on client networks
- Works without VPN
- Easier to deploy across many client environments
- Better security posture for small clients

Negative:

- The central platform cannot directly query a machine on demand in the MVP
- Offline detection depends on missing heartbeats
- Agent configuration updates require additional design