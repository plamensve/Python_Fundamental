encrypted_message = input()
list_word = [char for char in encrypted_message]

command = input()
while True:
    if command == 'Decode':
        break

    current_command = command.split('|')

    if current_command[0] == 'Move':
        slicing = int(current_command[1])
        list_word = list_word[slicing:] + list_word[:slicing]

    elif current_command[0] == 'Insert':
        index_for_insert = int(current_command[1])
        char_for_insert = current_command[2]
        list_word = list_word[:index_for_insert] + [char_for_insert] + list_word[index_for_insert:]

    elif current_command[0] == 'ChangeAll':
        for char in list_word:
            if char == current_command[1]:
                index = list_word.index(char)
                list_word[index] = current_command[2]

    command = input()

print(f"The decrypted message is:", ''.join(list_word))
# Провери индекса (има before в условието и може би заради това получавам 83 точки) test test
