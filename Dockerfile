FROM python:3.9


RUN apt-get update && apt-get -y dist-upgrade
RUN apt install -y netcat


# Python.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Set up app.
RUN mkdir /app
RUN mkdir -p /app/web/static
RUN mkdir -p /app/web/media

WORKDIR /app/


# Setup and install poetry.
ENV POETRY_VERSION=1.0.5
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_CACHE_DIR="/var/cache/pypoetry"


# Install poetry
RUN pip install "poetry==$POETRY_VERSION"
COPY pyproject.toml poetry.lock /app/
RUN poetry install


COPY . .


ENTRYPOINT ["sh", "./docker_entrypoint.sh"]
