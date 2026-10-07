# Deployment Activity 4 - Task 4 Deploy containers using Docker

## Project Overview

This repository contains the source code and Docker configurations for Deployment Portfolio Task 4:

* **Task 4.1 (Pass):** Docker environment verification using the canonical `hello-world` image.
* **Task 4.2 (Credit):** Python Flask web server deployed locally and pulled to a secondary Docker device (Iximiuz Labs).
* **Task 4.3 (Distinction):** "PyDone", an interactive To-Do list web application built with Flask and HTML/CSS.
* **Task 4.4 (High Distinction):** "Medicare Clinical Appointment System", a non-web-based console (CLI) application deployed to Docker.
---

## Repository Structure

```text
SWE40006-Deployment-Portfolio-Task-4/
├── Task4.2/        # Python Diagnostic Web Server 
├── Task4.3/        # PyDone To-Do Web Application 
├── Task4.4/        # Medicare Clinical Appointment CLI Application 
└── README.md       # Project documentation and deployment instructions
```

---

## Execution Command

Run each app directly from Docker Hub. The only requirement is [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

### Task 4.2 – Flask Hello App

```bash
docker pull cremy212/flask-hello-app:latest
docker run -d -p 5000:5000 --name flask-web-server cremy212/flask-hello-app:latest
```

Open <http://localhost:5000>

### Task 4.3 – PyDone To-Do App

```bash
docker pull cremy212/pydone-todo-app:v1.0
docker run -d -p 5001:5001 --name pydone-web-container cremy212/pydone-todo-app:v1.0
```

Open <http://localhost:5001>

### Task 4.4 – Medicare Clinical Appointment System (CLI)

```bash
docker pull cremy212/hospital-cli-app:v1.0
docker run -it --name hospital-system cremy212/hospital-cli-app:v1.0
```

### Stop and Remove

```bash
docker rm -f flask-web-server pydone-web-container hospital-system
```
