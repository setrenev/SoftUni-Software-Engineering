students = {}
filtered_students = {}

n = int(input())

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in students:
        students.update({name: [grade, 1]})
    else:
        students[name][0] += grade
        students[name][1] += 1

for student in students:
    average_grade = students[student][0] / students[student][1]
    if average_grade >= 4.5:
        filtered_students.update({student: average_grade})

for student, grade in sorted(filtered_students.items(), key=lambda x: -x[1]):
    print(f"{student} -> {grade:.2f}")
