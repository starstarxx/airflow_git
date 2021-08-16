


# [START tutorial]
# [START import_module]
from datetime import timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago



import sys
sys.path.append("../temp.py")
from temp import airtask

# [END import_module]


default_args = {
    'owner': 'starstarxx',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
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
def print_context():
    """Print the Airflow context and ds variable from the context."""
    print(1)
    print(1)
    return 'Whatever you return gets printed in the logs'

# [START instantiate_dag]
with DAG(
    'airflow_pipeline',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['test'],
) as dag:
    # [END instantiate_dag]




    # t1, t2 and t3 are examples of tasks created by instantiating operators
    # [START basic_task]
    t1 = PythonOperator(
        task_id = '111',
        python_callable=print_context,
        dag=dag,
    )

    

    t1
# [END tutorial]
