def loading_bar(num):
    bar = "[..........]"
    new_bar = bar.replace(".", "%", num // 10)
    return new_bar


number = int(input())

if number == 100:
    print("100% Complete!")
    print(loading_bar(number))
else:
    print(f"{number}% {loading_bar(number)}")
    print("Still loading...")
