from html5print import HTMLBeautifier
from selenium import webdriver
import requests
import dweepy
import json
import pprint
from datetime import date
import datetime
import time
import pytz
from pytz import timezone
from HourSourceCodeRecieve import recieveSourceFunction, filename
import HourSourceCodeRecieve
from reset_all import reset_all_readings
import math
count = 0
resettoday = 0
#running the source code ripper
while count != 9999:
    try:
        timeformat = (datetime.datetime.now(pytz.timezone('Asia/Singapore')))

        today1 = datetime.datetime.now().time()
        
        

        HourSourceCodeRecieve.recieveSourceFunction()   
        #opening txt file, setting up variable lines, when printing (lines[548]) we get line 549 output
        sourceCodeVariableRip = open(filename, 'r+')
        lines = sourceCodeVariableRip.readlines()

        currentDailyWatts = (lines[548].strip().rstrip())
        print(f"{currentDailyWatts} The Watts Gotten Today ie Daily")
        currentDailyCarbonSaved = lines[3420].strip().rstrip()
        print(f"{currentDailyCarbonSaved} The Carbon Saved Today ie Daily")
        monthlyWatts = lines[558].strip().rstrip()
        print(f"{monthlyWatts} The Watts Gotten this Month ie Monthly")
        yearlyWatts = lines[568].strip().rstrip()
        print(f"{yearlyWatts} The Watts gotten this Year ie Yearly")

        intmonwatts = int(float(monthlyWatts))
        monthlyCarbonSaved = intmonwatts * 0.42 + 0.001 

        intyrwatts = int(float(yearlyWatts))
        yearlyCarbonSaved = intyrwatts * 0.42

        print(f"{monthlyCarbonSaved} Carbon Saved this Month")
        print(f"{yearlyCarbonSaved} Carbon Saved This Year")




        
        dweepy.dweet_for('shyam__6', {'Last Good Update': str(timeformat)})
        time.sleep(5)
        dweepy.dweet_for('shyam__5', {'currentDailyWatts': currentDailyWatts})
        time.sleep(5)

        dweepy.dweet_for('shyam__5', {'currentDailyCarbonSaved': currentDailyCarbonSaved})
        time.sleep(5)

        dweepy.dweet_for('shyam__5', {'monthlyWatts': monthlyWatts})
        time.sleep(5)

        dweepy.dweet_for('shyam__5', {'yearlyCarbonSaved': yearlyCarbonSaved})
        time.sleep(5)

        dweepy.dweet_for('shyam__5', {'monthlyCarbonSaved': monthlyCarbonSaved})

        

        

        """collection = (dweepy.get_dweets_for('shyam__5'))
        print(collection[1]['content']['yearlyCarbonSaved'])
        print(('yearly carbon').title())
        print(collection[2]['content']['monthlyWatts'])
        print(('monthly watts').title())
        print(collection[3]['content']['currentDailyCarbonSaved'])
        print(('daily carbon saved').title())
        print(collection[4]['content']['currentDailyWatts'])
        print(('daily watts').title())
        print(collection[0]['content']['monthlyCarbonSaved'])"""
        
        print(('month carbon saved').title())
        print(today1)
        print('sleeping')
        print(datetime.datetime.now().time())
        print('done sleeping')
        timeformat = (datetime.datetime.now(pytz.timezone('Asia/Singapore')))
        time.sleep(300)

 


        




        dweepy.dweet_for('shyam__6', {'Last Good Update': str(timeformat)})
    except ValueError:
        print("Value Error")
        print(datetime.datetime.now().time())
        timeformat = (datetime.datetime.now(pytz.timezone('Asia/Singapore')))
        dweepy.dweet_for('shyam__5', {'currentDailyWatts': '0'})
        time.sleep(5)
        dweepy.dweet_for('shyam__5', {'currentDailyCarbonSaved': '0'})
        time.sleep(5)
    




    except dweepy.api.DweepyError:
        print("dweep error")
        timeformat = (datetime.datetime.now(pytz.timezone('Asia/Singapore')))

