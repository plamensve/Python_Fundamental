dwarf_dict = {}
key_value = 1  # Инициализиране на ключовата стойност на 1
flag = False
while True:
    line = input()
    if line == 'Once upon a time':
        break

    dwarf = line.split(' <:> ')
    name, hat_color, physics = dwarf[0], dwarf[1], dwarf[2]
    physics = int(physics)
    dwarf_dict[key_value] = {'name': name, 'hat_color': hat_color, 'physics': physics}

    for k, v in dwarf_dict.items():
        if name in dwarf_dict[k]['name'] and hat_color in dwarf_dict[k]['hat_color'] and physics > dwarf_dict[k]['physics']:
            del dwarf_dict[k]
            flag = True
            break

    key_value += 1  # Увеличете ключовата стойност
if flag:
    sorted_dwarfs = sorted(dwarf_dict.values(), key=lambda x: x['hat_color'])
else:
    sorted_dwarfs = sorted(dwarf_dict.values(), key=lambda x: x['physics'], reverse=True)

for dwarf in sorted_dwarfs:
    print(f"({dwarf['hat_color']}) {dwarf['name']} <-> {dwarf['physics']}")
