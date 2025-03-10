# For development (uses docker-compose.yml + docker-compose.override.yml by default)
docker-compose up -d

# For production
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

# Viewing logs
docker-compose logs -f

# Stopping the environment
docker-compose down

# Stopping and removing volumes
docker-compose down -v