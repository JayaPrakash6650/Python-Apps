class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?: ")
        self.check_answer(user_answer)
        self.question_number += 1

    def check_answer(self, check):
        if self.question_list[self.question_number].answer.lower() == check.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"That's wrong.\nThe correct answer was: {self.question_list[self.question_number].answer}")
        print(f"Your current score is: {self.score}/{self.question_number + 1}\n")
