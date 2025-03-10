#!/bin/sh
# Start the Python API server in the background
cd /app/backend && python app.py &

# Start nginx in the foreground
nginx -g "daemon off;"