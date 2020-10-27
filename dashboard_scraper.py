import requests
from bs4 import BeautifulSoup
import datetime
Tutorial = "https://www.dataquest.io/blog/web-scraping-tutorial-python/"
VirtualEnvironment = "https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/"

page = requests.get("https://www.sunnyportal.com/Templates/PublicPage.aspx?page=1169a2ff-8f51-4ea9-ba72-316009593c62")
soup = BeautifulSoup(page.content, 'html.parser')
nig = (soup.find(id="ctl00_ContentPlaceHolder1_PublicPagePlaceholder1_PageUserControl_ctl00_PublicPageLoadFixPage_energyYieldWidget_energyYieldValue"))
#print(nig.get_text())

def get_current_pv_value():
    pv_current = soup.find("span", attrs = {"class" : "mainValueAmount"})
    value = int(pv_current['data-value'])
    print(value)

    

get_current_pv_value()
