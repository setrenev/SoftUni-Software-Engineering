def fill_lift(lst, ind, pl_count):
    for i in range(lst[ind]+1, 5):
        if pl_count > 0:
            pl_count -= 1
            lst[ind] += 1
    return lst[ind], pl_count


people_count = int(input())
lift = [int(el) for el in input().split()]

capacity = len(lift) * 4

for index in range(len(lift)):
    if lift[index] < 4 and people_count > 0:
        lift[index], people_count = fill_lift(lift, index, people_count)

if people_count == 0 and sum(lift) < capacity:
    print("The lift has empty spots!")
elif people_count > 0 and sum(lift) == capacity:
    print(f"There isn't enough space! {people_count} people in a queue!")

print(" ".join(str(el) for el in lift))
