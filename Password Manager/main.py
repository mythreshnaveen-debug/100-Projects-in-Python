from tkinter import *
from tkinter import messagebox
import os
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generatePassword(nr_letters = random.randint(8,10), nr_symbols=random.randint(2,4), nr_numbers=random.randint(2,4)):

    lns = [letters, numbers, symbols]
    gLNS = [nr_letters, nr_numbers, nr_symbols]

    fancyList = [lns, gLNS]

    passwordList = []
    # This piece of code took me way too long to debug.
    # Finally, after getting a piece of paper and writing my thoughts out, was I actually able to figure it out.
    for i in range(0, len(gLNS)):
        for i2 in range(0, gLNS[i]):
            passwordList.append(random.choice(lns[i]))
    random.shuffle(passwordList)
    password = ""
    for i in passwordList:
        password += i
    PassEntry.delete(0, 'end')
    PassEntry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    newText = WebsiteEntry.get() + "|" + EmUsEntry.get() + "|" + PassEntry.get()
    with open("passwords.txt", mode='a') as file:
        file.write("\n"+newText)
    messagebox.showinfo(title="New Password Added", message=f"We have saved your information.\nSAVEDINFO: {newText}\n\nYou can find this at: {os.path.abspath("passwords.txt")}")
# ---------------------------- UI SETUP ------------------------------- #
Screen = Tk()
Screen.title("Password Manager")
Screen.config(padx=20,pady=20)

canvas = Canvas(height=200,width=200)
logoImg = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logoImg)
canvas.grid(row=1,column=2)

WebsiteLabel = Label(text="Website:")
WebsiteLabel.grid(row=2,column=1)
WebsiteEntry = Entry(width=35)
WebsiteEntry.grid(row=2,column=2,columnspan=2)
EmUsLabel = Label(text="Email/Username:")
EmUsLabel.grid(row=3,column=1)
EmUsEntry = Entry(width=35)
EmUsEntry.grid(row=3,column=2,columnspan=2)
PassLabel = Label(text="Password:")
PassLabel.grid(row=4,column=1)
PassEntry = Entry(width=21)
PassEntry.grid(row=4,column=2)
PassBtn = Button(text="Generate Password", width=35-21, command=generatePassword)
PassBtn.grid(row=4,column=3)
AddBtn = Button(text="Add",width=36, command=add_password)
AddBtn.grid(row=5,column=2,columnspan=2)

Screen.mainloop()