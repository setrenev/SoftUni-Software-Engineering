first_employee_efficient = int(input())
second_employee_efficient = int(input())
third_employee_efficient = int(input())
people_count = int(input())

total_time = 0
handled_people = 0

while handled_people < people_count:
    total_time += 1
    handled_people += (first_employee_efficient + second_employee_efficient + third_employee_efficient)
    if total_time % 4 == 0:
        total_time += 1

print(f"Time needed: {total_time}h.")
