# Project 31 — Flash Cards App (French ↔ English)  
*README generated with AI assistance.*

## 📘 Overview  
This project is a simple flash card language-learning app built using **Tkinter** and **pandas**.  
It displays a French word on a card, and gives the user the ability to:

- Flip the card to see the English translation  
- Load a new random French word  
- Practice vocabulary in a clean, simple UI  

This project is part of the Udemy 100 Days of Python course (Capstone Series: Days 31–35).

---

## 🧠 Features  

### ✔ Random Word Selection  
The app pulls words from `data/french_words.csv` and displays a random French word on each new card.

### ✔ Card Flipping Logic  
- Front → Shows **French**  
- Flip → Shows **English**  
The card graphic updates accordingly using `PhotoImage`.

### ✔ Buttons  
- ❌ Wrong button → **Flips** the current card  
- ✅ Right button → **Loads a new random word**

### ✔ GUI  
Built using:
- `Tk()`  
- `Canvas`  
- `Button`  
- PNG card images  

All images are centered correctly and kept referenced to avoid garbage collection.

---

## 🗂 File Structure  
```
project/
│
├── main.py
├── data/
│ └── french_words.csv
└── images/
├── card_front.png
├── card_back.png
├── right.png
└── wrong.png
```

---

## 🧩 How It Works  

### **1. Load the CSV**
```python
wordsList = pandas.DataFrame(pandas.read_csv("data/french_words.csv"))
```
### **2. Pick a Random French Word**
```python
currentWordIndex = random.randint(0, len(words) - 1)
```
### **3. Flip the Card**
```python
canvas.itemconfig(langText, text="English")
canvas.itemconfig(wordText, text=english_words[currentWordIndex])
canvas.itemconfig(card, image=cardFront)
```
## **4. Update Card Graphics**
Images stored in variables to prevent Tkinter garbage-collection.

---

## **🏁 Usage**
**1.** Run ```main.py```
**2.**Click ✓ to load a new French word
**3.**Click ✗ to flip to English
Repeat until you master the vocab!

---
### 🚀 Future Improvements
Track which words the user already mastered
Remove known words from rotation
Save progress to a file
Add a timer mode
Add pronunciation audio

