
import requests
import json


def weather():

    api_key = "ed200ef2b107c54163c9012a6112c262"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = 'hyderabad'
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]

    return int(current_temperature-273)


print(f'temperature is {weather()} degrees')
