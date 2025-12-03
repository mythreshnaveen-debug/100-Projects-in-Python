class QuizBrain:
    def __init__(self, qL):
        self.question_number = 0
        self.question_list = qL
        self.score = 0
    def nextQuestion(self):
        self.question_number += 1
        question = self.question_list[self.question_number - 1]
        userGuess = input(f"Q.{self.question_number}: {question.text}")
        if userGuess == question.answer:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect.")
        print(f"The correct answer is: {question.answer}")
        print(f"Your current score is: {self.score} / {self.question_number}")
    def endOfQuiz(self):
        if len(self.question_list) == self.question_number:
            return True
        else:
            return False
    def printUserSummary(self):
        print(f"Your score is:  {self.score} / {self.question_number}")
        print(f"That is equivalent to {round(self.score / self.question_number, 4) * 100}%.")