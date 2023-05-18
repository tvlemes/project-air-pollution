from airflow.plugins_manager import AirflowPlugin
from airflow.models import BaseOperator
import logging as log
from airflow.utils.decorators import apply_defaults


class DataTransferOperator(BaseOperator): # Cada operator deve herdar uma classe

    # Inicializando o construtor
    # source_file_path - caminho de origem
    # dest_file_path - caminho de destino
    # delete_list - lista para esr deletado
    @apply_defaults # aplica as propriedades da DAG, start_date, owner...
    def __init__(self, source_file_path, dest_file_path, delete_list, *args, **kwargs):
        self.source_file_path = source_file_path
        self.dest_file_path = dest_file_path
        self.delete_list = delete_list
        super().__init__(*args, **kwargs)


    def execute(self, context):

        SourceFile      = self.source_file_path
        DestinationFile = self.dest_file_path
        DeleteList      = self.delete_list

        log.info("### custom operator execution starts ###")
        log.info('source_file_path: %s', SourceFile)
        log.info('dest_file_path: %s', DestinationFile)
        log.info('delete_list: %s', DeleteList)

        fin = open(SourceFile)
        fout = open(DestinationFile, "a")

        for line in fin:
            log.info('### reading line: %s', line)
            for word in DeleteList:
                log.info('### matching string: %s', word)
                line = line.replace(word, "")

            log.info('### output line is: %s', line)
            fout.write(line)

        fin.close()
        fout.close()

class DemoPlugin(AirflowPlugin):
    name = 'demo_plugin'
    operators = [DataTransferOperator]
    sensors = []