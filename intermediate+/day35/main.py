import requests
from twilio.rest import Client

api_key = "API_KEY"
endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "ACCOUNT_SID"
auth_token = "AUTH_TOKEN"

params = {
    "lat": 54.787715,
    "lon": -6.492315,
    "appid": api_key,
    "units": "metric",
    "exclude": "current,minutely,daily"
}

response = requests.get(endpoint, params=params)
response.raise_for_status()

data = response.json()
next_12_hours = data["hourly"][:12]

will_rain = False

for hour in next_12_hours:
    for weather in hour["weather"]:
        if weather["id"] < 700:
            will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an 🌂",
            from_="FROM_NUMBER",
            to="TO_NUMBER"
        )
    print(message.status)
