#!/usr/bin/python

'''
Dependencies
espeak
'''

import time
import datetime
import os
import greeting

debugging = True

currentTime = datetime.datetime.now()

strStartUpMessage = "Hello, Matthew"
print(strStartUpMessage)
os.system("espeak '" + strStartUpMessage + "'")

alarmHour = input("Enter the hour you want to wake up at: ")
alarmMinute = input("Enter the minute you want to wake up at: ")

print("You want to wake up at " + str(alarmHour).zfill(2) + ":" + str(alarmMinute).zfill(2))

if not debugging:
    while not(currentTime.hour == alarmHour and currentTime.minute == alarmMinute):
        currentTime = datetime.datetime.now()
        clock = str(currentTime.hour).zfill(2) + ":" + str(currentTime.minute).zfill(2) + ":" + str(currentTime.second).zfill(2)
        print(clock)
        time.sleep(1)

greeting.goodMorning()