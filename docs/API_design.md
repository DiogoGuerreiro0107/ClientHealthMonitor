# API Design

## Table of Contents

- [Purpose](#purpose)
- [API Consumers](#api-consumers)
- [Authentication Types](#authentication-types)
  - [Dashboard User Authentication](#dashboard-user-authentication)
  - [Agent Authentication](#agent-authentication)
- [Initial Endpoint Groups](#initial-endpoint-groups)
  - [Authentication](#authentication)
  - [Clients](#clients)
  - [Locations](#locations)
  - [Machines](#machines)
  - [Agents](#agents)
  - [Monitoring](#monitoring)
  - [Alerts](#alerts)
- [Standard Response Format](#standard-response-format)
  - [Error Response](#error-response)

## Purpose

The API provides the endpoints to communicate with the server and get the information needed.

The API is built using Django REST Framework.

## API Consumers

The API is used by:

- React frontend dashboard
- Python monitoring agents
- Background workers
- Automation integrations

## Authentication Types

The platform will use two different authentication flows:

### Dashboard User Authentication

Used by administrators, technicians, and viewers.

Planned method:

- JWT access token
- JWT refresh token
- Role-based permissions

### Agent Authentication

Used by installed monitoring agents.

Planned method:

- Agent registration token for initial setup
- Long-lived agent API token after registration
- Token stored hashed in the backend
- Token sent by the agent in API requests
- Agent will refresh token from time to time

## Initial Endpoint Groups

### Authentication

| Method | Endpoint             | Description                                    |
| ------ | -------------------- | ---------------------------------------------- |
| `POST` | `/api/auth/login/`   | Authenticate a user and create a session/token |
| `POST` | `/api/auth/refresh/` | Refresh authentication credentials             |
| `POST` | `/api/auth/logout/`  | Log out the current user                       |
| `GET`  | `/api/auth/me/`      | Retrieve the authenticated user profile        |

### Clients

| Method   | Endpoint             | Description                |
| -------- | -------------------- | -------------------------- |
| `GET`    | `/api/clients/`      | List clients               |
| `POST`   | `/api/clients/`      | Create a new client        |
| `GET`    | `/api/clients/{id}/` | Retrieve a specific client |
| `PATCH`  | `/api/clients/{id}/` | Update a specific client   |
| `DELETE` | `/api/clients/{id}/` | Delete a specific client   |

### Locations

| Method   | Endpoint               | Description                  |
| -------- | ---------------------- | ---------------------------- |
| `GET`    | `/api/locations/`      | List locations               |
| `POST`   | `/api/locations/`      | Create a new location        |
| `GET`    | `/api/locations/{id}/` | Retrieve a specific location |
| `PATCH`  | `/api/locations/{id}/` | Update a specific location   |
| `DELETE` | `/api/locations/{id}/` | Delete a specific location   |

### Machines

| Method   | Endpoint              | Description                 |
| -------- | --------------------- | --------------------------- |
| `GET`    | `/api/machines/`      | List machines               |
| `POST`   | `/api/machines/`      | Create a new machine        |
| `GET`    | `/api/machines/{id}/` | Retrieve a specific machine |
| `PATCH`  | `/api/machines/{id}/` | Update a specific machine   |
| `DELETE` | `/api/machines/{id}/` | Delete a specific machine   |

### Agents

| Method  | Endpoint                    | Description               |
| ------- | --------------------------- | ------------------------- |
| `POST`  | `/api/agents/register/`     | Register a new agent      |
| `POST`  | `/api/agents/heartbeat/`    | Submit an agent heartbeat |
| `GET`   | `/api/agents/`              | List agents               |
| `GET`   | `/api/agents/{id}/`         | Retrieve a specific agent |
| `PATCH` | `/api/agents/{id}/`         | Update a specific agent   |
| `GET`   | `/api/agents/disable/{id}/` | Disable a specific agent  |

### Monitoring

| Method | Endpoint                  | Description                   |
| ------ | ------------------------- | ----------------------------- |
| `GET`  | `/api/health-snapshots/`  | List health snapshots         |
| `GET`  | `/api/check-results/`     | List check results            |

### Alerts

| Method  | Endpoint                        | Description               |
| ------- | ------------------------------- | ------------------------- |
| `GET`   | `/api/alerts/`                  | List alerts               |
| `GET`   | `/api/alerts/{id}/`             | Retrieve a specific alert |
| `PATCH` | `/api/alerts/{id}/`             | Update a specific alert   |
| `POST`  | `/api/alerts/{id}/acknowledge/` | Acknowledge an alert      |
| `POST`  | `/api/alerts/{id}/resolve/`     | Resolve an alert          |

---

## Standard Response Format

### Error Response

Errors are returned using an error object with the follwing format:

```json
{
  "error": {
    "code": "validation_error",
    "message": "Invalid request data",
    "details": {}
  }
}
```
