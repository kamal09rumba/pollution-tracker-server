# Creating a python base with shared environment variables
FROM python:3.11-bullseye AS python-base

# Non interactive frontend
ENV DEBIAN_FRONTEND=noninteractive

# Install requiremnts for python3.9
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    software-properties-common \
    git \
    curl \
    build-essential \
    libsqlite3-mod-spatialite \
    gdal-bin \
    gettext

ENV POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

# Add poetry home to path
ENV PATH="$POETRY_HOME/bin:$PATH"

# Install virtualenv
RUN pip install -U virtualenv

# Install Poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python

# Development stage
FROM python-base AS development

WORKDIR /code

ENTRYPOINT ["/code/docker/entrypoint.sh"]