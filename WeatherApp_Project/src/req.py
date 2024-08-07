import requests


# get api from api.open-meteo.com
URL = 'https://api.open-meteo.com/v1/forecast?latitude=35.8327&longitude=50.9915&hourly=temperature_2m&forecast_days=1'
location = 'delhi technologicaluniversity'
PARAM = {'address':location}
info = requests.get(url=URL, params=PARAM)
data = info.json()
# print(data)
temps = data["hourly"]["temperature_2m"]
print(temps)