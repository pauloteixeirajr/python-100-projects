# Application Programming Interfaces (APIs)
import requests
from datetime import datetime


iss_endpoint = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=iss_endpoint)
response.raise_for_status()

data = response.json()
lng = data["iss_position"]["longitude"]
lat = data["iss_position"]["latitude"]

print(lat, lng)

# Understand API Parameters
params = {
    "lat": lat,
    "lng": lng,
    "formatted": 0
}

sunset_endpoint = "https://api.sunrise-sunset.org/json"
response = requests.get(sunset_endpoint, params=params)
response.raise_for_status()
results = response.json()["results"]
sunrise = results["sunrise"]
sunset = results["sunset"]

sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]

time_now = datetime.now()

print(sunrise_hour, sunset_hour)
print(time_now.hour)
