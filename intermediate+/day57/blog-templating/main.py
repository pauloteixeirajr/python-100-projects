import requests
from flask import Flask, render_template
from post import Post

api_url = "https://api.npoint.io/5abcca6f4e39b4955965"

app = Flask(__name__)

response = requests.get(api_url)
posts_data = response.json()
posts = []
for post in posts_data:
    new_post = Post(
        post.get("id"),
        post.get("title"),
        post.get("subtitle"),
        post.get("body"))
    posts.append(new_post)


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:post_id>")
def get_post(post_id):
    post = [p for p in posts if p.id == post_id]
    return render_template("post.html", post=post[0])


if __name__ == "__main__":
    app.run(debug=True)
