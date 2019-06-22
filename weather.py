import requests
import json
from config import Config

config = Config()

class Weather:
    def __init__(self, zip_code):
        self.zip_code = zip_code

        # http://api.openweathermap.org/data/2.5/weather?zip=27519,us&appid=4748ef4b87cf70fd7cc2bf0ea5e0b43c

        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        api_key = "4748ef4b87cf70fd7cc2bf0ea5e0b43c"  

        complete_url = base_url + "zip=" + str(self.zip_code) + ",us&appid=" + api_key

        response = requests.get(complete_url)  
        x = response.json()
        self.y = x["main"]
        self.z = x["weather"]

    def getTemperature(self):
        tempK = self.y["temp"]
        unitOfTemperature = config.getUnitOfTemperature()

        if (unitOfTemperature == "F"):
            strFinal = str(round((tempK - 273.15) * 9/5 + 32)) + " degrees Fahrenheit."
        elif (unitOfTemperature == "C"):
            strFinal = str(round(tempK - 273.15)) + " degrees Celsius."
        elif (unitOfTemperature == "K"):
            strFinal = str(round(tempK)) + " degrees Kelvin."
        else:
            strFinal = "Please enter a valid unit of temperature in weather.py"
        
        return strFinal
    
    def getWeatherDescription(self):
        weather_description = str(self.z[0]["description"])

        return weather_description


        '''
        current_pressure = str(y["pressure"])
        current_humidiy = str(y["humidity"])
        
        z = x["weather"] 
        weather_description = str(z[0]["description"])
        '''