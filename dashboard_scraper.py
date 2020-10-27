import requests
from bs4 import BeautifulSoup
import datetime
import math

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
    
    

get_current_pv_value()
