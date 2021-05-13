from html5print import HTMLBeautifier
from selenium import webdriver
import dweepy
import datetime
import pytz
import time
from dashboard_scraper import final_co2_int

filename = 'currentHourFileAlpha.txt'
def recieveSourceFunction():
    count = 0

    import requests

    res = requests.get('https://www.sunnyportal.com/Templates/PublicPage.aspx?page=c4532d4d-ea28-47c4-8ea5-7e4fd89e76d2')
    html_source = res.text
    # this line trows an exception if an error on the 
                            # connection to the page occurs. 

    wattValue1 = ""
    # making the messy code of page source unmessy
    beautifulSourceCode = (HTMLBeautifier.beautify(html_source, 4))

    #writing the pretty source code to a file           


    currentHourWrite = open(filename, 'w+')
    currentHourWrite.write(beautifulSourceCode)
def rip_lines_and_dweet():
        import time
        import bs4
        from bs4 import BeautifulSoup
        try:
            import gspread
            import bs4
            import requests
            from oauth2client.service_account import ServiceAccountCredentials
            from pprint import pprint
            scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

            creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

            client = gspread.authorize(creds)

            sheet = client.open("SOLAR JSON SCRIPT").sheet1  # Open the spreadhseet

            data = sheet.get_all_records()  # Get a list of all records
            timeformat = (datetime.datetime.now(pytz.timezone('Asia/Singapore')))
            sourceCodeVariableRip = open(filename, 'r+')
            lines = sourceCodeVariableRip.readlines()

            currentDailyWatts = (lines[1911].strip().rstrip())
            print(f"{currentDailyWatts} The Watts Gotten Today ie Daily")
            currentDailyCarbonSaved = lines[1729].strip().rstrip()
            floatCarbonDaily = (currentDailyCarbonSaved)
            #print(final_co2_int)
            #currentDailyCarbonSaved = (currentDailyCarbonSaved) + final_co2_int
            

            print(f"{currentDailyCarbonSaved} The Carbon Saved Today ie Daily")
            monthlyWatts = lines[1738].strip().rstrip()
            print(f"{monthlyWatts} The Watts Gotten this Month ie Monthly")
            yearlyWatts = lines[1921].strip().rstrip()
            print(f"{yearlyWatts} The Watts gotten this Year ie Yearly")

            intmonwatts = int(float(monthlyWatts))
            monthlyCarbonSaved = intmonwatts * 0.42 + 0.001 

            intyrwatts = int(float(yearlyWatts))
            yearlyCarbonSaved = intyrwatts * 0.42

            print(f"{monthlyCarbonSaved} Carbon Saved this Month")
            print(f"{yearlyCarbonSaved} Carbon Saved This Year")
            #dweepy.dweet_for('shyam__6', {'Last Good Update': str(timeformat)})
            

            time.sleep(5)
            #dweepy.dweet_for('shyam__5', {'currentDailyWatts': currentDailyWatts})
            sheet.update_cell(22, 2, currentDailyWatts)
            time.sleep(5)
            #dweepy.dweet_for('shyam__5', {'currentDailyCarbonSaved': currentDailyCarbonSaved})
            
            highschool_co2_url = requests.get("https://bit.ly/highSchoolDoverSunny")
            highschool_co2_parser = BeautifulSoup(highschool_co2_url.content, 'html.parser')
            co2_value = highschool_co2_parser.find("span", attrs = {"id" : "ctl00_ContentPlaceHolder1_PublicPagePlaceholder1_PageUserControl_ctl00_PublicPageLoadFixPage_carbonWidget_carbonReductionValue"})
            final_co2_int = int(co2_value.text)
            #currentDailyWithHighschool = int(currentDailyCarbonSaved) + int(final_co2_int)
            sheet.update_cell(24, 2, floatCarbonDaily)
            
            time.sleep(5)

            #dweepy.dweet_for('shyam__5', {'monthlyWatts': monthlyWatts})
            sheet.update_cell(25, 2, monthlyWatts)
            time.sleep(5)

            #dweepy.dweet_for('shyam__5', {'yearlyCarbonSaved': yearlyCarbonSaved})
            sheet.update_cell(26, 2, yearlyCarbonSaved)
            time.sleep(5)

            #dweepy.dweet_for('shyam__5', {'monthlyCarbonSaved': monthlyCarbonSaved})
            sheet.update_cell(27, 2, monthlyCarbonSaved)
            time.sleep(5)
            sheet.update_cell(28,2, yearlyCarbonSaved/42 * 100)

            

            

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
            print('sleeping')
            print(datetime.datetime.now().time())
            print('done sleeping')
            timeformat = (datetime.datetime.now(pytz.timezone('Asia/Singapore')))
        except ValueError:
            print("Value Error")
            print(datetime.datetime.now().time())
            timeformat = (datetime.datetime.now(pytz.timezone('Asia/Singapore')))
            #dweepy.dweet_for('shyam__5', {'currentDailyWatts': '0'})
            time.sleep(5)
            #dweepy.dweet_for('shyam__5', {'currentDailyCarbonSaved': '0'})
            time.sleep(5)
        except dweepy.api.DweepyError:
            print("dweep error")
            timeformat = (datetime.datetime.now(pytz.timezone('Asia/Singapore')))

