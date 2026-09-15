"""
Uvod v API
API: https://open-meteo.com/

Za poljubno vpisano mesto:
Izpiši trenutno temperaturo.
Izpiši temperature za naslednjih 7 dni.
Ugotovi, kateri dan bo najtoplejši oz. najhladnejši, in izpiši datum ter temperaturo.
Ugotovi, kateri dan ima največjo razliko med dnevno in nočno temperaturo.
Med 10 največjimi slovenskimi mesti poišči tisto;
ki bo danes najtoplejše oz. najhladnejše,
ki bo imelo najmanj oz. največ dežja,
ki bo imelo najmanj oz. največ vetra.
"""

import requests

base_url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude":  46.35,
    "longitude":  14.2833,
    "daily":  "temperature_2m_max,temperature_2m_min,temperature_2m_mean&current=temperature_2m",
    "current": "temperature_2m",
    "timezone": "Europe/Berlin"
}

call = requests.get(base_url, params=params)
print(call.url)
toJson = call.json()

print(toJson["current"]["temperature_2m"])
#https://api.open-meteo.com/v1/forecast?latitude=46.35&longitude=14.2833&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean&current=temperature_2m&timezone=Europe%2FBerlin