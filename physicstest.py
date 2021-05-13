import requests
from bs4 import BeautifulSoup
import datetime
import math
import dweepy
import pytz
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

import time
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("topic2").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records

coord = 0
guessed = sheet.acell('A2').value
print(guessed)

print(guessed)
while coord != 300:
    time.sleep(0.1)
    coord += 1
    guessed = sheet.acell(f'A{coord}').value
    time.sleep(0.1)
    actual = sheet.acell(f'B{coord}').value
    if guessed == actual:
        sheet.update_cell(coord, 3, "Y")
    else:
        sheet.update_cell(coord, 3, "N  ")