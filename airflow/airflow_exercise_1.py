from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator 

#take the dag we built in class and add a last task which removes the dataset_raw.txt from the source folder
default_dag_args = { 'start_date': datetime(2022, 1, 1), 
                    'email_on_failure': False, 
                    'email_on_retry': False, 
                    'retries': 1, 
                    'retry_delay': timedelta(minutes=5), 
                    'project_id': 1 
                    }

#let's define our DAG
try_dag =  DAG("First_DAG",
            schedule_interval = None,
            default_args = default_dag_args)

# here at this level we define our tasks of the DAG
task_0 = BashOperator(task_id = 'bash_task', bash_command = "echo 'command executed from Bash Operator' ", dag = try_dag)
task_1 = BashOperator(task_id = 'bash_task_move_data', bash_command = "cp /opt/airflow/data_develhope/DATA/DATA_LAKE/dataset_raw.txt  /opt/airflow/data_develhope/DATA/CLEAN_DATA", dag = try_dag)
task_2 = BashOperator(task_id = 'bash_task_remove_data', bash_command = "rm /opt/airflow/data_develhope/DATA/DATA_LAKE/dataset_raw.txt", dag = try_dag)

# in the end of your DAG definition, we want to write the dependencies between tasks. >> <<
task_0 >> task_1 >> task_2