# Set up a new builder that supports multi-platform builds
docker buildx create --name mybuilder --use

# Build and push to a registry (e.g., Docker Hub)
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 \
  -t username/multiarch-app:latest \
  --push .

# To build and load locally (recent Docker versions)
docker buildx build --platform linux/amd64,linux/arm64 \
  -t multiarch-app:latest \
  --load .

# Test the image (it will pull the right architecture)
docker run -p 8080:8080 username/multiarch-app:latest

```sh
# Inspect the image manifest
docker buildx imagetools inspect username/multiarch-app:latest

# Sample output:
# Name: docker.io/username/multiarch-app:latest
# MediaType: application/vnd.docker.distribution.manifest.list.v2+json
# Digest: sha256:...
# 
# Manifests:
#   Name: docker.io/username/multiarch-app:latest@sha256:...
#   MediaType: application/vnd.docker.distribution.manifest.v2+json
#   Platform: linux/amd64
# 
#   Name: docker.io/username/multiarch-app:latest@sha256:...
#   MediaType: application/vnd.docker.distribution.manifest.v2+json
#   Platform: linux/arm64
# 
#   Name: docker.io/username/multiarch-app:latest@sha256:...
#   MediaType: application/vnd.docker.distribution.manifest.v2+json
#   Platform: linux/arm/v7
```