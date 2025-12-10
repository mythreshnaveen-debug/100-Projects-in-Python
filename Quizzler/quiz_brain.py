class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.text} (True/False): "

    def check_answer(self, b):
        correct_answer = self.current_question.answer
        if correct_answer == "True":
            correct_answer = True
        else:
            correct_answer = False
        if bool(correct_answer) == bool(b):
            return True
        else:
            return False
