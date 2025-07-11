from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

question_bank=[]
for qa in question_data:
    q=Question(qa['question'],qa['correct_answer'])
    question_bank.append(q)

quiz=QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz!")
print(f"Final score is: {quiz.correct_answer}/{quiz.question_number}")