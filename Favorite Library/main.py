import random

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = str(random.randint(1,100))

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'books.db')}"


table = ["name", "author", "rating"]

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.name))
        all_books = result.scalars().all()
    return render_template('index.html', books=all_books, booksLength=len(all_books))

class newBookForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = FloatField('Rating (out of 10)', validators=[DataRequired()])
    submit = SubmitField('Add Book')


@app.route("/add", methods=['GET', 'POST'])
def add():
    errors = False
    newForm = newBookForm()
    if newForm.validate_on_submit():
        errors = False
        with app.app_context():
            newBook = Book(name=newForm.name.data, author=newForm.author.data, rating=float(newForm.rating.data))
            db.session.add(newBook)
            db.session.commit()

        return home()
    elif newForm.errors:
        errors = True

    return render_template('add.html', form = newForm, table=table, errors=errors)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("✅ Tables created")
    app.run(debug=True)