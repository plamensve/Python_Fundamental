import re

names = input().split(', ')
racers = {}

command = input()
while command != 'end of race':
    regex_name = r'[A-Za-z]'
    regex_distance_sum = r'\d'
    matches_name = re.findall(regex_name, command)
    matches_distance = re.findall(regex_distance_sum, command)
    name = ''
    distance = 0
    for char in matches_name:
        name += char

    for num in matches_distance:
        distance += int(num)

    if name not in racers:
        racers[name] = distance
    else:
        racers[name] += distance

    name = ''
    distance = 0
    command = input()

sorted_data = sorted(racers.items(), key=lambda x: x[1], reverse=True)
winners = []

for name in sorted_data:
    if name[0] in names:
        winners.append(name[0])

first_second_third_place = winners[:3]
print(f'1st place: {first_second_third_place[0]}\n2nd place: {first_second_third_place[1]}\n3rd place: {first_second_third_place[2]}')
