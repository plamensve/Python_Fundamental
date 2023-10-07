name_of_gifts = input().split(" ")
command = input()
new_list = []
list_length = len(name_of_gifts) - 1  # Check for out of range index

while command != 'No Money':
    new_string = command.split()

    for current_string in new_string:
        new_list.append(current_string)

    if new_list[0] == 'OutOfStock':
        while new_list[1] in name_of_gifts:
            index = name_of_gifts.index(new_list[1])
            name_of_gifts[index] = 'None'
        new_list = []
        command = input()
        continue

    elif new_list[0] == 'Required':
        index_required_change = new_list[2]
        if int(index_required_change) > int(list_length) or int(index_required_change) < 0:  # Check for out of range index
            command = input()
            new_list = []
            continue
        name_of_gifts[int(index_required_change)] = new_list[1]
        new_list = []
        command = input()
        continue

    elif new_list[0] == "JustInCase":
        length_of_list = len(name_of_gifts)
        index_required_change = length_of_list - 1
        name_of_gifts[int(index_required_change)] = new_list[1]
        new_list = []
        command = input()

while 'None' in name_of_gifts:
    removed = name_of_gifts.index('None')
    name_of_gifts.pop(removed)

print(*name_of_gifts, sep=' ')
