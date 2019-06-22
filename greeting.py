import time
from datetime import datetime
import os
import pygame
from speak import espeak
from weather import Weather
from config import Config

config = Config()

def goodMorning():
    os.system("clear")
    speakHello()
    speakCurrentTime()
    speakWeather()
    turnOff()

def speakHello():
    pygame.init()
    gong = pygame.mixer.Sound('sounds/gong.wav')

    gong.play()

    strGreeting = "Good morning, " + config.getName()
    espeak(strGreeting)

    morningMix()

# selects background music that is played
def morningMix():
    morningMood = pygame.mixer.Sound('sounds/morningMood.wav')
    morningMood.play()

def speakCurrentTime():
    currentHour = datetime.now().hour
    currentMinute = datetime.now().minute

    if currentMinute == 0:
        strCurrentTime = "The current time is " + str(currentHour) + " o clock"
    elif currentMinute < 10:
        strCurrentTime = "The current time is " + str(currentHour) + " o " + str(currentMinute)
    else:
        strCurrentTime = "The current time is " + str(currentHour) + " " + str(currentMinute)

    espeak(strCurrentTime)

def speakWeather():
    weather = Weather(27519)
    strTemperature = "The current temperature is " + weather.getTemperature()
    strWeatherDescription = "The weather is currently " + weather.getWeatherDescription()

    espeak(strTemperature)
    espeak(strWeatherDescription)

def turnOff():
    input("Press 'Enter' to turn off alarm")