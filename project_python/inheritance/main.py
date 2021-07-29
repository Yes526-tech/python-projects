class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person has been created")
    def intro(self):
        print(self.name, self.surname, self.age)

class Student(Person):
    def __init__(self, name, surname, age, number):
        Person.__init__(self, name, surname, age)
        self.number = number
        print("student has been created")
class Teacher(Person):
    def __init__(self, name, surname, age):
        Person.__init__(self, name, surname, age)
        print("teacher has been created")

p1 = Person("Ahmet", "Turan", 20)
p1.intro()
s1 = Student("Erdem", "Yilmaz", 26)
s1.intro()