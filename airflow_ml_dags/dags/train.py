import airflow

from datetime import timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
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
    dag_id="train",
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
        volumes=volumes,
    )

    preprocess_data = DockerOperator(
        image="airflow-preprocess",
        command="--input-dir=/data/raw/{{ ds }} --output-dir=/data/processed/{{ ds }} --mode=data",
        network_mode="bridge",
        task_id="docker-airflow-preprocess-train",
        do_xcom_push=False,
        # !!! HOST folder(NOT IN CONTAINER) replace with yours !!!
        volumes=volumes,
    )

    preprocess_target = DockerOperator(
        image="airflow-preprocess",
        command="--input-dir=/data/raw/{{ ds }} --output-dir=/data/processed/{{ ds }} --mode=target",
        network_mode="bridge",
        task_id="docker-airflow-preprocess-target",
        do_xcom_push=False,
        # !!! HOST folder(NOT IN CONTAINER) replace with yours !!!
        volumes=volumes,
    )

    train = DockerOperator(
        image="airflow-train",
        command="--input-dir=/data/processed/{{ ds }} --output-dir=/data/models/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-train",
        do_xcom_push=False,
        # !!! HOST folder(NOT IN CONTAINER) replace with yours !!!
        volumes=volumes,
    )

    join_datasets = DummyOperator(task_id="join_datasets", trigger_rule="none_failed")

    download >> preprocess_data
    download >> preprocess_target
    [preprocess_data, preprocess_target] >> join_datasets
    join_datasets >> train
