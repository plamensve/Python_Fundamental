string_line = input()
final_string_in_list = []


def take_odd():
    odd_string = ''
    for index in range(len(string_line)):
        if index % 2 != 0:
            odd_string += string_line[index]
            final_string_in_list.append(string_line[index])
    print(odd_string)


def cut(length, number_of_chars):
    global final_string_in_list
    sliced_string_first_part = final_string_in_list[:length]
    sliced_string_second_part = final_string_in_list[length:]
    sliced_string_third_part = sliced_string_second_part[number_of_chars:]
    result = sliced_string_first_part + sliced_string_third_part
    print(''.join(result))
    final_string_in_list = result  # Добавете този ред


def substitute(changed_symbol, symbol_for_changing):
    global final_string_in_list
    final_string_in_list_like_a_string = ''.join(final_string_in_list)
    if changed_symbol in final_string_in_list_like_a_string:
        final_string_in_list_like_a_string = final_string_in_list_like_a_string.replace(changed_symbol, symbol_for_changing)
        final_string_in_list = list(final_string_in_list_like_a_string)
        print(''.join(final_string_in_list))
    else:
        print(f'Nothing to replace!')


command = input()
while True:
    if command == 'Done':
        break
    current_command = command.split()

    if current_command[0] == 'TakeOdd':
        take_odd()

    elif current_command[0] == 'Cut':
        length_of_string, number_of_chars_for_remove = current_command[1], current_command[2]
        cut(int(length_of_string), int(number_of_chars_for_remove))

    elif current_command[0] == 'Substitute':
        changed_symbol, symbol_for_changing = current_command[1], current_command[2]
        substitute(changed_symbol, symbol_for_changing)

    command = input()

print(f"Your password is: {''.join(final_string_in_list)}")