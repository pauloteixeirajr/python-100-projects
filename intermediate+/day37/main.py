import os
import requests
from datetime import datetime
# Http Post Requests

USERNAME = "paulo"
TOKEN = os.environ.get("PIXELA_TOKEN")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# Create the user account
# response = requests.post(PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

new_graph_config = {
    "id": "graph1",
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create a graph
# response = requests.post(
#     GRAPH_ENDPOINT,
#     json=new_graph_config,
#     headers=headers)

# print(response.text)

# Add a pixel to the tracker

PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/graph1"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5"
}

# response = requests.post(PIXEL_ENDPOINT, json=pixel_data, headers=headers)
# print(response.text)

# Update Pixel
# response = requests.put(
#     url=f"{PIXEL_ENDPOINT}/{today.strftime('%Y%m%d')}",
#     json={"quantity": "15"},
#     headers=headers
# )
# print(response.text)

# Delete Pixel
response = requests.delete(
    url=f"{PIXEL_ENDPOINT}/{today.strftime('%Y%m%d')}",
    headers=headers
)
print(response.text)
