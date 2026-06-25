# Security Considerations

## Table of Contents

- [Purpose](#purpose)
- [Main Principles](#main-principles)
- [Dashboard Authentication](#dashboard-authentication)
- [Agent Security](#agent-security)
- [Data Collected by the Agent](#data-collected-by-the-agent)
- [Remote Actions](#remote-actions)
- [Secrets Management](#secrets-management)

## Purpose

This document describes the main security principles and decisions for this software.

It is important to make sure that the agent can't be used to get unauthorized access to the machine. 

## Main Principles

- Use outbound-only agent communication
- Do not require inbound access to client machines
- Use HTTPS in production
- Store secrets outside source code
- Hash sensitive tokens
- Use role-based access control
- Collect only technical health data
- Avoid collecting business or personal data
- Keep audit logs for important actions

## Dashboard Authentication

Dashboard users will authenticate using JWT-based authentication.

Planned roles:

- Admin
- Technician
- Viewer

Role behavior:

- Admins can manage users, clients, machines, agents and settings
- Technicians can view clients, machines and alerts
- Technicians can update alert status
- Viewers can only read dashboard information

## Agent Security

Agents will authenticate using dedicated agent tokens.

Security requirements:

- Agent registration requires a setup token, which is refreshed from time to time automatically
- Agent tokens are stored hashed in the backend
- Disabled agents cannot send data (even if they send the server will ignore)
- Agent requests must not expose secrets in logs

## Data Collected by the Agent

Allowed data:

- Hostname
- Operating system
- Agent version
- Local IP address
- CPU usage
- CPU temp
- CPU voltage
- Memory usage
- Disk usage
- Uptime
- Process/service/check status
- Backup file age
- Printer/network availability

Data not allowed:

- User documents
- Browser history
- Screenshots
- Keystrokes
- POS sales data
- Customer data
- Invoice data
- Passwords
- Private keys
- Any other personal or business information

## Remote Actions

Remote command execution is out of scope for the MVP.

The first version of the agent is read-only.

Future remote actions, if implemented, must require:

- Explicit authorization
- Audit logging
- Limited predefined actions
- Client consent
- Strong authentication

## Secrets Management

Secrets must be stored in environment variables or local configuration files excluded from Git.

Examples:

- Django secret key
- Database password
- Agent token
- AI API key
- n8n webhook URL