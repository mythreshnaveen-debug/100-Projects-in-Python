from flask import Flask, render_template

import requests

app = Flask(__name__)

json = requests.get("https://api.npoint.io/ed8fac99f5ee10634689").json()

@app.get("/")
def index():
    return render_template("index.html", posts=json)

@app.get("/posts/<id>")
def newPost(id):
    for post in json:
        if id == str(post["id"]):
            return render_template("post.html", post=post)
    return render_template("error.html")

@app.get("/<name>")
def everythingElse(name):
    if name == "index.html":
        return render_template("index.html", posts=json)
    elif name in {"about.html", "contact.html"}:
        return render_template(name)
    return render_template('error.html')

if __name__ == "__main__":
    app.run(debug=True)
