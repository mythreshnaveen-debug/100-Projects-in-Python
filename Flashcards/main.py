from tkinter import *
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards")
window.config(pady=50,padx=50, bg=BACKGROUND_COLOR)

wordsList = pandas.DataFrame(pandas.read_csv("data/french_words.csv"))
currentWordIndex = 0

def changeCurrentWord():
    global currentWordIndex
    words = wordsList.get("French").to_list()
    currentWordIndex = random.randint(0, len(words) - 1)
    canvas.itemconfig(langText, text="French")
    canvas.itemconfig(wordText, text=words[currentWordIndex])
    canvas.itemconfig(card, image=cardBack)
def flipCard():
    global currentWordIndex
    words = wordsList.get("English").to_list()
    canvas.itemconfig(langText, text="English")
    canvas.itemconfig(wordText, text=words[currentWordIndex])
    canvas.itemconfig(card, image=cardFront)


cardFront = PhotoImage(file="images/card_front.png")
cardBack = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400,526/2,image=cardFront)
canvas.grid(row=0,column=0,columnspan=2)
langText = canvas.create_text(400,150,text="French",font=("Arial", 40, "italic"))
wordText = canvas.create_text(400, 263, text="trouve",font=("Arial", 60, "bold"))


wrongBtn = Button(image=wrong, highlightthickness=0, command=flipCard)
wrongBtn.grid(row=1,column=0)
rightBtn = Button(image=right, highlightthickness=0, command=changeCurrentWord)
rightBtn.grid(row=1,column=1)

changeCurrentWord()

window.mainloop()