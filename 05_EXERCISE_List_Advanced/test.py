initial_schedule = input().split(', ')
while True:
    try:
        current_command = input().split(":")
    except EOFError:
        break  # Прекратяваме цикъла при достигане на EOF

    if current_command[0] == 'course start':
        break  # Прекратяваме цикъла при въвеждане на "course start"

    action = current_command[0]
    lesson = current_command[1]
    exercise = lesson + "-Exercise"

    if action == 'Add':
        initial_schedule.append(lesson)

    elif action == 'Insert':
        if lesson not in initial_schedule:
            index = int(current_command[2])
            initial_schedule.insert(index, current_command[1])

    elif action == 'Remove':
        if lesson in initial_schedule:
            initial_schedule.remove(lesson)

    elif action == 'Swap':
        if current_command[1] in initial_schedule and current_command[2] in initial_schedule:
            index_x = initial_schedule.index(current_command[1])
            index_y = initial_schedule.index(current_command[2])
            initial_schedule[index_x], initial_schedule[index_y] = initial_schedule[index_y], initial_schedule[index_x]

    elif action == 'Exercise':
        if lesson not in initial_schedule:
            initial_schedule.append(lesson)
            initial_schedule.append(exercise)

        elif lesson in initial_schedule:
            initial_schedule.append(exercise)

for index, item in enumerate(initial_schedule):
    print(f"{index + 1}.{item}")
