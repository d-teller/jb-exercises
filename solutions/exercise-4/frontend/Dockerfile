FROM node:16-alpine

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# For development (will be overridden in docker-compose)
CMD ["npm", "start"]

# For production
# RUN npm run build
# FROM nginx:alpine
# COPY --from=0 /app/build /usr/share/nginx/html