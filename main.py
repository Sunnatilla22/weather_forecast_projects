import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "256c7063e6703a4299c4367e5158832c"
account_sid = "AC7ddef24707a35727d7389817937043ab"
auth_token = "98d666d683edef3466870092f8831c2c"

weather_params = {
    "lat": 51.5072,
    "lon": -0.1276,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data["list"][0]["weather"][0]["id"])

#get hold of the first eleven items in the list
weather_slice = weather_data["list"][:12]

print(weather_slice)

will_rain = False

#angela's way
for data in weather_slice:
    condition_code = data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Reme,ber to bring an umbrella"
        from_="+14302491121",
        to="+998935668904"
    )
    print(message.sid)
    # print("Bring an Umbrella")
#my way
# for data in range(len(weather_slice)):
#      if weather_slice[data]["weather"][0]["id"] < 700:
#          print(f"{data}. Bring an Umbrella")

