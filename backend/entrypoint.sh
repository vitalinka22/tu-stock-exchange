#!/bin/bash
set -e

# Wait for database to be ready
echo "Waiting for database to be ready..."
until nc -z db 5432; do
  sleep 2
  echo "Still waiting for database..."
done
echo "Database is ready!"

# Run the data population script
echo "Populating database with mock data..."
python populate_data.py

# Start the application
echo "Starting the application..."
exec uvicorn main:app --host 0.0.0.0 --port 8000 --reload