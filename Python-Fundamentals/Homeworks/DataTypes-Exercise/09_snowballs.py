snowballs_count = int(input())

snowballs_value_max = 0
snowball_snow = 0
snowball_time = 0
snowball_quality = 0

for snowball in range(snowballs_count):
    current_snowball_snow = int(input())
    current_snowball_time = int(input())
    current_snowball_quality = int(input())
    current_snowball_value = int((current_snowball_snow / current_snowball_time) ** current_snowball_quality)

    if current_snowball_value > snowballs_value_max:
        snowballs_value_max = current_snowball_value
        snowball_snow = current_snowball_snow
        snowball_time = current_snowball_time
        snowball_quality = current_snowball_quality

print(f"{snowball_snow} : {snowball_time} = {snowballs_value_max} ({snowball_quality})")