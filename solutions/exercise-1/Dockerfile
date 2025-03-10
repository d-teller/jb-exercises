# Stage 1: Build stage
FROM maven:3.8-openjdk-17 AS build
WORKDIR /app

# Copy pom.xml first to leverage Docker cache for dependencies
COPY pom.xml .
RUN mvn dependency:go-offline

# Copy source code and build the application
COPY src/ ./src/
RUN mvn package -DskipTests

# Stage 2: Production stage
FROM openjdk:17-jre-slim
WORKDIR /app

# Copy only the built JAR from the build stage
COPY --from=build /app/target/*.jar app.jar

# Configure health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=15s --retries=3 \
  CMD wget -q -O /dev/null http://localhost:8080/actuator/health || exit 1

# Run the application
ENTRYPOINT ["java", "-jar", "app.jar"]