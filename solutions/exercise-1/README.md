# Build the container
docker build -t myapp:multi-stage .

# Run the container
docker run -p 8080:8080 myapp:multi-stage

# Compare sizes with single-stage build
docker images