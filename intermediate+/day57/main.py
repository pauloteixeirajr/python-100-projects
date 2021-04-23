import random
import requests
from datetime import datetime
from flask import Flask, render_template

agify_url = "https://api.agify.io"
genderize_url = "https://api.genderize.io"


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


if __name__ == "__main__":
    app.run(debug=True)
