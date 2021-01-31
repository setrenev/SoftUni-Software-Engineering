red_cards = input()

players_team_a = 11
players_team_b = 11

team_a = []
team_b = []
is_terminate = False

list_of_red_cards = red_cards.split()

for element in list_of_red_cards:
    chosen_element = element.split("-")

    if players_team_a < 7 or players_team_b < 7:
        is_terminate = True
        break

    if chosen_element[0] == "A" and chosen_element[1] not in team_a:
        team_a.append(chosen_element[1])
        players_team_a -= 1
    if chosen_element[0] == "B" and chosen_element[1] not in team_b:
        team_b.append(chosen_element[1])
        players_team_b -= 1

print(f"Team A - {players_team_a}; Team B - {players_team_b}")
if is_terminate:
    print("Game was terminated")
