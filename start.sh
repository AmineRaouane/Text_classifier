#!/bin/bash

# Production startup script for the Text Classification API
# Optimized for Render.com deployment

set -e

echo "Starting Text Classification API..."

# Check if model files exist
if [ ! -f "model/model.h5" ]; then
    echo "Error: model/model.h5 not found!"
    exit 1
fi

if [ ! -f "model/tokenizer.json" ]; then
    echo "Error: model/tokenizer.json not found!"
    exit 1
fi

# Set default environment variables if not set
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8000}
export LOG_LEVEL=${LOG_LEVEL:-INFO}

echo "Configuration:"
echo "  Host: $HOST"
echo "  Port: $PORT"
echo "  Log Level: $LOG_LEVEL"

# Start the application with Uvicorn (recommended for Render)
echo "Starting with Uvicorn..."
exec uvicorn main:app \
    --host $HOST \
    --port $PORT \
    --log-level $LOG_LEVEL.lower()
