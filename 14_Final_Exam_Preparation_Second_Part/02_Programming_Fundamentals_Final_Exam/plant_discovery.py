numbers = int(input())
plant_info = {}
for _ in range(numbers):
    plants = input().split('<->')
    plants_name, rarity = plants
    plant_info[plants_name] = {"Rarity": int(rarity), "Ratings": []}

command = input()
while True:
    if command == 'Exhibition':
        break
    current_command = command.split(': ')

    if current_command[0] == 'Rate':
        plant_name, rating = current_command[1].split(' - ')
        if plant_name in plant_info:
            plant_info[plant_name]['Ratings'].append(int(rating))
        else:
            print('error')

    elif current_command[0] == 'Update':
        plant_name, rarity = current_command[1].split(' - ')
        if plant_name in plant_info:
            plant_info[plant_name]['Rarity'] = rarity
        else:
            print('error')

    elif current_command[0] == 'Reset':
        plant_name = current_command[1]
        if plant_name in plant_info:
            plant_info[plant_name]['Ratings'] = [0]

    command = input()

print(f"Plants for the exhibition:")
for k, v in plant_info.items():
    sum_of_ratings = sum(v['Ratings'])
    len_of_ratings = len(v['Ratings'])
    result = sum_of_ratings / len_of_ratings
    print(f"- {k}; Rarity: {v['Rarity']}; Rating: {result:.2f}")
