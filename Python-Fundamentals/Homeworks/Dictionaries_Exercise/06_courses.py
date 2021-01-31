def print_students(lst_course):
    for student in sorted(lst_course):
        print(f"-- {student}")


courses = {}
registered_students = {}

data = input()

while not data == "end":
    course_name, student_name = data.split(" : ")

    if course_name not in courses:
        courses.update({course_name: [student_name]})
        registered_students.update({course_name: 1})
    else:
        courses[course_name].append(student_name)
        registered_students[course_name] += 1

    data = input()

for course, student_count in sorted(registered_students.items(), key=lambda x: -x[1]):
    print(f"{course}: {student_count}")
    print_students(courses[course])

