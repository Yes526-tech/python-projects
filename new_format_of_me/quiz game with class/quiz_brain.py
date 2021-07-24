class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number}: {current_question.text}. (True/False): ")
        self.check_number(user_answer, current_question.answer)
    def check_number(self):
        if user_number.lower() == correct_number.lower():
            print("you got right.")
        else:
            print("that's wrong.")
        print(f"the correct answer was : {correct_answer}.")
