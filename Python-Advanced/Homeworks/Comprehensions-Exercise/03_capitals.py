countries = input().split(", ")
capitals = input().split(", ")

data = tuple(zip(countries, capitals))

[print(f"{country} -> {capital}") for country, capital in data]
