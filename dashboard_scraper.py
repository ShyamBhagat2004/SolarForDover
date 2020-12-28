import requests
from bs4 import BeautifulSoup
import datetime
import math
import dweepy
import pytz

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
    import dweepy
    import time
    page = requests.get("https://bit.ly/37Gvm9v")
    soup = BeautifulSoup(page.content, 'html.parser')
    pagePoolPanels = requests.get("https://www.sunnyportal.com/Templates/PublicPage.aspx?page=e30bffa6-04b5-45e7-b9d5-bdd17fc918cd")
    soupPool = BeautifulSoup(pagePoolPanels.content, 'html.parser')
    
    pv_current_junior = soup.find("span", attrs = {"class" : "mainValueAmount"})
    pv_current_pool = soupPool.find("span", attrs = {"class" : "mainValueAmount"})
    value_junior_current_int = int(pv_current_junior['data-value'])
    value_pool_current_int = int(pv_current_pool['data-value']) / 1000
    value_total_current_int = value_junior_current_int + value_pool_current_int
    print(f"The current power in watts not kilowatts is {value_total_current_int }") 
    value_total_current_int = value_total_current_int / 1000
    finalCurrentPower = math.trunc(value_total_current_int)
    get_current_pv_value.final = finalCurrentPower
    print(f"The current power combined is {finalCurrentPower}")
    if value_total_current_int * 1000 < 2000:
        dweepy.dweet_for('shyam__7', {'finalcurrentpower' : finalCurrentPower*1000})
    else:
        dweepy.dweet_for('shyam__7', {'finalCurrentPower' : finalCurrentPower})
    if finalCurrentPower < 15:
        time.sleep(5)
        dweepy.dweet_for('shyam__7', {'finalCurrentPower' : 15})

def pv_resetter_0():
    import dweepy
    import pytz
    import datetime
    now = datetime.datetime.now(pytz.timezone('Asia/Singapore'))
    if now.hour == 23:
        dweepy.dweet_for('shyam__7', {'finalCurrentPower' : 0})

