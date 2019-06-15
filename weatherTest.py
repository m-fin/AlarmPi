#!/usr/bin/python

import requests

url = 'https://samples.openweathermap.org/data/2.5/weather?zip=27519,us&appid=4748ef4b87cf70fd7cc2bf0ea5e0b43c'

res = requests.get(url)

data = res.json()

print(res)

print(data)