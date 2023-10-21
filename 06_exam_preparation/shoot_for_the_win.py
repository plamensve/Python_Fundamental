def valid_index(index):
    if 0 <= index < len(sequence):
        return True


sequence = [int(num) for num in input().split()]
command = input()
shot_target = 0
while True:
    if command == 'End':
        print(f"Shot targets: {shot_target} -> {' '.join(map(str, sequence))}")
        break
    current_command = int(command)
    index = valid_index(current_command)

    if index:
        if sequence[current_command] != -1:
            current_target = sequence[current_command]
            sequence[current_command] = -1
            for target in sequence:
                if target != -1 and target > current_target:
                    index_target = sequence.index(target)
                    target -= current_target
                    sequence[index_target] = target
                elif target != -1 and target <= current_target:
                    index_target = sequence.index(target)
                    target += current_target
                    sequence[index_target] = target
            shot_target += 1
    command = input()
