# (Project 57) Demographic Name and Gender App (DNaG)

A simple Flask web application that provides estimated **age** and **gender** for a given name using public APIs. (README made by AI.)

---

## Features

* Enter a name in the URL (e.g., `localhost:5000/John`) to see demographic predictions.
* Displays:

  * Estimated **Gender**
  * Estimated **Age**
* Lightweight and easy to run locally.
* Built with **Flask** and uses **Genderize.io** and **Agify.io** APIs.

---

## Installation

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd <repo-folder>
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

3. **Install dependencies**

```bash
pip install Flask requests
```

---

## Usage

1. Run the Flask app:

```bash
python main.py
```

2. Open your browser and go to:

```
http://localhost:5000/
```

3. To see demographic data, append a name to the URL. Example:

```
http://localhost:5000/Emily
```

The page will display:

* Name entered
* Predicted gender
* Estimated age

---

## File Structure

```
├── main.py          # Flask application
├── templates/
│   ├── index.html   # Home page
│   └── result.html  # Result page displaying age & gender
└── README.md
```

---

## APIs Used

1. **[Genderize.io](https://genderize.io/)** – Predicts gender based on a first name.
2. **[Agify.io](https://agify.io/)** – Predicts age based on a first name.

---

## Notes

* Predictions are estimates and may not be accurate for all names.
* Make sure you have an active internet connection to fetch data from the APIs.

---

## License

This project is open-source and free to use.
