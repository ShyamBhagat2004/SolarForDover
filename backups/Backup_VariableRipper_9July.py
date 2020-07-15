from html5print import HTMLBeautifier
from selenium import webdriver
import requests
import dweepy
import json
import pprint
 
from HourSourceCodeRecieve import recieveSourceFunction, filename
import HourSourceCodeRecieve


#running the source code ripper

HourSourceCodeRecieve.recieveSourceFunction()
#opening txt file, setting up variable lines, when printing (lines[548]) we get line 549 output
sourceCodeVariableRip = open(filename, 'r+')
lines = sourceCodeVariableRip.readlines()

currentDailyWatts = lines[548].strip().rstrip()
print(currentDailyWatts)
currentDailyCarbonSaved = lines[3420].strip().rstrip()
print(currentDailyCarbonSaved)
monthlyWatts = lines[558].strip().rstrip()
print(monthlyWatts)
yearlyWatts = lines[568].strip().rstrip()
print(yearlyWatts)

intmonwatts = int(float(monthlyWatts))
monthlyCarbonSaved = intmonwatts * 0.42 + 0.001 - 0.0009999999999

print(monthlyCarbonSaved)

dweepy.dweet_for('shyam__5', {'currentDailyWatts': currentDailyWatts})
dweepy.dweet_for('shyam__5', {'currentDailyCarbonSaved': currentDailyCarbonSaved})
dweepy.dweet_for('shyam__5', {'monthlyWatts': monthlyWatts})
dweepy.dweet_for('shyam__5', {'yearlyWatts': yearlyWatts})
dweepy.dweet_for('shyam__5', {'monthlyCarbonSaved': monthlyCarbonSaved})

collection = (dweepy.get_dweets_for('shyam__5'))

print(collection[1]['content']['yearlyWatts'])
print(('yearly watts').title())
print(collection[2]['content']['monthlyWatts'])
print(('monthly watts').title())
print(collection[3]['content']['currentDailyCarbonSaved'])
print(('daily carbon saved').title())
print(collection[4]['content']['currentDailyWatts'])
print(('daily watts').title())
print(collection[0]['content']['monthlyCarbonSaved'])
print(('month carbon saved').title())

