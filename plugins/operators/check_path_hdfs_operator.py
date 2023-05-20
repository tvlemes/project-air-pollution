from airflow.plugins_manager import AirflowPlugin
from airflow.models import BaseOperator
import logging as log
from airflow.utils.decorators import apply_defaults
from snakebite.client import Client

class CheckPathHdfsOperator(BaseOperator):

    @apply_defaults
    def __init__(self, path_hdf,  *args, **kwargs):
        self.path_hdf = path_hdf
        super().__init__(*args, **kwargs)

    def execute(self, context):
        PathHdfs = self.path_hdf

        log.info("### Check Path execution starts ###")
        log.info('Check Path: %s', PathHdfs)

        client = Client("namenode", 9000)
        x = list(client.count([PathHdfs]))
        if x[0]['fileCount'] >= 1:
            print('Total file(s): ', x[0]['fileCount'])
        else:
            raise Exception(f'It does not exist in the directory.')

class CheckPathHdfs(AirflowPlugin):
    name = "check_path_hdfs"
    operators = [CheckPathHdfsOperator]
    sensors = []