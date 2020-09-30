[![ci-badge]][ci-workflow]

[ci-badge]: https://github.com/jace-ys/airflow-playground/workflows/ci/badge.svg
[ci-workflow]: https://github.com/jace-ys/airflow-playground/actions?query=workflow%3Aci

# Airflow Playground

A playground repository for learning Airflow.

## Requirements

- `python v3.6.12+`
- `poetry v1.0+`
- `docker v19.03+`
- `docker-compose v1.25.5+`

## Getting Started

#### Configuration

1. Define your base Airflow configuration in [config/airflow.cfg](config/airflow.cfg), as documented in [Configuration Reference](https://airflow.apache.org/docs/stable/configurations-ref.html). This should contain the default configuration to be applied to all instances of Airflow.

2. Define your per-environment Airflow configuration in `airflow.env` located in either [config/dev](config/dev) or [config/prd](config/prd), using the environment variable syntax described in [Setting Configuration Options](https://airflow.apache.org/docs/stable/howto/set-config.html). These values will overwrite the default configuration defined in `config/airflow.cfg`.

#### Running Airflow Locally

1. To spin up the Airflow and Postgres containers:

   ```shell
   docker-compose up -d
   ```

2. If you have added new dependencies to `pyproject.toml` or modified configuration in `config/airflow.cfg`, you will need to rebuild the Docker image for your changes to take effect.

   To rebuild and restart the containers:

   ```shell
   docker-compose up -d --build
   ```

3. To exec into the Airflow `scheduler` container and run `airflow` commands:

   ```shell
   make exec
   airflow --help
   ```

4. To teardown the containers when you're done:

   ```shell
   docker-compose down -v
   ```

#### Developing DAGs

1. New DAGs should be created in the [dags](dags) folder. These will get mounted as volumes and loaded automatically into the Airflow containers, aiding the rapid development of DAGs locally.

2. To install a Python package:

   ```shell
   poetry add [package]
   docker-compose up -d --build
   ```

3. To run the test suites:

   ```shell
   make test
   ```

4. To run the code formatter:

   ```shell
   make fmt
   ```
