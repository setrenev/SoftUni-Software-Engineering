def check_house(hearts, visited_house):
    if hearts <= 0:
        print(f"Place {visited_house} already had Valentine's day.")
    else:
        hearts -= 2
        if hearts <= 0:
            print(f"Place {visited_house} has Valentine's day.")

    return hearts


neighborhood = [int(element) for element in input().split("@")]

house_number = 0

while True:
    command = input().split()
    if command[0] == "Love!":
        break

    jump = int(command[1])
    house_number += jump

    if house_number not in range(len(neighborhood)):
        house_number = 0

    neighborhood[house_number] = check_house(neighborhood[house_number], house_number)

failed_houses = len([house for house in neighborhood if house > 0])

print(f"Cupid's last position was {house_number}.")
if failed_houses > 0:
    print(f"Cupid has failed {failed_houses} places.")
else:
    print("Mission was successful.")
