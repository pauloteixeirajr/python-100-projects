import os
import requests
from datetime import datetime

APPLICATION_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

exercises = input("Tell me which exercises you did: ")

n_headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

n_request_body = {
    "query": exercises,
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 169,
    "age": 32
}

n_response = requests.post(
    url=NUTRITIONIX_ENDPOINT,
    json=n_request_body,
    headers=n_headers,
)

exercises = n_response.json()["exercises"]

today = datetime.now()
date_fmted = today.strftime("%d/%m/%Y")
time_fmted = today.strftime("%H:%M:%S")

for exercise in exercises:
    sheety_data = {
        "workout": {
            "date": date_fmted,
            "time": time_fmted,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    s_response = requests.post(
        url=SHEETY_ENDPOINT,
        json=sheety_data,
        headers={
            "Authorization": os.environ.get("TOKEN")
        })
    print(s_response.text)
