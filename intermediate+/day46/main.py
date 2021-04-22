import requests
from bs4 import BeautifulSoup

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100"

date = input("Which year do you wnat to travel to? (YYYY-MM-DD): ")
response = requests.get(f"{BILLBOARD_URL}/{date.strip()}")
markup = response.text

soup = BeautifulSoup(markup, "html.parser")
song_spans = soup.find_all(
    name="span",
    class_="chart-element__information__song"
)
song_titles = [song.getText() for song in song_spans]
print(song_titles)
