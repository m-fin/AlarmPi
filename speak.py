import os

def espeak(strSpeak):
    os.system("espeak '" + strSpeak + "'")