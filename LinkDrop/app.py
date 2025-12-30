from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB = "links.db"


def get_db():
    return sqlite3.connect(DB)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        note = request.form.get("note")

        if url:
            db = get_db()
            db.execute(
                "INSERT INTO links (url, note, created_at) VALUES (?, ?, ?)",
                (url, note, datetime.now().strftime("%Y-%m-%d %H:%M"))
            )
            db.commit()
            db.close()

        return redirect("/links")

    return render_template("index.html")


@app.route("/links")
def links():
    db = get_db()
    cursor = db.execute(
        "SELECT url, note, created_at, id FROM links ORDER BY id DESC"
    )

    links = [
        {"url": row[0], "note": row[1], "created_at": row[2], "id": row[3]}
        for row in cursor.fetchall()
    ]

    db.close()
    return render_template("links.html", links=links)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/delete/<id>")
def delete(id):
    db = get_db()
    db.execute("DELETE FROM links WHERE id = ?", (id,))
    db.commit()
    db.close()
    return redirect("/links")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
