import random
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def root():
    random_num = random.randint(1, 100)
    year = datetime.now().year
    return render_template("index.html", num=random_num, year=year)


if __name__ == "__main__":
    app.run(debug=True)
