import requests 
import time 
import json 
from airflow import DAG 
from airflow.operators.python_operator import PythonOperator 
from airflow.operators.python import BranchPythonOperator 
from airflow.operators.dummy import DummyOperator

from datetime import datetime, timedelta 
import pandas as pd 
import numpy as np 
import os


# exercise: write a DAG which is able to request market data for a list of stocks.

# this list should be an input of your function. The functions names are left to help you
# you DAG should only have one task

def get_data(tickers, **kwargs):
    url = 'https://www.alphavantage.co/query'
    api_key = "8VJOC7ZHRYTHZOJ4"
    output_format = '.json'
    output_dir = "/opt/airflow/data_develhope/DATA/DATA_LAKE"
    
    for ticker in tickers:
        params = {'function': 'TIME_SERIES_DAILY_ADJUSTED', 
                  'apikey': api_key,
                  'symbol': ticker
                  }
        
        response = requests.get(url, params)

        if response.status_code == 200:
            json_data = response.json()
            json_data = json.dumps(json_data)
            df = pd.read_json(json_data,orient='records')
            df.to_json(output_dir + f"/{ticker}_{datetime.now().date()}.json")   

# create the DAG which calls the python logic that you had created above
default_dag_args = { 'start_date': datetime(2022, 9, 1), 'email_on_failure': False, 'email_on_retry': False, 'retries': 1, 'retry_delay': timedelta(minutes=5), 'project_id': 1 }

# crontab notation can be useful https://crontab.guru/#0_0_*_*_1
with DAG("market_data_alphavantage_dag", schedule_interval = '@daily', catchup=False, default_args = default_dag_args) as dag_python:
    task_0 = PythonOperator(task_id = "get_market_data", python_callable = get_data, op_kwargs = {'tickers' : ['IBM','AAPL', 'GOOG', 'MSFT']}) 