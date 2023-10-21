def valid_index(index):
    if 0 <= index < len(sequence):
        return True


def two_valid_index(parameter1, parameter2):
    if 0 <= parameter1 < len(sequence) and 0 <= parameter2 < len(sequence):
        return True


sequence = [int(num) for num in input().split()]
command = input()
while True:
    if command == 'End':
        print(f"{'|'.join(map(str, sequence))}")
        break

    current_command = command.split()
    action = current_command[0]
    if action == 'Shoot':
        index = valid_index(int(current_command[1]))
        if index:
            power = int(current_command[2])
            sequence[int(current_command[1])] -= power
            if sequence[int(current_command[1])] <= 0:
                sequence.remove(sequence[index])

    elif action == 'Add':
        index = valid_index(int(current_command[1]))
        if index:
            item = int(current_command[2])
            sequence.insert(int(current_command[1]), item)
        else:
            print(f"Invalid placement!")

    elif action == 'Strike':
        index = valid_index(int(current_command[1]))
        for_remove = sequence[int(current_command[1])]
        if index:
            rad_1 = int(current_command[1]) + int(current_command[2])
            rad_2 = int(current_command[1]) - int(current_command[2])
            two_valid_index(rad_1, rad_2)
            if two_valid_index(rad_1, rad_2):
                sequence.pop(rad_1)
                sequence.pop(rad_2)
                index_removed_item = sequence.index(for_remove)
                sequence.pop(int(index_removed_item))
            else:
                print(f"Strike missed!")

    command = input()
