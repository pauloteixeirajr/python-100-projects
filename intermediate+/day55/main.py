from flask import Flask

app = Flask(__name__)


@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello, {name}. You are number {number + 1}"


if __name__ == '__main__':
    app.run(debug=True)
