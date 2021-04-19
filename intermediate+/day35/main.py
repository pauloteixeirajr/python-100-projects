import requests

api_key = "API_KEY"
endpoint = "https://api.openweathermap.org/data/2.5/onecall"

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

for hour in next_12_hours:
    for weather in hour["weather"]:
        print(weather["main"])
        if weather["id"] < 700:
            print("Bring an umbrella")
