from html5print import HTMLBeautifier
import requests
import dweepy
import json
import pprint
from datetime import date
import math
from reset_all import reset_all_readings
from dashboard_scraper import get_current_pv_value
import HourSourceCodeRecieve
import dashboard_scraper
import time
count = 0


while count != 1:
    dashboard_scraper.pv_resetter_0()
    HourSourceCodeRecieve.recieveSourceFunction()
    HourSourceCodeRecieve.rip_lines_and_dweet()
    #dashboard_scraper.get_current_pv_value()
    dashboard_scraper.get_current_pv_value_and_dweet()
    time.sleep(300)