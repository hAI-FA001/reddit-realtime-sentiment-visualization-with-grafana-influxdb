FROM python:3.12-slim

WORKDIR /app

COPY poetry.lock pyproject.toml ./
COPY src ./src

RUN pip install poetry && poetry install --no-root

CMD [ "poetry", "run", "python", "-m", "src.data_ingestion.reddit_stream" ]
