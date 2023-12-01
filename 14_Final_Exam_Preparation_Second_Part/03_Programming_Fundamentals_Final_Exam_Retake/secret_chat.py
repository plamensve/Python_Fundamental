concealed_message = input()

command = input()
while True:
    if command == 'Reveal':
        break
    current_command = command.split(':|:')

    if current_command[0] == 'InsertSpace':
        result = list(concealed_message)
        insert_space = result.insert(int(current_command[1]), ' ')
        concealed_message = ''.join(result)
        print(concealed_message)

    elif current_command[0] == 'Reverse':
        substring = current_command[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, '', 1)
            concealed_message += substring[::-1]
            print(concealed_message)
        else:
            print('error')

    elif current_command[0] == 'ChangeAll':
        substring = current_command[1]
        replacement = current_command[2]
        result = concealed_message.replace(substring, replacement)
        concealed_message = result
        print(concealed_message)
    command = input()

print(f"You have a new text message: {concealed_message}")