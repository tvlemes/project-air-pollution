"""
File: project_tcc.py
Author: Thiago Vilarinho Lemes
Date: 2023-05-13
e-mail: contatothiagolemes@gmail.com
Description: This file is part of the Big Data project to assess Air Pollution.

Project: Air Pollution
"""

'''
## Importing Libraries ##
'''
from airflow import DAG
from airflow.operators.bash_operator import BashOperator 
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime, timedelta
from upload_file_hdfs import upload_file_hdfs
from raw_air_pollution import create_raw
from operators.check_path_hdfs_operator import CheckPathHdfsOperator
from operators.check_file_hdfs_operator import CheckFileHdfsOperator
import os

'''
## DAG parameters ##
'''
default_args = {
    "owner": "airflow",
    "depends_on_past": False, 
    "email_on_failure": False,
    "start_date": datetime(2023, 5, 20),
    "retries": 2,
    "retry_delay": timedelta(seconds=5),
}


'''
# Variables - located in /config/var_dags.env
destination_file - path file
'''
destination_file = os.environ['AIRFLOW__PATH__LOCAL']
path_hdf         = os.environ['AIRFLOW__PATH__HDFS']
file_name        = os.environ['AIRFLOW__FILE__NAME']


'''
## Instantiating the DAG ##
'''
dag = DAG('dag_project_air_pollution', default_args=default_args, template_searchpath=['/usr/local/airflow/sql_files'], schedule_interval=timedelta(1))

# Start
td = DummyOperator(task_id='Start', dag=dag)

# 1° task - Data Request
t1 = PythonOperator(task_id='request_data_air_pollution', python_callable=create_raw, dag=dag)

# 2° task - Check File Exists
t2 = BashOperator(task_id="check_file_exists", bash_command=f"shasum {destination_file}", dag=dag)

# 3° task - Data Move
t3 = PythonOperator(task_id='move_file_hdfs_raw', python_callable=upload_file_hdfs, dag=dag)

# 4° task - Check file in HDFS
t4 = CheckPathHdfsOperator(task_id='check_path_exists_hdfs', path_hdf=path_hdf, dag=dag)

t5 = CheckFileHdfsOperator(
    task_id='check_file_exists_hdfs', 
    path_hdf=path_hdf, 
    file_name = file_name,
    dag=dag)

t6 = PostgresOperator(
    task_id='create_table_postgres',
    postgres_conn_id='postgres_conn',
    sql='create_table.sql',
    dag=dag
)

t7 = PostgresOperator(
    task_id='insert-data_postgres',
    postgres_conn_id='postgres_conn',
    sql='insert_into_table.sql',
    dag=dag
)

# End
te = DummyOperator(task_id='End', dag=dag)

td >> t1 >> t2 >> t3 >> [t4, t5] >> t6 >> t7 >> te