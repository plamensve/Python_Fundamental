number_of_pieces = int(input())
pieces_dict = {}
for _ in range(number_of_pieces):
    string_line = input().split('|')
    pieces_dict[string_line[0]] = [string_line[1], string_line[2]]

command = input()

while True:
    if command == 'Stop':
        break
    current_command = command.split('|')
    if current_command[0] == 'Add':
        if current_command[1] in pieces_dict:
            print(f"{current_command[1]} is already in the collection!")
        else:
            pieces_dict[current_command[1]] = [current_command[2], current_command[3]]
            print(f"{current_command[1]} by {current_command[2]} in {current_command[3]} added to the collection!")

    elif current_command[0] == 'Remove':
        if current_command[1] in pieces_dict:
            pieces_dict.pop(current_command[1])
            print(f"Successfully removed {current_command[1]}!")
        else:
            print(f"Invalid operation! {current_command[1]} does not exist in the collection.")

    elif current_command[0] == 'ChangeKey':
        if current_command[1] in pieces_dict:
            for k, v in pieces_dict.items():
                if k == current_command[1]:
                    new_key = current_command[2]
                    pop_item = v.pop()
                    insert_item = v.insert(1, new_key)
                    print(f"Changed the key of {current_command[1]} to {current_command[2]}!")
        else:
            print(f"Invalid operation! {current_command[1]} does not exist in the collection.")
    command = input()

for k, v in pieces_dict.items():
    print(f"{k} -> Composer: {v[0]}, Key: {v[1]}")
