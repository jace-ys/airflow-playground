FROM apache/airflow:1.10.12

USER root

ENV POETRY_VERSION=1.0.10
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="${PATH}:/root/.poetry/bin"

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

USER airflow

COPY ./config/airflow.cfg /opt/airflow/airflow.cfg
COPY ./dags /opt/airflow/dags
