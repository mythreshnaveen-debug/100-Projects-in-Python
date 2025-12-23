
# Project 61 - 🔐 Flask Secrets Login App

A simple Flask web application that demonstrates **form handling, validation, authentication logic, and CSRF protection** using **Flask-WTF**. Users must log in with the correct credentials to access a “top secret” page—otherwise, access is denied (with a meme).

This project is primarily for **learning purposes**, not production security. *(README Made by AI)*

---

## 🚀 Features

* Flask backend with multiple routes
* Secure random `SECRET_KEY` generation using Python’s `secrets` module
* Login form built with **Flask-WTF**
* Email validation using `email-validator`
* Password length enforcement
* CSRF protection
* Success / Access Denied pages
* Clean separation of templates

---

## 🧠 What This Project Teaches

* How Flask routing works
* How to use `FlaskForm` and WTForms
* Server-side form validation
* CSRF protection in Flask
* Basic authentication logic
* Rendering templates with Jinja2

---

## 📂 Project Structure

```
.
├── main.py
├── requirements.txt
└── templates
    ├── index.html
    ├── login.html
    ├── success.html
    └── denied.html
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Install dependencies

**Windows**

```bash
python -m pip install -r requirements.txt
```

**macOS / Linux**

```bash
pip3 install -r requirements.txt
```

---

### 3️⃣ Run the app

```bash
python main.py
```

The app will start on:

```
http://127.0.0.1:5000/
```

---

## 🔑 Login Credentials

Use the following credentials to access the secret page:

* **Email:** `admin@email.com`
* **Password:** `12345678`

Anything else will result in **Access Denied**.

> ⚠️ These credentials are **hardcoded** and are for demonstration only.

---

## 🔐 Security Notes

* A **new random SECRET_KEY** is generated on every app startup
* Passwords are **not hashed**
* No database is used
* Not intended for real authentication systems

This project focuses on **learning Flask fundamentals**, not production-grade security.

---

## 📦 Dependencies

From `requirements.txt`:

* Flask
* Flask-WTF
* WTForms
* Bootstrap-Flask
* Werkzeug
* email-validator

---

## 📸 Screens

* **Home page** → Welcome + Login button
* **Login page** → Email + password validation
* **Success page** → Rickroll 😄
* **Denied page** → Dog fail meme 🐶

---

## 🧪 Ideas to Improve

* Hash passwords using `werkzeug.security`
* Store users in a database (SQLite)
* Add registration
* Improve styling with Bootstrap
* Add sessions instead of direct comparison

---

## 📜 License

This project is open-source and free to use for educational purposes.
