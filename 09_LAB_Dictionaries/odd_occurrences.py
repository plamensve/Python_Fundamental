line = input().split()
my_list = []
for i in line:
    my_list.append(i.lower())

new_dict = {}
for x in my_list:
    new_dict[x] = my_list.count(x)

for y, z in new_dict.items():
    if z % 2 != 0:
        print(f"{y}", end=' ')
