cards_list = input().split()
shuffles_count = int(input())

final_order = []

for shuffle in range(shuffles_count):
    first_half = cards_list[:len(cards_list)//2]
    second_half = cards_list[-len(cards_list)//2:]
    final_order = [cards_list[0]]

    for i in range(len(cards_list)//2 - 1):
        final_order.append(second_half[i])
        final_order.append(first_half[i+1])

    final_order.append(cards_list[-1])
    cards_list = final_order

print(final_order)