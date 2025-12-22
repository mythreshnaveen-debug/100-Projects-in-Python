
# Project 57 - 📰 NewGen Blogs (Flask App)

A simple Flask web application that displays blog posts fetched from an external JSON API. Users can view a list of blogs on the home page and click into individual blog posts using dynamic routes. (README made by AI)

---

## 📌 Features

* Fetches blog data from an external API
* Displays all blog titles and subtitles on the homepage
* Dynamic routing for individual blog posts
* Uses Flask + Jinja2 templating
* Lightweight and beginner-friendly project structure

---

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **HTML (Jinja2 templates)**
* **Requests library**

---

## 📂 Project Structure

```
.
├── main.py
├── templates
│   ├── index.html
│   └── blogs.html
```

---

## 🚀 Getting Started

### 1️⃣ Install Dependencies

Make sure Python is installed, then install Flask and Requests:

```bash
pip install flask requests
```

---

### 2️⃣ Run the Application

```bash
python main.py
```

Flask will start a local development server.

---

### 3️⃣ Open in Browser

Go to:

```
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

### `main.py`

* Fetches blog data from:

  ```
  https://api.npoint.io/c790b4d5cab58020d391
  ```
* `/` route:

  * Renders `index.html`
  * Displays all blog titles and subtitles
* `/blogs/<int:blog_id>` route:

  * Finds the blog with the matching ID
  * Renders `blogs.html`
  * Returns **Not Found** if the blog ID doesn’t exist

---

### `index.html`

* Loops through all blog posts
* Displays:

  * Title
  * Subtitle
  * Link to the full blog post

---

### `blogs.html`

* Displays a single blog post:

  * Title
  * Subtitle
  * Body content

---

## ⚠️ Notes

* This project runs in **debug mode**, which is great for development but should be disabled in production.
* Blog data is read-only and refreshed on server restart.
* No database is used — all data comes from the external API.

---

## 📚 Learning Goals

This project is great for practicing:

* Flask routing
* Dynamic URLs
* Jinja2 templating
* Working with APIs in Python

---

## ✅ Future Improvements (Optional Ideas)

* Add CSS styling
* Add a 404 template instead of plain HTML
* Cache API responses
* Add search or pagination
* Move API fetching into a separate module
