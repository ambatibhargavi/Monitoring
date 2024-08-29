# Centralized Logging and Monitoring System for Microservices
Project Overview
This project demonstrates how to set up a centralized logging and monitoring system for microservices using Docker, ELK Stack (Elasticsearch, Logstash, Kibana), Prometheus, and Grafana. The system allows for real-time observability and monitoring of microservices, enabling better debugging, performance analysis, and system reliability.

Tools Used
Docker: Containerization of microservices.
Flask: Lightweight web framework for building the microservices.
Elasticsearch: Log storage and search engine.
Logstash: Log collection and parsing (can be replaced by Fluentd).
Kibana: Visualization and analysis of logs.
Prometheus: Metrics collection and monitoring.
Grafana: Visualization of metrics through customizable dashboards.
Project Structure
bash
Copy code
├── service1/                # Microservice 1
│   ├── app.py               # Flask application for service 1
│   ├── Dockerfile           # Dockerfile for service 1
├── service2/                # Microservice 2
│   ├── app.py               # Flask application for service 2
│   ├── Dockerfile           # Dockerfile for service 2
├── docker-compose.yml       # Docker Compose file to run the entire stack
└── README.md                # Project documentation
