# Automated Multi-Tier Web Application Deployment on AWS

## Project Overview

This project demonstrates the deployment of a containerized multi-tier web application on AWS with an automated CI/CD pipeline using GitHub Actions.

The application consists of a frontend, Flask REST API backend, and MySQL database. Docker and Docker Compose are used for containerization, while Nginx is configured as a reverse proxy.

GitHub Actions automates the build, Docker image publishing, deployment to AWS EC2, and post-deployment health checks.

## Architecture

Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions
    |
    +--------------------+
    |                    |
    v                    v
Build Docker Image    CI/CD Deployment
    |                    |
    v                    v
Docker Hub ----------> AWS EC2
                         |
                    Docker Compose
                    /           \
                   /             \
                  v               v
             Flask Backend      MySQL
                  |
                  v
                Nginx
                  |
                  v
               Frontend

## Technologies Used

- AWS EC2
- Ubuntu Linux
- Docker
- Docker Compose
- Docker Hub
- Git
- GitHub
- GitHub Actions
- Nginx
- Python
- Flask
- MySQL
- REST API
- GitHub Secrets
- CI/CD

## Application Components

### Frontend

The frontend provides the user interface for interacting with the application.

### Backend

The backend is developed using Flask and provides REST API endpoints for application health checks and user management.

Main endpoints:

- GET /
- GET /health
- GET /hello
- GET /users
- POST /users

### Database

MySQL is used to store application user data.

### Nginx

Nginx acts as a reverse proxy and routes application requests to the appropriate service.

## Docker Implementation

The backend application is containerized using Docker.

Docker Compose manages:

- Flask backend container
- MySQL database container
- Persistent MySQL volume
- Network communication between services

Backend:

- Host port: 5001
- Container port: 5000

MySQL:

- Container port: 3306

## CI/CD Pipeline

The project uses GitHub Actions to automate deployment.

### Pipeline Workflow

Developer pushes code
        |
        v
GitHub main branch
        |
        v
GitHub Actions triggered
        |
        v
Checkout source code
        |
        v
Build Docker image
        |
        v
Push image to Docker Hub
        |
        v
Connect to AWS EC2 using SSH
        |
        v
Pull latest code
        |
        v
Deploy using Docker Compose
        |
        v
Wait for backend readiness
        |
        v
Run health checks
        |
        v
Deployment successful

## Deployment Process

1. Developer pushes code to the main branch.
2. GitHub Actions workflow is triggered automatically.
3. Source code is checked out.
4. Docker image is built.
5. Docker image is pushed to Docker Hub.
6. GitHub Actions connects securely to AWS EC2 using SSH.
7. Latest source code is pulled on EC2.
8. Docker Compose deploys the application services.
9. Backend readiness is verified.
10. Backend and Nginx health endpoints are tested.
11. Deployment is marked successful.

## Security

Sensitive credentials are not stored directly in the GitHub Actions workflow.

GitHub Secrets are used for:

- EC2 host
- EC2 username
- EC2 SSH private key
- Docker Hub username
- Docker Hub access token

## Health Checks

The CI/CD pipeline validates the deployment using application health endpoints.

Backend:

http://localhost:5001/health

Nginx:

http://localhost/api/health

The pipeline waits for the backend to become ready before continuing with the remaining tests.

## Project Highlights

- Automated AWS deployment
- Containerized application architecture
- Docker image publishing through Docker Hub
- GitHub Actions CI/CD implementation
- Secure credential management using GitHub Secrets
- Nginx reverse proxy configuration
- Flask REST API
- MySQL database integration
- Automated post-deployment health checks
- Persistent database storage using Docker volumes

## Skills Demonstrated

Cloud:
AWS EC2

DevOps:
Docker, Docker Compose, GitHub Actions, CI/CD, Docker Hub

Web:
Nginx, Flask, REST API

Database:
MySQL

OS & Version Control:
Linux, Git, GitHub

## Project Outcome

The application is successfully deployed on AWS EC2 and can be automatically updated through the GitHub Actions CI/CD pipeline.

Every change pushed to the main branch can trigger the automated build, image publishing, deployment, and health verification process.
