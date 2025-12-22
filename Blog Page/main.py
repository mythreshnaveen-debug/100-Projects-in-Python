from flask import Flask, render_template
import requests, random

app = Flask(__name__)
json = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391').json()

@app.route("/")
def main():
    return render_template('index.html', random_num=random, posts=json)

@app.route("/blogs/<int:blog_id>")
def blog(blog_id):
    for post in json:
        if blog_id == post["id"]:
            return render_template('blogs.html', post=post)
    return "<h1>Not Found</h1>"

if __name__ == "__main__":
    app.run(debug=True)
