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
    
    
