import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

DIR = os.path.dirname(__file__)
load_dotenv(os.path.join(DIR, "auth.pwd"))

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH")
PHONE_NO = os.environ.get("PHONE_NO")

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"
OWM_API_KEY = os.environ.get("OWM_KEY")
owm_params = {
    "lat": 52.2,
    "lon": 13.7,
    "exclude": "minutely,daily,alerts",
    "appid": OWM_API_KEY,
    "lang": "pl",
    "units": "metric",
}

resp = requests.get(url=OWM_ENDPOINT, params=owm_params)
resp.raise_for_status()
data = resp.json().get("hourly")

data_12h = data[:12]
data_12h_weather = [hour.get('weather')[0]['main'] for hour in data_12h]

rain_pattern_12h = [weather in ("Rain", "Drizzle", "Thunderstorm") \
    for weather in data_12h_weather]

if True in rain_pattern_12h:
    print("It will rain in 12 hours - an SMS will be sent.")
    sms_client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    sms_message = sms_client.messages.create(
        body="It will rain today. Take an umbrella.☂️",
        from_="+14344362030",
        to=PHONE_NO
    )
    
else:
    print("There will be no rain in 12 hours")
    