from tkinter import *
import json
from tkinter import messagebox
import os
# ---------------------------- SEARCH NOTES ----------------------------- #
def find_notes():
    NotesName = NameOfNotesEntry.get()
    with open("data.json") as file:
        data = json.load(file)
        if NotesName in data:
            messagebox.showinfo(NameOfNotesEntry.get(), message=data[NotesName]["Notes"])
        else:
            messagebox.showerror("That isn't correct!", f"{NotesName} is not a valid name in our files.")
    # ---------------------------- SAVE NOTES ------------------------------- #
def save_notes():
    newData = {
        NameOfNotesEntry.get(): {
            'Notes': f"""
TOPIC: {TopicEntry.get()}
NOTES:
{NotesEntry.get()}"""
        }
    }
    with open("data.json", "r") as file:
        data = json.load(file)
        data.update(newData)
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    messagebox.showinfo(title="New Notes Added", message=f"We have saved your information.\nYou can find this at: {os.path.abspath("data.json")}\n\nYou can also search for the topic name. \nHint: It is {NameOfNotesEntry.get()}")
# ---------------------------- UI SETUP --------------------------------- #
Screen = Tk()
Screen.title("QuickNotes")
Screen.config(padx=20,pady=20)

canvas = Canvas(height=200,width=200)
logoImg = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logoImg)
canvas.grid(row=1,column=2)

NameOfNotesLabel = Label(text="Name of Notes:")
NameOfNotesLabel.grid(row=2,column=1)
NameOfNotesEntry = Entry(width=21)
NameOfNotesEntry.grid(row=2,column=2)
SearchBtn = Button(text="Search", command=find_notes)
SearchBtn.grid(row=2,column=3)
TopicLabel = Label(text="Topic:")
TopicLabel.grid(row=3,column=1)
TopicEntry = Entry(width=35)
TopicEntry.grid(row=3,column=2,columnspan=2)
NotesLabel = Label(text="Notes:")
NotesLabel.grid(row=4,column=1)
NotesEntry = Entry(width=35)
NotesEntry.grid(row=4,column=2, columnspan=2)
AddBtn = Button(text="Add",width=36, command=save_notes)
AddBtn.grid(row=5,column=2,columnspan=2)

Screen.mainloop()