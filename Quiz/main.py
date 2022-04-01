from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
i = 0

while i < len(question_data):
    new_question = Question(question_data[i]["text"], question_data[i]["answer"])
    question_bank.append(new_question)
    i += 1

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"You've completed the quiz!\nYour final score is: {quiz.score}/{quiz.question_number}")
