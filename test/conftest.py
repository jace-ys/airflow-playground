import os

from airflow.models import DagBag
import pytest


@pytest.fixture(scope="session")
def dag_bag():
    return DagBag(
        include_examples=False,
        dag_folder=f"{os.getcwd()}/dags",
    )
