"""
File: move_file_hdfs.py
Author: Thiago Vilarinho Lemes
Date: 2023-05-13
e-mail: contatothiagolemes@gmail.com
Description: This file is part of the Big Data project to assess air pollution.

Project: Air Pollution
"""

'''
References:

'''


def upload_file_hdfs():

    '''
    ## Importing Libraries ##
    '''
    import os
    from airflow.providers.apache.hdfs.hooks.webhdfs import WebHDFSHook