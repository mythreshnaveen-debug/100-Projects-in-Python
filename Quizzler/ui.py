from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, QuizBrain: QuizBrain):
        self.quiz = QuizBrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady = 20, bg=THEME_COLOR)

        BWImg = PhotoImage(file="images/false.png")
        BRImg = PhotoImage(file="images/true.png")

        self.Score = Label(text="Score: 0", bg=THEME_COLOR, fg="#FFFFFF")
        self.Score.grid(row=0,column=1)

        self.Canvas = Canvas()
        self.Canvas.config(height=250,width=300)
        self.Canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.CTxt = self.Canvas.create_text(150, 125, width=280,text="Q.1: In the original script of \"The Matrix\", the machines used humans as additional computing power instead of batteries. (True/False): ", font=("Arial", 20, "italic"))

        self.ButtonWrong = Button(image=BWImg, bg=THEME_COLOR, highlightthickness=0, command=lambda: self.check_answer(False))
        self.ButtonWrong.grid(row=2,column=0)

        self.ButtonRight = Button(image=BRImg, bg=THEME_COLOR, highlightthickness=0, command=lambda: self.check_answer(True))
        self.ButtonRight.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()
    def check_answer(self, b):
        if self.quiz.question_number != 10:
            if self.quiz.check_answer(b):
                self.quiz.score += 1
                self.Score.config(text=f"Score: {self.quiz.score}")
            self.get_next_question()
        else:
            self.Canvas.itemconfig(self.CTxt, text="You completed the quiz!")
    def get_next_question(self):
        if self.quiz.question_number < 10:
            self.Canvas.itemconfig(self.CTxt, text=self.quiz.next_question())
        else:
            messagebox.showerror("Complete!", "You have completed this quiz.")
