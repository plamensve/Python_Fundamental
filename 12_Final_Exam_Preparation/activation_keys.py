activation_key = input()

command = input()
while True:
    if command == 'Generate':
        print(f"Your activation key is: {activation_key}")
        break

    current_command = command.split('>>>')
    action = current_command[0]

    if action == 'Contains':
        if current_command[1] in activation_key:
            print(f"{activation_key} contains {current_command[1]}")
        else:
            print(f"Substring not found!")

    elif action == 'Flip':
        upper_or_lower_substring = current_command[1]
        start_index = int(current_command[2])
        end_index = int(current_command[3])
        if upper_or_lower_substring == 'Upper':
            result = activation_key[start_index:end_index].upper()
            upper_case = activation_key.replace(activation_key[start_index:end_index], result)
            activation_key = upper_case
            print(upper_case)
        else:
            result = activation_key[start_index:end_index].lower()
            lower_case = activation_key.replace(activation_key[start_index:end_index], result)
            activation_key = lower_case
            print(lower_case)

    elif action == 'Slice':
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        chars_for_remove = activation_key[start_index:end_index]
        activation_key = activation_key.replace(chars_for_remove, '')
        print(activation_key)
    command = input()