import random
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)

    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all", methods=["GET"])
def get_all_cafes():
    cafes = db.session.query(Cafe).all()

    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search", methods=["GET"])
def search_cafe():
    location = request.args.get("location").title()
    cafes = Cafe.query.filter_by(location=location).all()

    if not cafes:
        return jsonify(error={
            "Not Found": f"Sorry, we don't have a cafe at {location}"
        }), 404

    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    cafe_data = request.form
    print(cafe_data)
    new_cafe = Cafe(
        name=cafe_data.get("name"),
        map_url=cafe_data.get("map_url"),
        img_url=cafe_data.get("img_url"),
        location=cafe_data.get("location"),
        seats=cafe_data.get("seats"),
        has_toilet=cafe_data.get("has_toilet") == "true",
        has_wifi=cafe_data.get("has_wifi") == "true",
        has_sockets=cafe_data.get("has_sockets") == "true",
        can_take_calls=cafe_data.get("can_take_calls") == "true",
        coffee_price=cafe_data.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe"})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("price")
    cafe = Cafe.query.get(cafe_id)

    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()

        return jsonify({"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": f"Cafe with id {cafe_id} not found."}), 404


# HTTP DELETE - Delete Record

if __name__ == '__main__':
    app.run(debug=True)
