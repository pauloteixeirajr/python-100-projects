import requests

api_key = "API_KEY"
endpoint = "https://api.openweathermap.org/data/2.5/onecall"

params = {
    "lat": 53.34807,
    "lon": -6.24827,
    "appid": api_key,
    "units": "metric",
}

response = requests.get(endpoint, params=params)
response.raise_for_status()

print(response.status_code)
print(response.json())
