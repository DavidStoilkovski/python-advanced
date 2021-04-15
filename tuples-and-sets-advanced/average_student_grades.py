n = int(input())

student_grades = {}

for _ in range(n):
    student, grade = input().split()
    grade = float(grade)
    if student not in student_grades:
        student_grades[student] = []
    student_grades[student].append(grade)


def average_grade(value):
    return sum(value) / len(value)


for (student, grades) in student_grades.items():
    avg = average_grade(grades)
    grades_string = " ".join(map(lambda grade: f'{grade:.2f}', grades))
    print(f'{student} -> {grades_string} (avg: {avg:.2f})')