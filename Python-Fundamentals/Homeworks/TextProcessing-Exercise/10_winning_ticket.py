def ticket_jackpot(l_half, r_half):
    result = False
    for match_symbol in winning_symbols:
        if l_half == match_symbol * 10 and r_half == l_half:
            print(f'ticket "{l_half}{r_half}" - 10{match_symbol} Jackpot!')
            result = True
            break
    return result


def ticket_win(l_half, r_half):
    result = False
    match_length = []
    for match_symbol in winning_symbols:
        if match_symbol * 6 in l_half and match_symbol * 6 in r_half:
            match_length.append(l_half.count(match_symbol))
            match_length.append(r_half.count(match_symbol))
            print(f'ticket "{l_half}{r_half}" - {min(match_length)}{match_symbol}')
            result = True
            break
    return result


tickets = input().split(", ")

winning_symbols = ["@", "#", "$", "^"]

for ticket in tickets:
    ticket = ticket.strip()

    if not len(ticket) == 20:
        print('invalid ticket')
        continue

    left_half = ticket.strip()[:10]
    right_half = ticket.strip()[10:]

    if ticket_jackpot(left_half, right_half):
        continue

    if ticket_win(left_half, right_half):
        continue

    print(f'ticket "{ticket}" - no match')
