lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_money_needed = 0
broken_shield_count = 0

for fight in range(1, lost_fight_count +1):
    if fight % 2 == 0:
        total_money_needed += helmet_price

    if fight % 3 == 0:
        total_money_needed += sword_price
        if fight % 2 == 0:
            total_money_needed += shield_price
            broken_shield_count += 1

    if broken_shield_count == 2:
        total_money_needed += armor_price
        broken_shield_count = 0

print(f"Gladiator expenses: {total_money_needed:.2f} aureus")
