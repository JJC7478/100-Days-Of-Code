import requests


OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "this is an api key"
exclude = "current,minutely,daily"

params = {
    "lat": 40.760780,
    "lon": -111.891045,
    "appid": api_key,
    "exclude": exclude
}

response = requests.get(url=OWM_ENDPOINT, params=params)
response.raise_for_status()

weather_data = response.json()
hourly = weather_data["hourly"]

twelve_hours = [hourly[n] for n in range(12)]
for hour in twelve_hours:
    hour_weather = hour["weather"][0]["id"]
    if hour_weather < 700:
        print("Bring an umbrella")