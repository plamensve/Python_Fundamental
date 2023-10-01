name_of_gifts = input().split(" ")

command = input()
new_list = []

while command != 'No Money':
    new_string = command.split()
    for current_string in new_string:
        new_list.append(current_string)
    if new_list[0] == 'OutOfStock':
        if new_list[1] in name_of_gifts:
            index = name_of_gifts.index(new_list[1])
            name_of_gifts[index] = 'None'





