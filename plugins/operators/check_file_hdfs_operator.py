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
from airflow.plugins_manager import AirflowPlugin
from airflow.models import BaseOperator
import logging as log
from airflow.utils.decorators import apply_defaults
from snakebite.client import Client

'''
## Class CheckFileHdfsOperator ##
'''
class CheckFileHdfsOperator(BaseOperator):

    @apply_defaults
    def __init__(self, path_hdf,  file_name, *args, **kwargs):
        self.path_hdf = path_hdf
        self.file_name = file_name
        super().__init__(*args, **kwargs)

    def execute(self, context):
        PathHdfs = self.path_hdf
        FileName = self.file_name

        log.info("### Check Fil execution starts ###")
        log.info('Check File: %s', FileName)

        client = Client("namenode", 9000)
        x = list(client.ls([PathHdfs + '/' + FileName]))
        if len(x) >= 1:
            for i in range(len(x)):
                if FileName in x[i]['path']:
                    print('Total file(s) found: ', x[i]['path'])
       
        
class CheckFileHdfs(AirflowPlugin):
    name = "check_file_hdfs"
    operators = [CheckFileHdfsOperator]
    sensors = []