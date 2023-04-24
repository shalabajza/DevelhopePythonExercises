from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator 

default_dag_args = { 'start_date': datetime(2022, 1, 1), 
                    'email_on_failure': False, 
                    'email_on_retry': False, 
                    'retries': 1, 
                    'retry_delay': timedelta(minutes=5), 
                    'project_id': 1 
                    }

try_dag =  DAG("First_DAG",
            schedule_interval = None,
            default_args = default_dag_args)

task_1 = BashOperator(task_id = 'bash_task_move_data', bash_command = "cp /opt/airflow/data_develhope/DATA/DATA_LAKE/dataset_raw.txt  /opt/airflow/data_develhope/DATA/CLEAN_DATA && rm /opt/airflow/data_develhope/DATA/DATA_LAKE/dataset_raw.txt", dag = try_dag)
task_2 = BashOperator(task_id = 'bash_task', bash_command = "echo 'We did it boys, dataset_raw.txt is no more. Long live dataset_raw.txt' ", dag = try_dag)

task_1 >> task_2