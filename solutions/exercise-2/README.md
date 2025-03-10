# Build the container
docker build -t fullstack-app:latest .

# Run the container
docker run -p 80:80 fullstack-app:latest