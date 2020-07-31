from html5print import HTMLBeautifier
from selenium import webdriver
filename = 'currentHourFileAlpha.txt'


import json
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
data = json.dumps({
    "success":True,
        "data":[
            {

                "record_id":258585618,
                "timestamp":"2018-01-21 22:34:34",
                "bytes":29466,

            }
            ,
            {
                "record_id":258585604,
                "timestamp":"2018-01-21 22:33:14",
                "bytes":37892,
            }
            ,
            {
                "record_id":258584399,
                "timestamp":"2018-01-21 22:37:40",
                "bytes":36396,
            }
        ]
    })

data = json.loads(data)
dates = [i['timestamp'] for i in data["data"]]
values = [i['bytes'] for i in data['data']]

df = pd.DataFrame({'dates':dates, 'values':values})
df['dates']  = [pd.to_datetime(i) for i in df['dates']]

print(df.sort_values(by='dates'))


plt.bar(dates, values)