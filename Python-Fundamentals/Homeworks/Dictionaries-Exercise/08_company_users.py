companies = {}

command = input()

while not command == "End":
    company_name, employee_id = command.split(" -> ")

    if company_name not in companies:
        companies[company_name] = []

    if employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)

    command = input()

for company, employees in sorted(companies.items(), key=lambda x: x[0]):
    print(company)
    for emp in employees:
        print(f"-- {emp}")