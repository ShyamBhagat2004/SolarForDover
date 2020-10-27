from html5print import HTMLBeautifier
from selenium import webdriver
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
def rip_lines():
        sourceCodeVariableRip = open(filename, 'r+')
        lines = sourceCodeVariableRip.readlines()

        currentDailyWatts = (lines[548].strip().rstrip())
        print(f"{currentDailyWatts} The Watts Gotten Today ie Daily")
        currentDailyCarbonSaved = lines[3420].strip().rstrip()
        print(f"{currentDailyCarbonSaved} The Carbon Saved Today ie Daily")
        monthlyWatts = lines[558].strip().rstrip()
        print(f"{monthlyWatts} The Watts Gotten this Month ie Monthly")
        yearlyWatts = lines[568].strip().rstrip()
        print(f"{yearlyWatts} The Watts gotten this Year ie Yearly")

        intmonwatts = int(float(monthlyWatts))
        monthlyCarbonSaved = intmonwatts * 0.42 + 0.001 

        intyrwatts = int(float(yearlyWatts))
        yearlyCarbonSaved = intyrwatts * 0.42

        print(f"{monthlyCarbonSaved} Carbon Saved this Month")
        print(f"{yearlyCarbonSaved} Carbon Saved This Year")
    


