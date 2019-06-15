import time
import datetime
import os
import pygame
pygame.init()

def goodMorning():
    my_sound = pygame.mixer.Sound('gong.wav')
    my_sound.play()
    os.system("espeak '" + speakHello() + "'")
    os.system("espeak '" + speakCurrentTime() + "'")

def speakHello():
    strGreeting = "Good morning, Matthew."
    return strGreeting

def speakCurrentTime():
    currentTime = datetime.datetime.now()
    currentHour = currentTime.hour
    currentMinute = currentTime.minute

    if currentMinute == 0:
        strCurrentTime = "The current time is " + str(currentHour) + " o clock"
    elif currentMinute < 10:
        strCurrentTime = "The current time is " + str(currentHour) + " o " + str(currentMinute)
    else:
        strCurrentTime = "The current time is " + str(currentHour) + " " + str(currentMinute)

    return strCurrentTime