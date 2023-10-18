initial_treasure_chest = input().split("|")

input_data = input()
stolen_items = []
while input_data != 'Yohoho!':
    separated_data = input_data.split()
    command = separated_data[0]

    if command == "Loot":
        for item in range(1, len(separated_data)):
            if separated_data[item] not in initial_treasure_chest:
                initial_treasure_chest.insert(0, separated_data[item])
    elif command == "Drop":
        index = int(separated_data[-1])
        if index < len(initial_treasure_chest):
            removed = initial_treasure_chest.pop(index)
            initial_treasure_chest.append(removed)

    elif command == "Steal":
        count_steals = min(int(separated_data[-1]),
                           len(initial_treasure_chest))  # if the items are not enough to fulfill the command, take as much as there are
        stolen_items = []
        for steal in range(count_steals, 0, -1):
            stolen_items.append(initial_treasure_chest[-steal])
            initial_treasure_chest.remove(initial_treasure_chest[-steal])
        print(*stolen_items, sep=', ')  # print the stolen items
    input_data = input()
# print(*stolen_items, sep=', ')
items_length_sum = 0
if len(initial_treasure_chest) > 0:
    for item in initial_treasure_chest:
        items_length_sum += len(item)
    average_treasure_gain = items_length_sum / len(initial_treasure_chest)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
