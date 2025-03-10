# Stage 1: Build the frontend
FROM node:16 AS frontend-build
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Build the backend
FROM python:3.9-slim AS backend-build
WORKDIR /app/backend
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ ./
# If there's any build step for the backend, it would go here

# Stage 3: Production image
FROM nginx:alpine
WORKDIR /app

# Copy the frontend build
COPY --from=frontend-build /app/frontend/build /usr/share/nginx/html

# Copy the backend
COPY --from=backend-build /app/backend /app/backend

# Install Python runtime for the backend
RUN apk add --no-cache python3 py3-pip && \
    pip3 install --no-cache-dir -r /app/backend/requirements.txt

# Configure nginx to serve frontend and proxy API requests
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Start both services
COPY start.sh /app/
RUN chmod +x /app/start.sh
CMD ["/app/start.sh"]