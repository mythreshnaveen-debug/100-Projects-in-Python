# Day 66 (for me to remember)

from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Integer, String, Boolean, update
import random as r

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "id": self.id,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price,
        }



with app.app_context():
    db.create_all()


def pythonify():
    """
    Converts the SQL All_Cafes, and the Cafe class to be more python friendly.
    """
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    newAllCafes = [] # I know this isn't proper Python Variable argsatting, but as someone coming from
    # Luau and JS, I can't really stop my weird argsatting ways.
    for cafe in all_cafes:
        newAllCafes.append(cafe.to_dict())
    return newAllCafes

@app.route("/")
def home():
    return redirect("https://documenter.getpostman.com/view/49196489/2sBXVcjsQv")

# HTTP GET - Read Record
# HTTP POST - Create Record
# HTTP PUT/PATCH - Update Record
# HTTP DELETE - Delete Record

@app.route("/random", methods=["GET"])
def random():
    all_cafes = pythonify()
    random_cafe = r.choice(all_cafes)
    return jsonify(random_cafe)

@app.route("/all", methods=["GET"])
def all():
    return jsonify(pythonify())

@app.route("/search", methods=["GET"])
def search():
    loc = request.args.get("loc")
    all_cafes = pythonify()
    cafes_user_wants = []
    for cafe in all_cafes:
        if cafe["location"] == loc:
            cafes_user_wants.append(cafe)
    return cafes_user_wants

@app.route("/add", methods=["POST"])
def add():
    name = request.args.get("name")
    map_url = request.args.get("map_url")
    img_url = request.args.get("img_url")
    location = request.args.get("location")
    seats = request.args.get("seats")
    has_toilet = bool(request.args.get("has_toilet", 0))
    has_wifi = bool(request.args.get("has_wifi", 0))
    has_sockets = bool(request.args.get("has_sockets", 0))
    can_take_calls = bool(request.args.get("can_take_calls", 0))

    coffee_price = request.args.get("coffee_price")

    new_cafe = Cafe(
        name=name,
        map_url=map_url,
        img_url=img_url,
        location=location,
        seats=seats,
        has_toilet=has_toilet,
        has_wifi=has_wifi,
        has_sockets=has_sockets,
        can_take_calls=can_take_calls,
        coffee_price=coffee_price
    )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success":"published"})
@app.route("/update-price/<id>",methods=["PATCH"])
def change_price(id):
    if request.method == "PATCH":
        try:
            int(id)
        except ValueError:
            return jsonify(response={"error":"id should be an integer"}), 400
        try:
            cafe = db.session.get(Cafe, int(id))
            if not cafe:
                return jsonify(response={"error":"cafe not found"}), 404
            cafe.coffee_price = request.args.get("new_price")
            db.session.commit()
        except AttributeError:
            return jsonify(response={"error":"cafe not found"}), 400
        return jsonify(response={"success":"updated"}), 200
    return jsonify(response={"error":"this branch only allows patch requests"}), 405

@app.route("/report-closed/<id>", methods=["DELETE"])
def report_closed(id):
    if request.method == "DELETE":
        api_key = request.args.get("api_key")
        if api_key == 'TopSecretAPIKey':
            try:
                int(id)
            except ValueError:
                return jsonify(response={"error":"id should be an integer"}), 400
            try:
                cafe = db.session.get(Cafe, int(id))
                if not cafe:
                    return jsonify(response={"error":"cafe not found"}), 404
                db.session.delete(cafe)
                db.session.commit()
                return jsonify(response={"success":"closed"}), 200
            except AttributeError:
                return jsonify(response={"error":"cafe not found"}), 400
        else:
            return jsonify(response={"error":"Incorrect API Key"}), 401
    else:
        return jsonify(response={"error":"this branch only allows delete requests"}), 405
    return jsonify(response={"coffee": "im a teapot"}), 418



if __name__ == '__main__':
    app.run(debug=True,threaded=False, use_reloader=False, port=8000)