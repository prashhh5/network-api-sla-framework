# Network & API SLA Monitoring Framework 📡

Automated network service health checker and SLA performance auditor. Built with Python, PyTest, and Docker to test RESTful microservices, monitor packet latency, and detect network degradation.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![PyTest](https://img.shields.io/badge/PyTest-Automated-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)

---

## 🏗 System Flow

```mermaid
graph LR
    A[SLA Test Suite] --> B[Target Microservice]
    B --> C{HTTP Response}
    C -- 200 OK & Latency < 2s --> D[SLA Passed]
    C -- Timeout / 5xx Error --> E[SLA Alert & Failure Report]
