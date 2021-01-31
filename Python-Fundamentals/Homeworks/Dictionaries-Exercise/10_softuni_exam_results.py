def add_result(exams, name, lang, pnt, count):
    if lang not in exams:
        exams[lang] = {}
        count[lang] = 0

    if name not in exams[lang]:
        exams[lang][name] = pnt
    else:
        if exams[lang][name] < pnt:
            exams[lang][name] = pnt

    count[lang] += 1
    return exams, count


def ban_student(exams, name):
    for lng, res in exams.items():
        for nm, pt in exams[lng].items():
            if name == nm:
                exams[lng][name] = 0

    return exams


results_by_languages = {}
results = {}
submissions = {}

command = input()

while not command == "exam finished":
    if len(command.split("-")) == 2:
        student = command.split("-")[0]
        results_by_languages = ban_student(results_by_languages, student)
    else:
        student, language, points = command.split("-")
        points = int(points)
        results_by_languages, submissions = add_result(results_by_languages, student, language, points, submissions)

    command = input()

for languages, result in results_by_languages.items():
    for names, point in results_by_languages[languages].items():
        if point > 0:
            results[names] = point

print("Results:")
for names, point in sorted(results.items(), key=lambda x: (-x[1], x[0])):
    print(f"{names} | {point}")

print("Submissions:")
for languages, total_submissions in sorted(submissions.items(), key=lambda x: (-x[1], x[0])):
    print(f"{languages} - {total_submissions}")
