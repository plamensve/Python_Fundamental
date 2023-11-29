number_of_pieces = int(input())

pieces_info = {}

for _ in range(number_of_pieces):
    piece = input().split('|')
    pieces_info[piece[0]] = {'composer': piece[1], 'key': piece[2]}

command = input()
while True:
    if command == 'Stop':
        break
    current_command = command.split('|')
    if current_command[0] == 'Add':
        if current_command[1] in pieces_info:
            print(f"{current_command[1]} is already in the collection!")
        else:
            pieces_info[current_command[1]] = {'composer': current_command[2], 'key': current_command[3]}
            print(f"{current_command[1]} by {current_command[2]} in {current_command[3]} added to the collection!")

    elif current_command[0] == 'Remove':
        if current_command[1] in pieces_info:
            pieces_info.pop(current_command[1])
            print(f"Successfully removed {current_command[1]}!")
        else:
            print(f"Invalid operation! {current_command[1]} does not exist in the collection.")

    elif current_command[0] == 'ChangeKey':
        if current_command[1] in pieces_info:
            old_key = pieces_info[current_command[1]]['key']
            pieces_info[current_command[1]]['key'] = current_command[2]
            print(f"Changed the key of {current_command[1]} to {current_command[2]}!")
        else:
            print(f"Invalid operation! {current_command[1]} does not exist in the collection.")

    command = input()

for k, v in pieces_info.items():
    print(f"{k} -> Composer: {pieces_info[k]['composer']}, Key: {pieces_info[k]['key']}")