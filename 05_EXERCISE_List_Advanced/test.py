initial_schedule = input().split(", ")

while True:
    current_command = input().split(":")
    if current_command != 'course start':
        if len(current_command) == 2:
            if current_command[0] == 'Add' and current_command[1] not in initial_schedule:
                initial_schedule.append(current_command[1])

            elif current_command[0] == 'Remove' and current_command[1] in initial_schedule:
                initial_schedule.remove(current_command[1])

            elif current_command[0] == 'Exercise':
                if current_command[1] in initial_schedule:
                    initial_schedule.append(current_command[0] + current_command[1])
                else:
                    initial_schedule.append(current_command[1] + '-' + current_command[0])

        elif len(current_command) == 3:
            if current_command[0] == 'Insert' and current_command[1] not in initial_schedule:
                initial_schedule.insert(int(current_command[2]), current_command[1])

            elif current_command[0] == 'Swap' and current_command[1] in initial_schedule and current_command[2] in initial_schedule:
                index_x = initial_schedule.index(current_command[1])
                index_y = initial_schedule.index(current_command[2])
                initial_schedule[index_x], initial_schedule[index_y] = initial_schedule[index_y], initial_schedule[index_x]
        else:
            for index, item in enumerate(initial_schedule):
                print(f"{index + 1}.{item}")


