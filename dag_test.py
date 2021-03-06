# [START tutorial]
# [START import_module]
from datetime import timedelta
from datetime import datetime as datetime1
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator


import sys
sys.path.append("../temp.py")
from temp import airtask

# [END import_module]


default_args = {
    'owner': 'starstarxx',
    'depends_on_past': False,
    'email': ['2499714067@qq.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
    'start_date': datetime1.now()-timedelta(minutes=1)
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}
# [END default_args]
# [START instantiate_dag]
with DAG(
    'air_pipeline',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(minutes=1),
    catchup=False,
    #start_date=days_ago(2),
    tags=['test'],
) as dag:
    
    task = PythonOperator(
        task_id='run_temp',
        python_callable=airtask,
        dag=dag,
    )
    

    task
# [END tutorial]
