"""
File: project_tcc.py
Author: Thiago Vilarinho Lemes
Date: 2023-05-13
e-mail: contatothiagolemes@gmail.com
Description: This file is part of the Big Data project to assess Air Pollution.

Project: Air Pollution
"""

def check_file_hdfs():
    from snakebite.client import Client
    import os

    path_dst = os.environ['AIRFLOW__FILE__EXISTS']

    client = Client("namenode", 9000)
    x = list(client.count([f'{path_dst}']))
    print('Total de arquivos: ', x[0]['fileCount'])
    if x[0]['fileCount'] >= 1:
        print('Total de arquivos: ', x[0]['fileCount'])
    else:
        raise Exception(f'Não existe arquivos no diretório.')
