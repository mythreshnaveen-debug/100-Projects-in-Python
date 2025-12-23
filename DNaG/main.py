from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/<name>")
def results(name):
    genderizeTable = requests.get(f"https://api.genderize.io/?name={name}").json()
    agifyTable = requests.get(f"https://api.agify.io/?name={name}").json()

    return render_template('result.html', name=name, gender=genderizeTable["gender"], age=str(agifyTable["age"]))
if __name__ == "__main__":
    app.run(debug=True)
