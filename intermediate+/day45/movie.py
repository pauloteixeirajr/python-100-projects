
import requests
from bs4 import BeautifulSoup

BEST_MOVIES_URL = "https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(BEST_MOVIES_URL)
markup = response.text

soup = BeautifulSoup(markup, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [f"{movie.getText()}\n" for movie in all_movies][::-1]

with open("movies.txt", mode="w") as file:
    file.writelines(movie_titles)
