import requests

params = {
    "amount": 10,
    "type": "boolean"
}
open_trivia_endpoint = "https://opentdb.com/api.php"

response = requests.get(url=open_trivia_endpoint, params=params)
response.raise_for_status()

question_data = response.json()["results"]
