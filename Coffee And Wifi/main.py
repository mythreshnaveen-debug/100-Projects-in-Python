from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

table = ["cafe","locationURL","openTime","closeTime","wifiRating","coffeeRating","powerOutletRating"]

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    locationURL = StringField('Location (on Google Maps)', validators=[DataRequired(), URL()])
    openTime = TimeField('Open Time:', validators=[DataRequired()])
    closeTime = TimeField('Closing Time:', validators=[DataRequired()])
    wifiRating = SelectField('Wifi Rating', validators=[DataRequired()], choices=("✘","🛜","🛜🛜","🛜🛜🛜","🛜🛜🛜🛜","🛜🛜🛜🛜🛜"))
    coffeeRating = SelectField('Coffee Rating', validators=[DataRequired()], choices=['✘',"☕️","☕️☕️","☕️☕️☕️","☕️☕️☕️☕️","☕️☕️☕️☕️☕️"])
    powerOutletRating = SelectField('Power Outlet Rating', validators=[DataRequired()], choices=['✘',"🔌","🔌🔌","🔌🔌🔌","🔌🔌🔌🔌","🔌🔌🔌🔌🔌"])
    submit = SubmitField('Submit')
# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields ✅
# make coffee/wifi/power a select element with choice of 0 to 5. ✅
#e.g. You could use emojis ☕️/💪/✘/🔌 ✅
# make all fields required except submit ✅
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='\n', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file)
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


@app.route('/add', methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        errors = False
        with open("cafe-data.csv", mode="a", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            newRow = []
            for l in table:
                newRow.append(form[l].data)
            writer.writerow(newRow)
        return cafes()
    elif form.errors:
        errors = True
    else:
        errors = False


    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form, t=table, error=errors)


if __name__ == '__main__':
    app.run(debug=True)
