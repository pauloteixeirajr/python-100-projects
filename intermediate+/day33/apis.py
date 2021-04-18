# Application Programming Interfaces (APIs)
import requests


endpoint = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=endpoint)
response.raise_for_status()

data = response.json()
lon = data["iss_position"]["longitude"]
lat = data["iss_position"]["latitude"]

print(lat, lon)
