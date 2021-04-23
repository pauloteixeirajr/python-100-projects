import random
import requests
from datetime import datetime
from flask import Flask, render_template

agify_url = "https://api.agify.io"
genderize_url = "https://api.genderize.io"
blog_posts_url = "https://api.npoint.io/5abcca6f4e39b4955965"


def get_age_and_gender(name: str):
    params = {
        "name": name
    }
    age = requests.get(agify_url, params=params)
    gender = requests.get(genderize_url, params=params)

    return [age.json().get("age"), gender.json().get("gender")]


app = Flask(__name__)


@app.route("/")
def root():
    random_num = random.randint(1, 100)
    year = datetime.now().year
    return render_template("index.html", num=random_num, year=year)


@app.route("/guess/<name>")
def guess(name: str):
    age, gender = get_age_and_gender(name)
    return render_template(
        "guess.html",
        name=name.title(),
        age=age,
        gender=gender
    )


@app.route("/blog")
def blog():
    response = requests.get(blog_posts_url)
    posts = response.json()
    return render_template("blog.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
