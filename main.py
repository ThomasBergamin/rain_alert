import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "YOUR_KEY"
PHONE_NUMBER = "PHONE_NUMBER_TWILIO"
account_sid = "xx"
auth_token = "xx"

weather_parameters = {
    "lat": "YOUR_LAT",
    "lon": "YOUR_LON",
    "appid": api_key,
    "exclude": "current,minutely,daily",
    "units": "metric"
}


response = requests.get(OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()


weather_prevision = [(weather_data["hourly"][hour]["weather"][0]["id"]) for hour in range(0, 13)]

will_rain = False

for id_weather in weather_prevision:
    if id_weather < 700:
        will_rain = True
    else:
        pass

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today. Don't forget your umbrella!",
                     from_= PHONE_NUMBER,
                     to='YOUR_PHONE_NUMBER',
                 )

    print(message.status)


