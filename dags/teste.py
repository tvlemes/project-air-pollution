from datetime import datetime
import os
from snakebite.client import Client
import requests
import json
import pandas as pd
from datetime import datetime


date_now = (datetime.now())
date_now = datetime(date_now.year, date_now.month, date_now.day, date_now.hour,date_now.minute, date_now.second)
date_now = str(date_now.timestamp())
date_now = date_now[0:10]

request =   requests.get(f'http://api.openweathermap.org/data/2.5/air_pollution/history?lat=-10.186&lon=-48.333&start=1609470000&end={date_now}&appid=751d15d739b39f5b27cbfa029a4ba68a')

data_raw                = json.loads(request.content)
# print(data_raw)
t                       = len(data_raw['list'])

print(t)

# print(x.day)
# m = x.strftime("%B")
# print(m)
# print(x.year)
# print(x)



# data = datetime.now()

# print(data)