from html5print import HTMLBeautifier
from selenium import webdriver
import dweepy
import datetime
import pytz
import time

filename = 'currentHourFileAlpha.txt'
def recieveSourceFunction():
    count = 0

    import requests

    res = requests.get('https://www.sunnyportal.com/Templates/PublicPage.aspx?page=fa4629bd-711e-4baf-b6cb-bfb39a09a0ce')
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
        try:
            timeformat = (datetime.datetime.now(pytz.timezone('Asia/Singapore')))
            sourceCodeVariableRip = open(filename, 'r+')
            lines = sourceCodeVariableRip.readlines()

            currentDailyWatts = (lines[274].strip().rstrip())
            print(f"{currentDailyWatts} The Watts Gotten Today ie Daily")
            currentDailyCarbonSaved = lines[1710].strip().rstrip()
            print(f"{currentDailyCarbonSaved} The Carbon Saved Today ie Daily")
            monthlyWatts = lines[279].strip().rstrip()
            print(f"{monthlyWatts} The Watts Gotten this Month ie Monthly")
            yearlyWatts = lines[284].strip().rstrip()
            print(f"{yearlyWatts} The Watts gotten this Year ie Yearly")

            intmonwatts = int(float(monthlyWatts))
            monthlyCarbonSaved = intmonwatts * 0.42 + 0.001 

            intyrwatts = int(float(yearlyWatts))
            yearlyCarbonSaved = intyrwatts * 0.42

            print(f"{monthlyCarbonSaved} Carbon Saved this Month")
            print(f"{yearlyCarbonSaved} Carbon Saved This Year")
            dweepy.dweet_for('shyam__6', {'Last Good Update': str(timeformat)})
            time.sleep(5)
            dweepy.dweet_for('shyam__5', {'currentDailyWatts': currentDailyWatts})
            time.sleep(5)
            dweepy.dweet_for('shyam__5', {'currentDailyCarbonSaved': currentDailyCarbonSaved})
            time.sleep(5)

            dweepy.dweet_for('shyam__5', {'monthlyWatts': monthlyWatts})
            time.sleep(5)

            dweepy.dweet_for('shyam__5', {'yearlyCarbonSaved': yearlyCarbonSaved})
            time.sleep(5)

            dweepy.dweet_for('shyam__5', {'monthlyCarbonSaved': monthlyCarbonSaved})

            

            

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
            dweepy.dweet_for('shyam__5', {'currentDailyWatts': '0'})
            time.sleep(5)
            dweepy.dweet_for('shyam__5', {'currentDailyCarbonSaved': '0'})
            time.sleep(5)
        except dweepy.api.DweepyError:
            print("dweep error")
            timeformat = (datetime.datetime.now(pytz.timezone('Asia/Singapore')))




  