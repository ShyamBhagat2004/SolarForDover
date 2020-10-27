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

HourSourceCodeRecieve.recieveSourceFunction()
HourSourceCodeRecieve.rip_lines()
dashboard_scraper.get_current_pv_value()
print(get_current_pv_value.final)
