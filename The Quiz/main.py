from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []
for question in question_data:
    questionBank.append(Question(question["text"], question["answer"]))
quiz = QuizBrain(questionBank)
while not quiz.endOfQuiz():
    quiz.nextQuestion()
print("------------\nEND OF QUIZ RESULTS:")
quiz.printUserSummary()
print("Thank you for playing our quiz!")