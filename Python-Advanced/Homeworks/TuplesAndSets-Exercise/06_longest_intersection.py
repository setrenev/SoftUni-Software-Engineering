def find_intersection(ranges):
    first_element = max([int(el.split(",")[0]) for el in ranges])
    second_element = min([int(el.split(",")[1]) for el in ranges])
    result = list(range(first_element, second_element+1))
    return result


intersections = []

n = int(input())

for _ in range(n):
    intersection = find_intersection(input().split("-"))
    intersections.append(intersection)

sorted_intersections = sorted(intersections, key=lambda x: -len(x))

print(f"Longest intersection is {list(sorted_intersections[0])} with length {len(sorted_intersections[0])}")
