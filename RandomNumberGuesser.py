#Project 54 - Random Number Guesser
#This is a simple page I built using flask, which allows you to guess a number (localhost:5000/number)
#and it says if they're too high, or too low, or at the number.
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h2>Welcome to the number guesser!</h2>"\
            "<p> Your goal is go guess a random number between 1 and 9.</p>\n<p>Good Luck!</p>\n<img src=\"https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif\">"

@app.route('/<num>')
def guess(num):
    number = int(num)
    if number > 3:
        return "<h2>Sorry, TOO HIGH!</h2>"
    elif number < 3:
        return "<h2>Sorry, TOO LOW!</h2>"
    return "<h2>Good Job! You found the number!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
