import requests
from bs4 import BeautifulSoup
import datetime
import math
import dweepy
import pytz
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

Tutorial = "https://www.dataquest.io/blog/web-scraping-tutorial-python/"
VirtualEnvironment = "https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/"

page = requests.get("https://bit.ly/37Gvm9v")
soup = BeautifulSoup(page.content, 'html.parser')
nig = (soup.find(id="ctl00_ContentPlaceHolder1_PublicPagePlaceholder1_PageUserControl_ctl00_PublicPageLoadFixPage_energyYieldWidget_energyYieldValue"))

pagePoolPanels = requests.get("https://www.sunnyportal.com/Templates/PublicPage.aspx?page=e30bffa6-04b5-45e7-b9d5-bdd17fc918cd")
soupPool = BeautifulSoup(pagePoolPanels.content, 'html.parser')
#print(nig.get_text())

def get_current_pv_value():
    pv_current_junior = soup.find("span", attrs = {"class" : "mainValueAmount"})
    pv_current_pool = soupPool.find("span", attrs = {"class" : "mainValueAmount"})
    value_junior_current_int = int(pv_current_junior['data-value'])
    value_pool_current_int = int(pv_current_pool['data-value'])
    value_total_current_int = value_junior_current_int + value_pool_current_int
    value_total_current_int = value_total_current_int / 1000
    finalCurrentPower = math.trunc(value_total_current_int)
    get_current_pv_value.final = finalCurrentPower
def get_current_pv_value_and_dweet():
    import random
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    from pprint import pprint
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("SOLAR JSON SCRIPT").sheet1  # Open the spreadhseet

    data = sheet.get_all_records()  # Get a list of all records

    import dweepy
    import time
    page = requests.get("https://bit.ly/37Gvm9v")
    soup = BeautifulSoup(page.content, 'html.parser')
    pagePoolPanels = requests.get("https://bit.ly/highSchoolDoverSunny")
    soupPool = BeautifulSoup(pagePoolPanels.content, 'html.parser')
    
    pv_current_junior = soup.find("span", attrs = {"class" : "mainValueAmount"})
    pv_current_pool = soupPool.find("span", attrs = {"class" : "mainValueAmount"})
    value_junior_current_int = int(pv_current_junior['data-value'])
    value_pool_current_int = int(pv_current_pool['data-value'])
    value_total_current_int = value_junior_current_int + value_pool_current_int
    print(f"The current power in watts not kilowatts is {value_total_current_int }") 
    value_total_current_int = value_total_current_int / 1000
    finalCurrentPower = math.trunc(value_total_current_int)
    get_current_pv_value.final = finalCurrentPower
    print(f"The current power combined is {finalCurrentPower}")
    
    """
    if value_total_current_int * 1000 < 2000:
        dweepy.dweet_for('shyam__7', {'finalcurrentpower' : finalCurrentPower*1000})
    else:
        dweepy.dweet_for('shyam__7', {'finalCurrentPower' : finalCurrentPower})"""
    if finalCurrentPower < 50:
        time.sleep(5)
        """
        dweepy.dweet_for('shyam__7', {'finalCurrentPower' : 15})
        """
        sheet.update_cell(23,2, 50)
    else:
        time.sleep(5)
        """
        dweepy.dweet_for('shyam__7', {'finalCurrentPower' : finalCurrentPower})
        """
        sheet.update_cell(23,2, finalCurrentPower)

def pv_resetter_0():
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    from pprint import pprint
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("SOLAR JSON SCRIPT").sheet1  # Open the spreadhseet

    data = sheet.get_all_records()  # Get a list of all records
    import dweepy
    import pytz
    import datetime
    from datetime import time
    now = datetime.datetime.now(pytz.timezone('Asia/Singapore'))
    if now.hour == 23:
        """dweepy.dweet_for('shyam__7', {'finalCurrentPower' : 0})"""
        sheet.update_cell(23,2  , 0)
        sheet.update_cell(24,2,0)


def co2_highschool():
    import requests
    import bs4
    import pprint
    highschool_co2_url = requests.get("https://bit.ly/highSchoolDoverSunny")
    highschool_co2_parser = BeautifulSoup(highschool_co2_url.content, 'html.parser')
    co2_value = highschool_co2_parser.find("span", attrs = {"id" : "ctl00_ContentPlaceHolder1_PublicPagePlaceholder1_PageUserControl_ctl00_PublicPageLoadFixPage_carbonWidget_carbonReductionValue"})
    final_co2_int = int(co2_value.text)
    print(final_co2_int)
import requests
import bs4
import pprint
highschool_co2_url = requests.get("https://bit.ly/highSchoolDoverSunny")
highschool_co2_parser = BeautifulSoup(highschool_co2_url.content, 'html.parser')
co2_value = highschool_co2_parser.find("span", attrs = {"id" : "ctl00_ContentPlaceHolder1_PublicPagePlaceholder1_PageUserControl_ctl00_PublicPageLoadFixPage_carbonWidget_carbonReductionValue"})
final_co2_int = int(co2_value.text)

