initial_schedule = input().split(", ")
exercise_flag = False
exercise_flag_string = ''
while True:
    try:
        current_command = input().split(":")
    except EOFError:
        break  # Прекратяваме цикъла при достигане на EOF

    if current_command[0] == 'course start':
        break  # Прекратяваме цикъла при въвеждане на "course start"

    if len(current_command) == 2:
        if current_command[0] == 'Add' and current_command[1] not in initial_schedule:
            initial_schedule.append(current_command[1])

        elif current_command[0] == 'Remove' and current_command[1] in initial_schedule:
            initial_schedule.remove(current_command[1])

        elif current_command[0] == 'Exercise':
            exercise_flag = True
            exercise_flag_string = current_command[1]
            initial_schedule.append(current_command[1])

    elif len(current_command) == 3:
        if current_command[0] == 'Insert' and current_command[1] not in initial_schedule:
            initial_schedule.insert(int(current_command[2]), current_command[1])

        elif current_command[0] == 'Swap' and current_command[1] in initial_schedule and current_command[2] in initial_schedule:
            index_x = initial_schedule.index(current_command[1])
            index_y = initial_schedule.index(current_command[2])
            initial_schedule[index_x], initial_schedule[index_y] = initial_schedule[index_y], initial_schedule[index_x]

if exercise_flag is True:
    for index, word in enumerate(initial_schedule):
        if word == exercise_flag_string:
            insert_index = index + 1
            initial_schedule.insert(insert_index, f'{word}-Exercise')

for index, item in enumerate(initial_schedule):
    print(f"{index + 1}.{item}")
