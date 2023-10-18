initial_list = input().split("!")

command = input()
while command != 'Go Shopping!':
    current_command = command.split()

    action = current_command[0]
    item = current_command[1]

    if action == 'Urgent':
        if item not in initial_list:
            initial_list.insert(0, item)

    elif action == 'Unnecessary':
        if item in initial_list:
            initial_list.remove(item)

    elif action == 'Correct':
        if item in initial_list:
            index = initial_list.index(item)
            initial_list.remove(item)
            initial_list.insert(index, current_command[2])

    elif action == 'Rearrange':
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)
    command = input()

print(", ".join(initial_list))