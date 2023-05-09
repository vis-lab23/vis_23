FROM docker.io/library/python:3.10.11-slim as base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
RUN apt-get update
RUN apt-get install -y --no-install-recommends default-libmysqlclient-dev
RUN rm -rf /var/cache/apk/

FROM base as builder-base

RUN apt-get install -y --no-install-recommends build-essential
RUN wget -q -O - -o /dev/null https://install.python-poetry.org | python3 -

WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./pyproject.toml ./
RUN /opt/poetry/bin/poetry  install --only main

FROM base as prod

COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

COPY productmanager code
WORKDIR /code

EXPOSE 8000

COPY ./entrypoint.sh ./entrypoint.sh
RUN chmod a+x /code/entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
