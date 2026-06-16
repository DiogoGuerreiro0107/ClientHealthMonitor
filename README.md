# ClientHealthMonitor
ClientHealthMonitor is an  open-source full-stack monitoring and support platform designed for IT service providers to monitor their business clients' machines, by colleting technical data from said machines and displaying it on a clean and easy to use UI.

To collect the information a lightweight agent is installed on the client machine to send information to the technitian server such as:
- Machine availability
- CPU and memory usage
- Disk space 
- Backup status 
- Database service status
- VPN status and usage
- Etc (the software is projected to be expanded and allow the collection of more precise information for each business needs)

## Core Technologies

### Backend — Django REST Framework

The backend will be developed using **Python**, **Django**, and **Django REST Framework**.

Django was chosen because it provides a solid  foundation for building secure web applications quickly, as it includes built-in support for authentication, database models, admin interfaces and migrations.

**Main responsibilities:**

* Client and machine management
* Agent registration and authentication
* Health data collection
* Alert and incident management
* API endpoints for the frontend
* Integration with automation and AI services

---

### Frontend — React

The frontend will be developed using **React**.

React was chosen because for its easy of use and for its universality. The platform will need to display clients, machines, health status, alerts, incidents, and reports in a clear and interactive way.

**Main responsibilities:**

* Technician dashboard
* Client and machine views
* Health status overview
* Alert and incident pages
* Forms for managing clients, machines, and checks
* Visual representation of system status

---

### Database — PostgreSQL

The main database will be **PostgreSQL**.

PostgreSQL was chosen because it is a powerful, reliable, and widely used relational database.

**Main responsibilities:**

* Store client information
* Store machine and agent records
* Store health check results
* Store alerts and incidents
* Store audit and notification history
* Support reporting and future analytics

---

### Client Agent — Python

The lightweight monitoring agent will initially be developed in **Python**.

Python was chosen because it is fast to develop with, has excellent libraries for system monitoring, and is suitable for building an initial cross-platform agent prototype. The agent will be responsible for collecting technical health information from client machines and sending it to the central API.

For the first version, the agent will focus on read-only monitoring and will not execute remote commands.

**Main responsibilities:**

* Send regular heartbeats to the central API
* Collect CPU, memory, disk, and uptime information
* Check if specific processes are running
* Check Windows service status
* Check backup file age
* Check basic network connectivity
* Report machine health data securely

---

### Background Tasks — Celery and Redis

The project will use **Celery** with **Redis** for background processing.

This was chosen because some tasks should not run directly inside normal API requests. Health evaluation, alert generation, notification handling, AI summaries, and scheduled checks are better handled asynchronously.

Redis will work as the message broker, while Celery workers will process background jobs.

**Main responsibilities:**

* Process incoming health data
* Evaluate alert rules
* Trigger notifications
* Generate periodic reports
* Handle AI summary tasks
* Run scheduled system checks

---

### Automation — n8n

The project will integrate with **n8n** for workflow automation.

n8n was chosen because automation is one of the key areas this project is intended to demonstrate. In real IT support environments, alerts often need to trigger actions such as sending emails, creating tickets, notifying technicians, or generating reports.

Instead of hardcoding every automation inside the application, n8n allows workflows to be created and modified visually.

**Example automations:**

* Send an email when a critical alert is created
* Notify a technician when a client machine goes offline
* Generate a daily health report
* Create a support task when a backup is missing
* Send a summary of unresolved incidents

---

### AI Integration

The project will include AI-assisted features for incident summaries and troubleshooting suggestions.

AI will not be used to replace a technician. Instead, it will be used to help technicians understand issues faster by summarizing health data, alerts, and possible causes.

This reflects a practical use of AI in business and IT operations.

**Possible AI features:**

* Generate technician-friendly incident summaries
* Suggest troubleshooting steps
* Convert technical alerts into client-friendly messages
* Group repeated alerts into a single explanation
* Generate daily support summaries

---

### Containerization — Docker and Docker Compose

The project will use **Docker** and **Docker Compose** for local development and deployment.

Docker was chosen to make the project easier to run consistently across different environments. Since the application includes multiple services, Docker Compose is useful for managing the backend, frontend, database, Redis, Celery workers, and n8n together.

**Services expected in Docker Compose:**

* Backend API
* Frontend application
* PostgreSQL database
* Redis
* Celery worker
* Celery beat scheduler
* n8n
* Nginx reverse proxy, in later stages

---

### CI/CD — GitHub Actions

The project will use **GitHub Actions** for continuous integration.

GitHub Actions was chosen because it integrates directly with the repository and allows automated checks to run whenever code is pushed or a pull request is opened.

**Planned CI tasks:**

* Run backend tests
* Run frontend checks
* Validate formatting
* Check for linting issues
* Build Docker images
* Run basic security checks
* Validate that the project can start successfully

---

### Version Control and Planning — GitHub

The project will use **GitHub** for version control, planning, and progress tracking.

GitHub was chosen because it allows the code, documentation, issues, milestones, pull requests, and project board to stay in one place. This makes the project easier to follow and also allows others to see the development history.

**GitHub will be used for:**

* Source code management
* Issues for tasks and bugs
* Milestones for project phases
* Pull requests for implementation history
* GitHub Projects for progress tracking
* Documentation inside the repository
* Architecture Decision Records inside `/docs/adr`

---

## Documentation

The project will include documentation inside the `/docs` directory.

Documentation is an important part of this project because the goal is not only to build the software, but also to demonstrate planning, architecture, technical reasoning, and maintainability.

Planned documentation:

* Architecture overview
* API design
* Agent design
* Database schema
* Security considerations
* Deployment guide
* n8n workflow examples
* AI integration notes
* Architecture Decision Records

The goal is to build a portfolio project that demonstrates how software, infrastructure, automation, and AI can work together to solve practical operational problems.
