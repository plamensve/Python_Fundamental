string_line = input()

command = input()
while True:
    if command == 'Finish':
        break
    current_command = command.split()

    if current_command[0] == 'Replace':
        current_char = current_command[1]
        new_char = current_command[2]
        result = string_line.replace(current_char, new_char)
        string_line = result
        print(string_line)

    elif current_command[0] == 'Cut':
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if 0 < start_index < len(string_line) and 0 < end_index < len(string_line):
            first_string = string_line[:start_index]
            second_string = string_line[end_index + 1:]
            final_string = first_string + second_string
            print(final_string)
        else:
            print(f"Invalid indices!")

    elif current_command[0] == 'Make':
        if current_command[1] == 'Upper':
            result = string_line.upper()
            string_line = result
            print(string_line)
        elif current_command[1] == 'Lower':
            result = string_line.lower()
            string_line = result
            print(string_line)

    elif current_command[0] == 'Check':
        substring = current_command[1]
        if substring in string_line:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")

    elif current_command[0] == 'Sum':
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if 0 < start_index < len(string_line) and 0 < end_index < len(string_line):
            cut_string = string_line[start_index:end_index + 1]
            ascii_sum_cut_string = 0
            for char in cut_string:
                ascii_sum_cut_string += ord(char)
            print(ascii_sum_cut_string)
        else:
            print(f"Invalid indices!")
    command = input()

