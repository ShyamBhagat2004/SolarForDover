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
"""
docker guide = https://docs.google.com/document/d/1R9swZekHIR2PnytGjqD7clZdm3pO2CtC3lxJzSTKnCQ/edit
"""
try:

    while count != 1:
        HourSourceCodeRecieve.recieveSourceFunction()
        HourSourceCodeRecieve.rip_lines_and_dweet()
        #dashboard_scraper.get_current_pv_value()
        dashboard_scraper.get_current_pv_value_and_dweet()
        dashboard_scraper.pv_resetter_0()

        time.sleep(300)
except:
    pass
        
