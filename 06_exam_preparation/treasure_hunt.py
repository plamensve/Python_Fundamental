def valid_index(current_index, length_loot):
    if 0 <= int(current_index) <= int(length_loot) - 1:
        return True


def sum_of_elements(parameter):
    length_count = 0
    for loot in parameter:
        length_count += len(loot)
    divider = len(parameter)
    try:
        result_loot = length_count / divider
        print(f"Average treasure gain: {result_loot:.2f} pirate credits.")
    except ZeroDivisionError:
        print(f"Failed treasure hunt.")


initial_loot = input().split("|")
list_with_removed_items = []
command = input()

while command != 'Yohoho!':
    current_command = command.split()
    action = current_command[0]

    if action == 'Loot':
        for item in current_command[1:]:
            if item not in initial_loot:
                initial_loot.insert(0, item)

    elif action == 'Drop':
        index = int(current_command[1])
        if valid_index(index, len(initial_loot) - 1):
            removed = initial_loot[index]
            initial_loot.remove(removed)
            initial_loot.append(removed)

    elif action == 'Steal':
        num = int(current_command[1])
        if num > len(initial_loot):
            for item in initial_loot:
                list_with_removed_items.append(item)
            initial_loot.clear()
        else:
            for item in initial_loot[-num:]:
                list_with_removed_items.append(item)
                initial_loot.remove(item)

    command = input()

print(", ".join(list_with_removed_items))
sum_of_elements(initial_loot)
