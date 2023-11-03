items = {"shards": 0,  "fragments": 0, "motes": 0}
obtained = False

while not obtained:
    current_material = input().split()
    for index in range(0, len(current_material), 2):
        key = current_material[index + 1].lower()
        value = int(current_material[index])
        if key not in items.keys():
            items[key] = 0

        items[key] += value

        if items['shards'] >= 250:
            print(f'Shadowmourne obtained!')
            items['shards'] -= 250
            obtained = True

        elif items['fragments'] >= 250:
            print(f'Valanyr obtained!')
            items['fragments'] -= 250
            obtained = True

        elif items['motes'] >= 250:
            print(f'Dragonwrath obtained!')
            items['motes'] -= 250
            obtained = True

        if obtained:
            break

for k, v in items.items():
    print(f'{k}: {v}')