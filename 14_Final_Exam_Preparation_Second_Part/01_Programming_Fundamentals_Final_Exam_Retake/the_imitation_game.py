encrypted_message = input()

command = input()
while True:
    if command == 'Decode':
        break
    current_command = command.split('|')

    if current_command[0] == 'ChangeAll':
        substring, replacement = current_command[1], current_command[2]
        replace = encrypted_message.replace(substring, replacement)
        encrypted_message = replace

    elif current_command[0] == 'Insert':
        index, value = int(current_command[1]), current_command[2]
        result = list(encrypted_message)
        insert_char = result.insert(index, value)
        encrypted_message = f"{''.join(result)}"

    elif current_command[0] == 'Move':
        number_of_letters = int(current_command[1])
        removed = encrypted_message[:number_of_letters]
        second_part_of_string = encrypted_message[number_of_letters:]
        final_result = second_part_of_string + removed
        encrypted_message = final_result
    command = input()

print(f"The decrypted message is: {encrypted_message}")