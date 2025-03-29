FROM python:3.12.1-slim


ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local'

WORKDIR /app

RUN pip3 install poetry

COPY pyproject.toml ./
COPY src ./src

CMD [ "poetry", "run", "python", "-m", "src.data_ingestion.reddit_stream" ]
