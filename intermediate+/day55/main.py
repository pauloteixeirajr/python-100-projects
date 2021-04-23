from flask import Flask
from my_dec import make_bold, make_emphasis, make_underline

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"


@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello, {name}. You are number {number + 1}"


class User:
    def __init__(self, name) -> None:
        self.name = name
        self.is_logged_in = False


def is_authenticated(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper


@is_authenticated
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Paulo")
create_blog_post(new_user)

if __name__ == '__main__':
    app.run(debug=True)
