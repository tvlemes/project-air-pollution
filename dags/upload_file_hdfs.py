"""
File: move_file_hdfs.py
Author: Thiago Vilarinho Lemes
Date: 2023-05-13
e-mail: contatothiagolemes@gmail.com
Description: This file is part of the Big Data project to assess air pollution.

Project: Air Pollution
"""

def upload_file_hdfs():

    '''
    ## Importing Libraries ##
    '''
    import os
    from airflow.providers.apache.hdfs.hooks.webhdfs import WebHDFSHook

    '''
    ## File Move HDFS ##
    # Variables - located in /config/var_dags.env 
    hdfs_conn  - connector created in ariflow web
    path_local - file location path
    path_dst   - path in HDFS cluster

    webHDFS_hook - create a connection instance with HDFS
    load_file    - upload local file to HDFS cluster
    '''

    hdfs_conn   = os.environ['AIRFLOW__HDFS__CONN'] 
    path_local  = os.environ['AIRFLOW__PATH__LOCAL'] 
    path_dst    = os.environ['AIRFLOW__PATH_DST']   
    
    webHDFS_hook = WebHDFSHook(webhdfs_conn_id=hdfs_conn)
    webHDFS_hook.load_file(path_local, path_dst, overwrite=True)
