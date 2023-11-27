number_line = int(input())
plant_info = {}

for i in range(number_line):
    plant = input().split('<->')
    plant_key, rarity = plant[0], int(plant[1])
    plant_info[plant_key] = [rarity, 0, 0]  # -> Index_0-Rarity, Index_1-Rating, Index_2-Counter of ratings

command = input()

while True:
    if command == 'Exhibition':
        break
    current_command = command.split(' ')

    if current_command[0] == 'Rate:':
        if current_command[1] in plant_info:
            if current_command[3].isdigit():
                plant_info[current_command[1]][1] += int(current_command[3])
                plant_info[current_command[1]][2] += 1
        else:
            print('error')

    elif current_command[0] == 'Update:':
        if current_command[1] in plant_info:
            if current_command[3].isdigit():
                plant_info[current_command[1]][0] = int(current_command[3])
        else:
            print('error')

    elif current_command[0] == 'Reset:':
        if current_command[1] in plant_info:
            plant_info[current_command[1]][1] = 0
        else:
            print('error')
    command = input()

print(f"Plants for the exhibition:")
for k, v in plant_info.items():
    print(f"- {k}; Rarity: {v[0]}; Rating: {v[1] / v[2]:.2f}")