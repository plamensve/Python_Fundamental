encrypted_message = input()
list_word = []
for c in encrypted_message:
    list_word.append(c)

command = input()
while command != 'Decode':
    current_command = command.split('|')
    if current_command[0] == 'ChangeAll':
        for char in list_word:
            if char == current_command[1]:
                index = list_word.index(char)
                list_word[index] = current_command[2]

    elif current_command[0] == 'Insert':
        index_for_insert = int(current_command[1])
        char_for_insert = current_command[2]
        list_word.insert(index_for_insert, char_for_insert)

    elif current_command[0] == 'Move':
        symbol_for_move = []
        slicing = int(current_command[1])
        moved_characters = list_word[:slicing]
        for ch in moved_characters:
            symbol_for_move.append(ch)

        for char in moved_characters:
            if char in list_word:
                list_word.remove(char)
        sum_of_list = list_word + symbol_for_move
        list_word = sum_of_list
    command = input()

print(f"The decrypted message is:", ''.join(list_word))
# Провери индекса (има before в условието и може би заради това получавам 83 точки)
