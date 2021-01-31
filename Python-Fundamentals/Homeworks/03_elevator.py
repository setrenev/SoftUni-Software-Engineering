people_count = int(input())
capacity = int(input())

courses_count = people_count // capacity
if not people_count % capacity == 0:
    courses_count += 1

print(courses_count)
