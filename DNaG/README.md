# Project 58 - Demographic Name & Gender App (DNaG)

A simple Flask web application that predicts the **demographic age and gender** of a person based on their name.
It uses the **Genderize** and **Agify** public APIs to fetch predictions and displays them in a clean HTML interface.

---

## 🚀 Features

* Predicts **gender** from a given name
* Predicts **average age** associated with the name
* Simple URL-based input (no forms needed)
* Lightweight Flask setup
* Uses real-world public APIs

---

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **HTML**
* **Requests** library
* **Genderize API**
* **Agify API**

---

## 📂 Project Structure

```
project/
│
├── main.py
├── templates/
│   ├── index.html
│   └── result.html
```

---

## ⚙️ Installation & Setup

### 1. Clone or download the project

```bash
git clone https://github.com/yourusername/dnag-app.git
cd dnag-app
```

### 2. Install dependencies

Make sure you have Python installed, then run:

```bash
pip install flask requests
```

### 3. Run the application

```bash
python main.py
```

The app will start on:

```
http://localhost:5000
```

---

## 🧪 How to Use

1. Open your browser
2. Go to:

   ```
   http://localhost:5000
   ```
3. Append a name to the URL:

   ```
   http://localhost:5000/John
   ```
4. View the predicted **gender** and **age** for that name

---

## 📄 Example Output

**URL**

```
/Emily
```

**Page Content**

```
Results for Emily
You are probably female.
According to the demographic, you are around 29 years old.
```

---

## 🧠 How It Works

* The app takes the name from the URL
* Sends the name to:

  * `https://api.genderize.io`
  * `https://api.agify.io`
* Parses the returned JSON data
* Displays results using Flask templates

---

## ⚠️ Notes

* Predictions are **statistical estimates**, not guarantees
* API results may return `null` for uncommon names
* Debug mode is enabled for development only

---

## 📜 License

This project is open-source and free to use for learning and experimentation.
