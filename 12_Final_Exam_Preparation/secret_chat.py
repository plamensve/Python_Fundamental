concealed_message = input()


command = input()
while True:
    if command == 'Reveal':
        break

    current_command = command.split(':|:')
    if current_command[0] == 'InsertSpace':
        index = int(current_command[1])
        insert_command = concealed_message[:index] + ' ' + concealed_message[index:]
        concealed_message = insert_command
        print(concealed_message)

    elif current_command[0] == 'Reverse':
        substring = current_command[1]
        if current_command[1] in concealed_message:
            concealed_message = concealed_message.replace(substring, '', 1)
            concealed_message += substring[::-1]
            print(concealed_message)
        else:
            print('error')

    elif current_command[0] == 'ChangeAll':
        substring, replacement = current_command[1], current_command[2]
        for char in concealed_message:
            if substring in concealed_message:
                concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)

    command = input()

print(f"You have a new text message: {concealed_message}")

