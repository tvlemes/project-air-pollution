"""
File: project_tcc.py
Author: Thiago Vilarinho Lemes
Date: 2023-05-13
e-mail: contatothiagolemes@gmail.com
Description: This file is part of the Big Data project to assess Air Pollution.

Project: Air Pollution
"""

def check_file_hdfs_name():
    from snakebite.client import Client
    import os

    path_dst    = os.environ['AIRFLOW__FILE__EXISTS']
    file_name   = 'zxz'
    client = Client("namenode", 9000)
    x = list(client.ls([f'{path_dst}']))
    for i in range(len(x)):
        if file_name in x[i]['path']:
            print('Total de arquivos: ', x[i]['path'])
   
