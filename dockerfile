# Dockerfile for housing-api

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install dependencies using Poetry
RUN pip install --no-cache-dir poetry && poetry install

# Expose the port that the app runs on
EXPOSE 8000

# Default command to run the application
CMD ["sh", "-c", "alembic upgrade head && poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000"]