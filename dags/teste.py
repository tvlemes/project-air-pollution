from datetime import datetime
import os
from snakebite.client import Client


y = (datetime.now())
x = datetime.fromtimestamp(1684008783)
print(x.day)
m = x.strftime("%B")
print(m)
print(x.year)
print(x)



path_hdf         = os.environ['AIRFLOW__FILE__EXISTS']
file_name        = '/raw_air_pollution1.csv'

client = Client("namenode", 9000)
x = list(client.ls([path_hdf+file_name]))
print(len(x))
if len(x) >= 1:
    for i in range(len(x)):
        if file_name in x[i]['path']:
            print('Total file(s) found: ', x[i]['path'])
        
