import random


class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, answer):
        if answer not in self.choices:
            raise ValueError("wrong info")
        return self.answer == answer


class Quiz:
    def __init__(self, questions):
        self.questions = random.sample(questions, len(questions))
        self.question_index = 0
        self.score = 0

    def get_question(self):
        return self.questions[self.question_index]

    def display_question(self):
        question = self.get_question()
        print(f"question {self.question_index + 1}: {question.text}")

        for q in question.choices:
            print("-" + q)

        answer = input("answer: ")
        if (question.check_answer(answer)):
            self.score += 1


        self.question_index += 1
        self.load_question()


    def load_question(self):
        if len(self.questions) == self.question_index:
            self.display_score()
        else:
            self.display_progress()

            self.display_question()
    def display_score(self):
        print("end of the quiz".center(100, "*"))
        score = 100 / len(self.questions)
        total_score = self.score * score
        print(f"you made {self.score}/{len(self.questions)}")
        print("score", total_score)


    def display_progress(self):
        total_question = len(self.questions)
        question_number = self.question_index + 1

        print(f"{question_number}/{total_question}".center(100, "*"))






q1 = Question("the best programming language", ["python", "c#", "java", "dart"], "python")
q2 = Question("the best value programming language", ["python", "c#", "java", "dart"], "python")
q3 = Question("the most populer programming language", ["python", "c#", "java", "dart"], "python")
quest = [q1, q2, q3]
quiz = Quiz(quest)
print(quiz.load_question())
