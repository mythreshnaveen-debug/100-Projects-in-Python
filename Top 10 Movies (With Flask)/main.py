import os

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, NumberRange, URL
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'movies.db')}"

Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    review: Mapped[str] = mapped_column(String, nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False, unique=True)

@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
        all_movies = result.scalars().all()
    return render_template("index.html", movies=all_movies)

class EditForm(FlaskForm):
    rating = FloatField('Rating (out of 10 | eg 7.5)', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_movie(id):
    with app.app_context():
        movie = Movie.query.get(id)
        form = EditForm(obj=movie)
        if request.method == "POST":
            if form.validate_on_submit():
                form.populate_obj(movie)
                db.session.add(movie)
                db.session.commit()
                return redirect(url_for("home"))
    return render_template("edit.html", form=EditForm())
@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete_movie(id):
    with app.app_context():
        movie = Movie.query.get(id)
        db.session.delete(movie)
        db.session.commit()
        return redirect(url_for("home"))

class addMovie(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])
    ranking = IntegerField('Ranking', validators=[DataRequired(), NumberRange(min=1, max=10)])
    description = StringField('Description', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    image_url = StringField('Image URL', validators=[DataRequired(), URL()])
    submit = SubmitField('Submit')

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    newForm = addMovie()
    if request.method == "GET":
        return render_template("add.html", form=newForm)
    elif request.method == "POST":
        title = request.form["title"]
        rating = request.form["rating"]
        ranking = request.form["ranking"]
        description = request.form["description"]
        image_url = request.form["image_url"]
        year = request.form["year"]
        # adding the movie
        with app.app_context():
            newMovie = Movie(title=title, rating=rating, ranking=ranking, img_url=image_url,
                             description=description, review="No Review Set.", year=year)
            db.session.add(newMovie)
            db.session.commit()
            return redirect(url_for("home"))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
