from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

# db.create_all() Only needs to run once to create the DB


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":

        book = Book(
            title=request.form.get("title"),
            author=request.form.get("author"),
            rating=request.form.get("rating")
        )

        db.session.add(book)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    book_id = request.args.get("id")
    book = Book.query.get(book_id)
    if request.method == "POST":
        book.rating = request.form.get("rating")
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("rating.html", book=book)


@app.route("/delete", methods=["GET"])
def delete():
    book_id = request.args.get("id")
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
