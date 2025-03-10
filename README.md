# Docker and DevOps Exercises

## Exercise 1: Multi-Stage Docker Build for a Java Application

**Objective:** Create an optimized Docker image for a Java application using multi-stage builds.

**Instructions:**

1. Create a simple Spring Boot application or use an existing one
2. Write a Dockerfile with two stages:
   - Stage 1: Use `maven:3.8-openjdk-17` as the build image
   - Stage 2: Use `openjdk:17-jre-slim` as the production image

3. In the first stage, copy your source code, run Maven to build the JAR
4. In the second stage, copy only the built JAR from the first stage
5. Configure the proper entrypoint to run the application
6. Build and run your container
7. Compare the image size with a single-stage build

**Success Criteria:**

- The application runs correctly in the container
- The multi-stage image is significantly smaller than a single-stage version
- No build tools or source code exists in the final image

## Exercise 2: Multi-Stage Docker Build with Frontend and Backend

**Objective:** Create a multi-stage build for a full-stack application with separate frontend and backend components.

**Instructions:**

1. Use a simple application with a Node.js/React frontend and a Python/Flask backend
2. Create a Dockerfile with three stages:
   - Stage 1: Build the frontend using `node:16` as base
   - Stage 2: Build the backend using `python:3.9` as base
   - Stage 3: Create a production image using `nginx:alpine` for serving both

3. In the first stage, install dependencies and build the frontend
4. In the second stage, install Python dependencies
5. In the final stage, copy the built frontend assets to serve statically
6. Copy the backend code and configure nginx to proxy API requests
7. Build and run the container

**Success Criteria:**

- The application works end-to-end with proper communication between frontend and backend
- The final image is optimized for production with minimal size
- Build tools and source code only exist in their respective build stages

## Exercise 3: Multi-Platform Container Images with Buildx

**Objective:** Build and publish container images that run on multiple CPU architectures.

**Instructions:**

1. Create a simple application (e.g., a Python web server)
2. Set up Docker Buildx with proper emulation support
3. Create a Dockerfile compatible with multiple architectures
4. Build for ARM64, AMD64, and ARM/v7 platforms in a single command
5. Test your image on different platforms (using emulation if needed)
6. Push to a container registry with proper platform manifests

**Success Criteria:**

- Successfully build one image for multiple platforms
- Verify the image can run on different architectures
- Properly tag and publish the multi-platform image
- Demonstrate pulling the correct architecture automatically

## Exercise 4: Microservices Development Environment with Docker Compose

**Objective:** Create a complete development environment for a microservices application using Docker Compose.

**Instructions:**

1. Design a system with at least 3 services:
   - A web frontend
   - An API service
   - A database

2. Write individual Dockerfiles for each custom service
3. Create a `docker-compose.yml` file that:
   - Defines all services with proper dependencies
   - Sets up a custom network
   - Configures persistent volumes for the database
   - Includes environment variables for configuration
   - Implements healthchecks for critical services

4. Add Docker Compose overrides for development vs. production environments
5. Implement proper logging configuration

**Success Criteria:**

- All services start and communicate properly
- Data persists between container restarts
- Development mode enables features like hot reloading
- Proper service discovery works between containers
- The application can be started with a single command

Each of these exercises builds upon core Docker concepts while introducing more advanced practices that are essential in professional DevOps environments. The progression helps learners understand how these technologies fit together in real-world scenarios.