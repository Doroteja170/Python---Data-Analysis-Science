class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.correct_answer=0
    def still_has_question(self):
        return self.question_number<len(self.question_list)

    def next_question(self):
        q_num=self.question_number
        self.question_number += 1
        question=self.question_list[q_num]
        answer=input(f"Q.{q_num+1}: {question.text} (True/False)?: ")
        self.check_answer(answer,question.answer)

    def check_answer(self,answer,correct_answer):
        if answer.lower()==correct_answer.lower():
            self.correct_answer+=1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.correct_answer}/{self.question_number}")
        print('\n')



