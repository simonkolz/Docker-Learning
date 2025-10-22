# Docker-learning

This repository documents my hands-on learning journey with Docker through two containerized mini-projects.  
Each project demonstrates a different use case and key Docker concepts — from building images and composing services to networking and scaling.

## Projects

1. hello_flask/
   A simple Flask + MySQL app that outputs a basic greeting and the connected MySQL version.  
   It is also pushed to an AWS Elastic Container Registry (ECR) to demonstrate image hosting and pulling.

   What you'll learn:
   - Writing a Dockerfile
   - Building an image and tagging it
   - Pushing to and pulling from AWS ECR
   - Running containers manually
   - Connecting Flask with MySQL in Docker

   Run Instructions:

       # Step into the project folder
       cd hello_flask

       # Build the image locally (if not pulling from ECR)
       docker build -t hello-flask-mysql .

       # OR pull the hosted image from ECR (if you have access)
       docker pull 282378667097.dkr.ecr.eu-west-2.amazonaws.com/flask-mysql:latest

       # Create a custom Docker network
       docker network create my-app-network

       # Run MySQL container
       docker run -d --name mydb --network my-app-network -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:8

       # Run the Flask container
       docker run -p 5002:5002 --network my-app-network hello-flask-mysql

2. CoderCo-docker-challenge/
   A multi-container Docker app using Flask, Redis, and NGINX.  
   It counts how many times a user visits the page and demonstrates container communication, networking, load balancing, and scaling.

   What you'll learn:
   - Docker Compose
   - Flask + Redis integration
   - Using environment variables in containers
   - Load balancing Flask containers with NGINX
   - Docker internal networking (host="redis")
   - Sharing volumes and scaling services

   Run Instructions:

       # Step into the folder
       cd flask-challenge

       # Build and run all services (Flask, Redis, NGINX) together
       docker compose up --build

       # Optional: Scale Flask containers (requires NGINX configured as load balancer)
       docker compose up --build --scale web=3

   Then visit:
       http://localhost:5000        -> The Welcome page
   or
       http://localhost:5000/count  -> The Tracking page
<img width="760" height="416" alt="Screenshot 2025-10-22 at 13 55 55" src="https://github.com/user-attachments/assets/866d2eae-e92f-4d64-a740-06e1893b7542" />

<img width="775" height="550" alt="Screenshot 2025-10-22 at 13 56 28" src="https://github.com/user-attachments/assets/ebeeb7ef-a28c-46b5-8aa8-b8dba5ff6112" />

## Why I Built These

I created these apps to:
- Learn Docker from first principles
- Understand how to build and connect containers
- Document and teach others what each component does
- Practice deploying containerized apps with real-world stacks (Flask, Redis, MySQL, NGINX)

## Tech Stack Summary

| Concept       | hello_flask           | CoderCo-docker-challenge              |
|----------------|------------------------|------------------------------|
| Language       | Python (Flask)         | Python (Flask)              |
| Backend        | MySQL                  | Redis                       |
| Network        | Docker bridge network  | Docker Compose network       |
| Load Balancer  | None                   | NGINX reverse proxy          |
| Hosting        | AWS ECR (optional)     | Local with Compose           |
| Complexity     | Basic (single container)| Intermediate (multi-service) |

