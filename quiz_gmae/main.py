import random
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choice = choices
        self.answer = answer

    def check_answer(self, answer):
        if answer not in self.choice:
            raise ValueError("wrong information")
        return self.answer == answer


class Quiz:
    def __init__(self, questions):
        self.question = random.sample(questions, len(questions))
        self.questionIndex = 0
        self.score = 0
    def get_question(self):
        return self.question[quiz.questionIndex]

    def display_question(self):
        question = self.get_question()

        print(f"question {self.questionIndex + 1}: {question.text}")

        for q in question.choice:
            print("-" + q)





q1 = Question("which one is the best programming language?", ["python", "c#", "java", "dart"], "python")
list_1 = [q1]
quiz = Quiz(list_1)

print(quiz.display_question())