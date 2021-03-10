room_count = int(input())

total_free_chairs = 0
is_enough_chairs = True

for room in range(1, room_count + 1):
    room_state = [el for el in input().split()]
    chairs_count = int(len(room_state[0]))
    taken_chairs = int(room_state[1])
    if taken_chairs <= chairs_count:
        total_free_chairs += chairs_count - taken_chairs
    else:
        print(f"{taken_chairs - chairs_count} more chairs needed in room {room}")
        is_enough_chairs = False

if is_enough_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
