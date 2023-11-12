from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.decorators import task
from datetime import datetime, timedelta

default_args = {
    'owner': 'Peretolchin.YuS',
    'email': ['yuriy.peretolchin@mail.com'],
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'email_on_retry': False,
    'depends_on_past': False,
    'email_on_failure': False,
    'priority_weight': 10,
    'execution_timeout': timedelta(hours=10),
    'dag_run_timeout': timedelta(hours=10)
}

"""
Описание DAG
"""
with DAG(
        dag_id='first_dag',
        schedule_interval='0 19 * * *',
        start_date=datetime(2022, 1, 1),
        catchup=False,
        description=f"""Описание DAG, которое будет видно в airflow""",
        tags=['firs_dag'],
        default_args=default_args
) as dag:
    
    result_firs_task = BashOperator(task_id='firs_task', bash_command=f"python3 /opt/airflow/dags/test.py")

    result_second_task = BashOperator(task_id='second_task', bash_command=f"python3 /opt/airflow/dags/test.py")

    result_theird_task = BashOperator(task_id='theird_task', bash_command=f"python3 /opt/airflow/dags/test.py")

    @task()
    def func_1():
        print("Hello world")

    result_firs_task >> result_second_task >> result_theird_task >> func_1()
