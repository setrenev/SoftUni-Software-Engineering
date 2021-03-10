def hero_forces(data, to_do, increase, hero_name):
    if to_do == "Recharge":
        current_mana_points = data["mana_points"]
        raised_mana = current_mana_points + increase
        if raised_mana > 200:
            increase = 200 - current_mana_points
            raised_mana = 200
        data["mana_points"] = raised_mana
        print(f"{hero_name} recharged for {increase} MP!")

    elif to_do == "Heal":
        current_hit_points = data["hit_points"]
        raised_hit = current_hit_points + increase
        if raised_hit > 100:
            increase = 100 - current_hit_points
            raised_hit = 100
        data["hit_points"] = raised_hit
        print(f"{hero_name} healed for {increase} HP!")

    return data


count_of_heroes = int(input())

heroes = {}

for index in range(count_of_heroes):
    hero = {}
    name, hp, mp = input().split()
    hero["hit_points"] = int(hp)
    hero["mana_points"] = int(mp)
    heroes[name] = hero

line = input()

while not line == "End":
    command = line.split(" - ")
    command_type = command[0]
    name = command[1]

    if len(command) == 3:
        amount = int(command[2])
        heroes[name] = hero_forces(heroes[name], command_type, amount, name)
    else:
        if command_type == "CastSpell":
            mana_needed = int(command[2])
            spell_name = command[3]
            if mana_needed > heroes[name]["mana_points"]:
                print(f"{name} does not have enough MP to cast {spell_name}!")
            else:
                new_mana_points = heroes[name]["mana_points"] - mana_needed
                heroes[name]["mana_points"] = new_mana_points
                print(f"{name} has successfully cast {spell_name} and now has {new_mana_points} MP!")

        elif command_type == "TakeDamage":
            damage = int(command[2])
            attacker = command[3]
            new_hit_points = heroes[name]["hit_points"] - damage
            heroes[name]["hit_points"] = new_hit_points
            if new_hit_points > 0:
                print(f"{name} was hit for {damage} HP by {attacker} and now has {new_hit_points} HP left!")
            else:
                heroes.pop(name)
                print(f"{name} has been killed by {attacker}!")

    line = input()

heroes_by_hit_points = {}

for hero, data_hero in heroes.items():
    heroes_by_hit_points[hero] = data_hero["hit_points"]

for name, hp in sorted(heroes_by_hit_points.items(), key=lambda x: (-x[1], x[0])):
    amount_of_mana = heroes[name]["mana_points"]
    print(name)
    print(f"  HP: {hp}")
    print(f"  MP: {amount_of_mana}")

# failed
