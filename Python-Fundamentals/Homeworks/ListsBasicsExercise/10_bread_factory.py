working_day_events = input().split("|")

energy = 100
coins = 100

is_manage_all = True

for event in working_day_events:
    event_name, number = event.split("-")
    number = int(number)

    if event_name == "rest":
        if energy + number > 100:
            energy = 100
            number = 100 - energy
        else:
            energy += number
        print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")

    elif event_name == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if number <= coins:
            coins -= number
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            is_manage_all = False
            break

if is_manage_all:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
