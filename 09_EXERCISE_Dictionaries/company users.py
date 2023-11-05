command = input()
my_dict = {}
while command != 'End':
    current_command = command.split(' -> ')
    name, num = current_command
    if name not in my_dict:
        my_dict[name] = [num]
    else:
        if num not in my_dict[name]:
            my_dict[name].append(num)
    command = input()


for k, v in my_dict.items():
    print(f"{k}")
    for name in v:
        print(f"-- {name}")