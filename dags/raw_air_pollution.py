"""
File: raw_air_pollution.py
Author: Thiago Vilarinho Lemes
Date: 2023-05-13
e-mail: contatothiagolemes@gmail.com
Description: This file is part of the Big Data project to assess air pollution.

Project: Air Pollution
"""

'''
References:
Convert Date: https://www.unixtimestamp.com/
'''

def create_raw():

    '''
    ## Importing Libraries ##
    '''
    import requests
    import json
    import pandas as pd
    import datetime
    import os

    '''
    ## Request da API ##
    # Variables - located in /config/var_dags.env 
    '''
    search_weather  =   os.environ['AIRFLOW__SEARCH__WEATHER']
    search_type     =   os.environ['AIRFLOW__SEARCH__TYPE']
    start_date      =   os.environ['AIRFLOW__START__DATE']
    end_date        =   os.environ['AIRFLOW__DATE']
    latitude        =   os.environ['AIRFLOW__LATITUDE']
    longitude       =   os.environ['AIRFLOW__LONGITUDE']
    appid_key       =   os.environ['AIRFLOW__APPID__KEY']
    request         =   requests.get(f'http://api.openweathermap.org/data/2.5/{search_weather}/{search_type}?lat={latitude}&lon={longitude}&start={start_date}&end={end_date}&appid={appid_key}')

    '''
    ##  Converting request to JSON ##
    '''
    data_raw                = json.loads(request.content)
    data_raw

    '''
    ## Formatting the Data ##
    ''' 
    t                       = len(data_raw['list'])
    list_components         = {}
    list_date               = {}
    list_components         = [data_raw['list'][i]['components'] for i in range(t)]
    list_date               = [data_raw['list'][i]['dt'] for i in range(t)] 

    '''
    ## Formatting Date to Timestamp ##
    '''
    list_date               = list(map(lambda x: datetime.datetime.fromtimestamp(x), list_date))
    list_date_day           = list(map(lambda x: x.day, list_date))
    list_date_month         = list(map(lambda x: x.month, list_date))
    list_date_name_month    = list(map(lambda x: x.strftime("%B"), list_date))
    list_date_year          = list(map(lambda x: x.year, list_date))

    '''
    ## Creating Dataframe ##
    '''
    raw_dt                  = pd.DataFrame(list_components, index=list_date)
    raw_dt.index.name       = 'date'
    raw_dt.reset_index()
    raw_dt['day']           = list_date_day
    raw_dt['month']         = list_date_month
    raw_dt['year']          = list_date_year
    raw_dt['name_month']    = list_date_name_month

    '''
    ##  Creating CSV file ##
    # Variable - located in /config/var_dags.env 
    destination_file - path file
    '''
    destination_file = os.environ['AIRFLOW__DESTINATION__FILE']
    raw_dt.to_csv(destination_file, encoding='utf-8')


