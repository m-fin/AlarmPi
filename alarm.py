'''
Dependencies
espeak
'''

import time
from datetime import datetime
import os
from greeting import goodMorning
from speak import espeak

name = "Matthew"

def main():
    startup()
    alarmClock()
    goodMorning()

def startup():
    os.system("clear")

    strStartUpMessage = "Hello, " + name

    print(strStartUpMessage)
    espeak(strStartUpMessage)
    
def alarmClock():
    alarmHour = int(input("Enter the hour you want to wake up at: "))
    alarmMinute = int(input("Enter the minute you want to wake up at: "))

    os.system("clear")
    strAlarmSetMessage = "Alarm set for " + str(alarmHour).zfill(2) + ":" + str(alarmMinute).zfill(2) + " in " + alarmDifference(alarmHour, alarmMinute)
    print(strAlarmSetMessage)
    espeak(strAlarmSetMessage)

    while not(datetime.now().hour == alarmHour and datetime.now().minute == alarmMinute):
        clock = str(datetime.now().hour).zfill(2) + ":" + str(datetime.now().minute).zfill(2) + ":" + str(datetime.now().second).zfill(2)
        print(clock, end="\r")
        time.sleep(1)

    print("DONE")

def alarmDifference(alarmHour, alarmMinute):
    alarmHourDelta = int(alarmHour) - datetime.now().hour
    alarmMinuteDelta = int(alarmMinute) - datetime.now().minute

    while not (0 <= alarmHourDelta <= 23):
        if (alarmHourDelta > 23):
            alarmHourDelta -= 24
        elif (alarmHourDelta < 0):
            alarmHourDelta += 24

    while not (0 <= alarmMinuteDelta <= 59):
        if (alarmMinuteDelta > 59):
            alarmMinuteDelta -= 60
            alarmHourDelta += 1
        elif (alarmMinuteDelta < 0):
            alarmMinuteDelta += 60
            alarmHourDelta -= 1

    return str(alarmHourDelta) + " hours and " + str(alarmMinuteDelta) + " minutes."

if __name__ == "__main__":
    main()