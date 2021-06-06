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

volumes = ["/Users/alex/my/MADE/semester_2/prod_ml/hw_repo/airflow_ml_dags/data:/data"]

with DAG(
    dag_id="predict",
    start_date=airflow.utils.dates.days_ago(5),
    schedule_interval="@daily",
    default_args=default_args,
) as dag:
    DockerOperator(
        image="airflow-predict",
        command="--input-dir=/data/processed/{{ ds }} --output-dir=/data/predictions/{{ ds }} --model-dir=/data/models/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-predict",
        do_xcom_push=False,
        # !!! HOST folder(NOT IN CONTAINER) replace with yours !!!
        volumes=volumes,
    )
