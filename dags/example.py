from datetime import datetime, timedelta
from logging import info

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def add():
    info(f"2 + 2 = {2 + 2}")


def subtract():
    info(f"2 - 2 = {2 - 2}")


dag = DAG(
    "add_subtract",
    start_date=datetime.now() - timedelta(days=1),
    schedule_interval="@hourly",
)

t0 = PythonOperator(task_id="add", python_callable=add, dag=dag)
t1 = PythonOperator(task_id="subtract", python_callable=subtract, dag=dag)

t0 >> t1
