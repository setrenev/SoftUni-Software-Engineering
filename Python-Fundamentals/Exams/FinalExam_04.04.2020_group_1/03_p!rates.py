def prosper(statistic, current_town, added_gold):
    if added_gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        statistic["gold"] += added_gold
        total_gold = statistic["gold"]
        print(f"{added_gold} gold added to the city treasury. {current_town} "
              f"now has {total_gold} gold.")
    return statistic


def plunder(statistic, current_town, killed_people, stolen_gold):
    statistic["population"] -= killed_people
    statistic["gold"] -= stolen_gold
    print(f"{current_town} plundered! {stolen_gold} gold stolen, {killed_people} citizens killed.")
    if statistic["population"] == 0 or statistic["gold"] == 0:
        statistic.clear()
    return statistic


towns = {}

line = input()
while not line == "Sail":
    town, population, gold = line.split("||")

    if town not in towns:
        towns[town] = {}
        towns[town]["population"] = int(population)
        towns[town]["gold"] = int(gold)
    else:
        towns[town]["population"] += int(population)
        towns[town]["gold"] += int(gold)

    line = input()

line = input()
while not line == "End":
    command = line.split("=>")
    command_type = command[0]
    town = command[1]

    if command_type == "Plunder":
        people = int(command[2])
        gold = int(command[3])
        towns[town] = plunder(towns[town], town, people, gold)
        if len(towns[town]) == 0:
            print(f"{town} has been wiped off the map!")
            towns.pop(town)

    elif command_type == "Prosper":
        gold = int(command[2])
        towns[town] = prosper(towns[town], town, gold)

    line = input()

town_gold = {}

for town, data in towns.items():
    for key, value in towns[town].items():
        if key == "gold":
            town_gold[town] = value

sorted_towns = dict(sorted(town_gold.items(), key=lambda x: (-x[1], x[0])))

count_of_towns = len(towns)

if count_of_towns == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
    for name, gold_value in sorted_towns.items():
        citizens = towns[name]["population"]
        print(f"{name} -> Population: {citizens} citizens, Gold: {gold_value} kg")
