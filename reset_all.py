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
count = 0




def reset_all_readings():
    zero = 0
    timeformat = (datetime.datetime.now(pytz.timezone('Asia/Singapore')))
    timeformatformat = str(timeformat.strftime("%H"))
    if timeformatformat == "23":
            time.sleep(90)
            dweepy.dweet_for('shyam__5', {'currentDailyWatts': zero})
            time.sleep(90)
            dweepy.dweet_for('shyam__5', {'currentDailyCarbonSaved': zero})
            time.sleep(90)
            dweepy.dweet_for('shyam__5', {'monthlyWatts': zero})
            time.sleep(90)
            dweepy.dweet_for('shyam__5', {'yearlyCarbonSaved': zero})
            time.sleep(90)
            dweepy.dweet_for('shyam__5', {'monthlyCarbonSaved': zero})
            time.sleep(90)
            resettoday = 1


