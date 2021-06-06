student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
for student in student_scores:
    if student_scores[student] > 90 and student_scores[student] <= 100:
        outstanding_student = " outstanding"
        student_grades[student] = outstanding_student
    elif student_scores[student] > 80 and student_scores[student] <= 90:
        exceeds_expectations_student = " exceeds expectations"
        student_grades[student] = exceeds_expectations_student
    elif student_scores[student] > 70 and student_scores[student] <= 80:
        acceptable_student = " acceptable"
        student_grades[student] = acceptable_student
    elif student_scores[student] <= 70:
        fail_student = " fail"
        student_grades[student] = fail_student


# TODO-2: Write your code below to add the grades to student_grades.👇


# 🚨 Don't change the code below 👇
print(student_grades)
