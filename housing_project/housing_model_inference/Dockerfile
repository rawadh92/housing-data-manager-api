FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
COPY . .
RUN mkdir -p /app/model
EXPOSE 8001
CMD ["sh", "-c", "python train_model.py && uvicorn predict_api:app --host 0.0.0.0 --port 8001"]
