string_line = input()
new_password = string_line

command = input()
while True:
    if command == 'Done':
        break
    current_command = command.split()

    if current_command[0] == 'TakeOdd':
        new_password = ''
        for index in range(len(string_line)):
            if index % 2 != 0:
                new_password += string_line[index]
        print(new_password)

    elif current_command[0] == 'Cut':
        sliced_part_one = int(current_command[1])
        sliced_part_two = int(current_command[2])
        sliced_first_part = new_password[sliced_part_one:]
        sliced_second_part = sliced_first_part[sliced_part_two:]
        result = new_password[:sliced_part_one] + sliced_second_part
        print(result)
        new_password = result

    elif current_command[0] == 'Substitute':
        substring = current_command[1]
        substitute = current_command[2]
        if substring in new_password:
            result = new_password.replace(substring, substitute)
            print(result)
            new_password = result
        else:
            print(f"Nothing to replace!")

    command = input()

print(f"Your password is: {new_password}")
