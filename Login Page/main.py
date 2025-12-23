import secrets
import string

from flask import Flask, render_template
from flask_wtf import FlaskForm
from pandas.io.sas.sas_constants import encoding_names
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, AnyOf, Length, Email
import email_validator

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

chars = string.ascii_letters + string.digits + string.punctuation
result = ''.join(secrets.choice(chars) for _ in range(32))
print("THE SECRET KEY IS: " + result)

app.config["SECRET_KEY"] = result


class MyForm(FlaskForm):
    name = StringField('email', validators=[Email(message="Please enter a valid email."), DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, message="For your own safety, you must have 8 letters minimum in your password.")])
    login = SubmitField('Log In')

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/login", methods=["GET", "POST"])
def login():
    newForm = MyForm()
    errors = []
    if newForm.validate_on_submit():
        email = newForm.name.data
        password = newForm.password.data
        if email == "admin@email.com" and password == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    else:
        if "name" in newForm.errors:
            errors.append("Invalid Email.")
    return render_template('login.html', form=newForm, errors=errors)
if __name__ == '__main__':
    app.run(debug=True)
