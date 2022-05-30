import requests
import os
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
TWILIO_ACCT_SID = "twilio acct sid"
TWILIO_AUTH_TOKEN = "twilio auth token"


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
        will_rain = True

account_sid = TWILIO_ACCT_SID
auth_token = TWILIO_AUTH_TOKEN


client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body="It will rain today.", 
        from_="twilio number", 
        to="my number"
    )

print(message.status)