sequence_of_elements = [num for num in input().split()]
command = input()
number_of_moves = 0
while command != 'end':
    number_of_moves += 1
    index = command.split()
    position_1 = int(index[0])
    position_2 = int(index[1])

    if (
            position_1 == position_2
            or position_1 >= len(sequence_of_elements)
            or position_2 >= len(sequence_of_elements)
            or position_1 < 0
            or position_2 < 0
    ):
        mid_index = len(sequence_of_elements) // 2
        sequence_of_elements.insert(mid_index, f"-{number_of_moves}a")
        sequence_of_elements.insert(mid_index + 1, f"-{number_of_moves}a")
        print(f"Invalid input! Adding additional elements to the board")

    else:
        item_1 = sequence_of_elements[position_1]
        item_2 = sequence_of_elements[position_2]
        if item_1 == item_2:
            sequence_of_elements.remove(item_1)
            sequence_of_elements.remove(item_2)
            print(f"Congrats! You have found matching elements - {item_1}!")
        else:
            print("Try again!")

    if len(sequence_of_elements) <= 0:
        break
    else:
        command = input()

if len(sequence_of_elements) > 0:
    result = ' '.join(map(str, sequence_of_elements))
    print(f"Sorry you lose :(\n{result}")
else:
    print(f"You have won in {number_of_moves} turns!")
