# Day 56 - Personal Portfolio

A simple personal portfolio website built using **Flask** and a static HTML template. This project serves as an introduction to backend web development with Python while showcasing a clean, responsive frontend design.

(README made by AI)
## ✨ Features

* Flask-powered backend
* Single route serving a portfolio homepage
* Responsive, modern UI using **Astral by HTML5 UP**
* Sections for:

  * Home / Introduction
  * Work / About
  * Contact
* Static asset handling (CSS, JS, images)

## 🧠 Tech Stack

* **Python**
* **Flask**
* **HTML5**
* **CSS3**
* **JavaScript**
* **HTML5 UP – Astral template**

## 📂 Project Structure

```
project/
│
├── main.py
├── templates/
│   └── index.html
│
├── static/
│   ├── assets/
│   │   ├── css/
│   │   └── js/
│   └── images/
│       └── me.jpg
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

Make sure you have Python installed, then install Flask:

```bash
pip install flask
```

### 3. Run the application

```bash
python main.py
```

### 4. Open in browser

Visit:

```
http://127.0.0.1:5000/
```

## 🧩 main.py Overview

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

* Initializes a Flask app
* Defines a single route (`/`)
* Renders `index.html` from the `templates` folder
* Runs in debug mode for development

## 🎨 Frontend Template

* Template: **Astral** by [HTML5 UP](https://html5up.net)
* License: Creative Commons Attribution 3.0
* Fully responsive and mobile-friendly

## 📬 Contact Form

The contact form is currently **frontend-only**.
(No backend logic is implemented yet for handling submissions.)

> Future improvements could include:

* Flask-WTF forms
* Email handling via SMTP
* Database storage

## 🛠️ Future Improvements

* Add backend form handling
* Deploy using Render / Railway / Vercel
* Add dynamic project cards
* Integrate a database
* Improve SEO and performance

## 📄 License

This project is free for personal and commercial use.
Frontend design courtesy of **HTML5 UP**.
