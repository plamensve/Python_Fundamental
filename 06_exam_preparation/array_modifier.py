numbers = [int(s) for s in input().split()]
command = input()

while command != 'end':
    current_command = command.split()
    action = current_command[0]

    if action == 'swap':
        index_1 = int(current_command[1])
        index_2 = int(current_command[2])
        numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]

    elif action == 'multiply':
        index_1 = int(current_command[1])
        index_2 = int(current_command[2])
        result = numbers[index_1] * numbers[index_2]
        numbers[index_1] = result

    elif action == "decrease":
        for pos in range(len(numbers)):
            numbers[pos] -= 1
    command = input()

final_list = [str(i) for i in numbers]

print(', '.join(final_list))