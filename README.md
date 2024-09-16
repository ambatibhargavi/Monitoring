# Centralized Logging and Monitoring System for Microservices
Project Overview
This project showcases how to create a centralized monitoring system for microservices using Docker, Prometheus, and Grafana. The system helps observe the microservices in real-time, allowing for better system performance analysis, debugging, and enhanced reliability.

Tools Used
Docker: Used to containerize the microservices.
Flask: A lightweight Python web framework for building the microservices.
Prometheus: Responsible for collecting metrics from your microservices, such as CPU usage, memory consumption, and custom application metrics.
Grafana: Provides visualization for the metrics collected by Prometheus through customizable dashboards.
Project Structure
The project structure provides a clear organization of your microservices and configurations:

                
│----- app.py                
│----- Dockerfile      
|------ prometheus.yaml
|------ requirements.txt
|------- Docker-compose.yaml

