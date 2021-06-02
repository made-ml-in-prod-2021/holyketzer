import airflow

from datetime import timedelta
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "admin",
    "email": ["admin@example.com"],
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="generate_data",
    start_date=airflow.utils.dates.days_ago(5),
    schedule_interval="@daily",
    default_args=default_args,
) as dag:
    download = DockerOperator(
        image="airflow-download",
        command="/data/raw/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-download",
        do_xcom_push=False,
        # !!! HOST folder(NOT IN CONTAINER) replace with yours !!!
        volumes=["/Users/alex/my/MADE/semester_2/prod_ml/hw_repo/airflow_ml_dags/data:/data"]
    )

    download
