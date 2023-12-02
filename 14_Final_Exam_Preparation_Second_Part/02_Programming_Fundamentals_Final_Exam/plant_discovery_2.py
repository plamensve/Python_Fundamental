import re


def command_validation(command):
    pattern = r'\b([A-Za-z]+):\s([A-Za-z]+)\s-\s\d+|\b([A-Za-z]+):\s([A-Za-z]+)\b'
    matches_rate_update = re.findall(pattern, command)
    if matches_rate_update:
        return True
    return False


numbers = int(input())
plant_rarity_info = {}
plant_rating_info = {}

for _ in range(numbers):
    plant_rarity = input().split('<->')
    plant_name, rarity = plant_rarity[0], int(plant_rarity[1])
    plant_rarity_info[plant_name] = rarity
    plant_rating_info[plant_name] = []

command = input()

if command_validation(command):
    while True:
        current_command = command.split(' ')
        if current_command[0] == 'Rate:':
            plant_name, rating = current_command[1], int(current_command[3])
            if plant_name in plant_rarity_info:
                plant_rating_info[plant_name].append(rating)
            else:
                print('error')

        elif current_command[0] == 'Update:':
            plant_name, update_rarity = current_command[1], int(current_command[3])
            if plant_name in plant_rarity_info:
                plant_rarity_info[plant_name] = update_rarity
            else:
                print('error')

        elif current_command[0] == 'Reset:':
            plant_name = current_command[1]
            if plant_name in plant_rating_info:
                plant_rating_info[plant_name] = []
            else:
                print('error')
        command = input()
        if not command_validation(command):
            break

if command == 'Exhibition':
    print(f"Plants for the exhibition:")
    for k, v in plant_rarity_info.items():
        plant_name_k = k
        if len(plant_rating_info[plant_name_k]) > 0:
            print(
                f"- {k}; Rarity: {v}; Rating: {sum(plant_rating_info[plant_name_k]) / len(plant_rating_info[plant_name_k]):.2f}")
        else:
            print(
                f"- {k}; Rarity: {v}; Rating: 0.00")
else:
    command = input()
    command_validation(command)
