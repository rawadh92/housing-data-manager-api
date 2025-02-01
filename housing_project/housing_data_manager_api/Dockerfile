# Dockerfile for housing-data-manager-api
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
EXPOSE 8001
CMD ["sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8001 --reload"]
