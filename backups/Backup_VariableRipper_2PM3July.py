from html5print import HTMLBeautifier
from selenium import webdriver
import requests
 
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


dweepy.dweet_for('shyam__5', {'currentDailyWatts': currentDailyWatts})
dweepy.dweet_for('shyam__5', {'currentDailyCarbonSaved:': currentDailyCarbonSaved})
dweepy.dweet_for('shyam__5', {'monthlyWatts': monthlyWatts})
dweepy.dweet_for('shyam__5', {'yearlyWatts': yearlyWatts})
dweepy.dweet_for('shyam__5', {'test': 'test'})