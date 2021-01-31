# def side_function(side_add, user_add, book):
#     is_exist = False
#     if side_add not in book:
#         book[side_add] = []
#     for sd, us in book.items():
#         if user_add in us:
#             is_exist = True
#             break
#     if not is_exist:
#         book[side_add].append(user_add)
#     return book
#
#
# def user_function(side_tr, user_tr, book):
#     for sd, us in book.items():
#         if user_tr in us:
#             book[sd].remove(user_tr)
#             break
#
#     book[side_tr].append(user_tr)
#     return book


force_book = {}

command = input()

while not command == "Lumpawaroo":
    if " -> " in command:
        force_user, force_side = command.split(" -> ")
       # force_book = user_function(force_side, force_user, force_book)
        if force_side not in force_book:
            force_book[force_side] = []

        for side, users in force_book.items():
            if force_user in users:
                force_book[side].remove(force_user)
                break

        force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    else:
        force_side, force_user = command.split(" | ")
        #force_book = side_function(force_side, force_user, force_book)
        is_exist = False
        if force_side not in force_book:
            force_book[force_side] = []

        for side, users in force_book.items():
            if force_user in users:
                is_exist = True
                break

        if not is_exist:
            force_book[force_side].append(force_user)

    command = input()

for side, members in sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0])):
    if len(members) > 0:
        print(f"Side: {side}, Members: {len(members)}")
    for user in sorted(members):
        print(f"! {user}")
