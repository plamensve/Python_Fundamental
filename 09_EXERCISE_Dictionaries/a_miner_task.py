my_list = []
command = input()
while command != 'stop':

    if command == 'stop':
        break
    else:
        my_list.append(command)

    command = input()

my_dict = {}
for i in range(0, len(my_list) - 1, 2):
    res = my_list[i]
    qty = int(my_list[i + 1])
    if res in my_dict.keys():
        my_dict[res] += qty
    else:
        my_dict[res] = qty

for k, v in my_dict.items():
    print(f"{k} -> {v}")