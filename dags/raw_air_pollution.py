"""
File: raw_air_pollution.py
Author: Thiago Vilarinho Lemes
Date: 2023-05-13
e-mail: contatothiagolemes@gmail.com
Description: This file is part of the Big Data project to assess air pollution.

Project: Air Pollution
"""

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
    search_weather          =   os.environ['AIRFLOW__SEARCH__WEATHER']
    search_type             =   os.environ['AIRFLOW__SEARCH__TYPE']
    start_date              =   os.environ['AIRFLOW__START__DATE']
    date_now                =   (datetime.datetime.now())
    date_now                =   datetime.datetime(date_now.year, date_now.month, date_now.day, date_now.hour,date_now.minute, date_now.second)
    date_now                =   str(date_now.timestamp())
    end_date                =   date_now[0:10]
    latitude                =   os.environ['AIRFLOW__LATITUDE']
    longitude               =   os.environ['AIRFLOW__LONGITUDE']
    appid_key               =   os.environ['AIRFLOW__APPID__KEY']
    request                 =   requests.get(f'http://api.openweathermap.org/data/2.5/{search_weather}/{search_type}?lat={latitude}&lon={longitude}&start={start_date}&end={end_date}&appid={appid_key}')
    # print(request)
    '''
    ##  Converting request to JSON ##
    '''
    data_raw                = json.loads(request.content)
    # data_raw

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
    list_hour               = list(map(lambda x: x.hour, list_date))
    '''
    ## Creating Dataframe ##
    '''
    raw_dt = pd.DataFrame(list_components)
    raw_dt['date_period']   = list_date
    raw_dt['date_day']      = list_date_day
    raw_dt['date_month']    = list_date_month
    raw_dt['date_year']     = list_date_year
    raw_dt['name_month']    = list_date_name_month
    raw_dt['date_hour']     = list_hour

    '''
    ##  Creating CSV file ##
    # Variable - located in /config/var_dags.env 
    destination_file - path file
    '''
    destination_file        = os.environ['AIRFLOW__PATH__LOCAL']
    raw_dt.to_csv(destination_file, encoding='utf-8')


