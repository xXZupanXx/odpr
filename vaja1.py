"""
import requests
base_url = ""
call = requests.get(base_url).json()
print(call["daily"]["rain_sum"][0])

#dostop do napačnih ključev
print(raznoliki["krenki"])

prazen = {}
print(type)
"""



import requests

base_url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 46.3167,
    "longitude": 14.2,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m",
    "timezone": "Europe/Berlin",
    "forecast_days": 1
}

#https://api.open-meteo.com/v1/forecast?latitude=46.3167&longitude=14.2&current=temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m&timezone=Europe%2FBerlin&forecast_days=1

call = requests.get(base_url, params=params)
print(call.url)
toJson = call.json()
print(toJson["current"]["temperature_2m"])
print(toJson["current"]["relative_humidity_2m"])
print(toJson["current"]["wind_speed_10m"])
print(toJson["current"]["wind_direction_10m"])