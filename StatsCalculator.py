from html5print import HTMLBeautifier
from selenium import webdriver
import requests
import dweepy
import json
import pprint
 
from HourSourceCodeRecieve import recieveSourceFunction, filename
import HourSourceCodeRecieve


collection = (dweepy.get_dweets_for('shyam__5'))


"""print(collection[1]['content']['yearlyCarbonSaved'])
print(('yearly carbon').title())
print(collection[2]['content']['monthlyWatts'])
print(('monthly watts').title())
print(collection[3]['content']['currentDailyCarbonSaved'])
print(('daily carbon saved').title())
print(collection[4]['content']['currentDailyWatts'])
print(('daily watts').title())
print(collection[0]['content']['monthlyCarbonSaved'])
print(('month carbon saved').title())"""

day_classroom = float((collection[4]['content']['currentDailyWatts']) / 4 / 8)
day_ac = float((collection[4]['content']['currentDailyWatts']) / 3 / 8)
day_laptopCharging = float((collection[4]['content']['currentDailyWatts']) / 0.085 / 8)
day_carHours = float(((collection[4]['content']['currentDailyWatts']) / 0.15))

"""
print(day_ac)
print(day_classroom)
print(day_laptopCharging)"""


print(day_carHours)