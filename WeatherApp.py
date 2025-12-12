# Project/Day 35 - Weather App
# This is my first time using SMS Texting!

import requests
import os
from twilio.rest import Client

OWMEndpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ['APP_API_KEY']

weather_params ={
    "lat": os.environ["lat"],
    'lon': os.environ["long"],
    "appid": api_key,
    "cnt": 4
}

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

from_phone_num = os.environ["from"]
to_phone_num = os.environ["to"]

client = Client(account_sid, auth_token)



response = requests.get(OWMEndpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

isRaining = False

for hour_data in weather_data["list"]:
    condition_code = hour_data['weather'][0]["id"]
    if int(condition_code) < 700:
        isRaining = True
if isRaining:
    message = client.messages.create(
        body="It is going to rain within the next 12 hours, bringing an umbrella might be a good decision.",
        from_=from_phone_num,
        to=to_phone_num,
    )
else:
    message = client.messages.create(
        body="It's not going to rain, feel free to leave your umbrella at home!",
        from_=from_phone_num,
        to=to_phone_num,
    )
