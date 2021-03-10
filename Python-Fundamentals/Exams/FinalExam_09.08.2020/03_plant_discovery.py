discovered_plants = {}

n = int(input())

for _ in range(n):
    plant, rarity = input().split("<->")
    description = {"rarity": int(rarity), "ratings": []}
    discovered_plants[plant] = description

line = input()

while not line == "Exhibition":
    command, plant_and_value = line.split(": ")
    try:
        if command == "Rate":
            plant, rating = plant_and_value.split(" - ")
            discovered_plants[plant]["ratings"].append(int(rating))

        elif command == "Update":
            plant, new_rarity = plant_and_value.split(" - ")
            discovered_plants[plant]["rarity"] = int(new_rarity)

        elif command == "Reset":
            plant = plant_and_value
            discovered_plants[plant]["ratings"].clear()

    except:
        print("error")

    line = input()

for plant, value in discovered_plants.items():
    if len(discovered_plants[plant]["ratings"]) > 0:
        avg_rating = sum(discovered_plants[plant]["ratings"]) / len(discovered_plants[plant]["ratings"])
    else:
        avg_rating = 0
    value["avg_rating"] = avg_rating

sorted_plants = sorted(discovered_plants.items(), key=lambda x: (-x[1]["rarity"], -x[1]["avg_rating"]))

print("Plants for the exhibition:")
for plant, value in sorted_plants:
    print(f"- {plant}; Rarity: {value['rarity']}; Rating: {value['avg_rating']:.2f}")
