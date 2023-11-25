cities = input()
cities_dict = {}
while True:
    if cities == 'Sail':
        break

    current_city = cities.split('||')
    city, population, gold = current_city[0], int(current_city[1]), int(current_city[2])
    if city not in cities_dict:
        cities_dict[city] = {'population': population, 'gold': gold}
    else:
        cities_dict[city]['population'] += population
        cities_dict[city]['gold'] += gold
    cities = input()

command = input()
while True:
    if command == 'End':
        break
    current_command = command.split('=>')
    action = current_command[0]

    if action == 'Plunder':
        city, peoples, gold = current_command[1], current_command[2], current_command[3]
        cities_dict[city]['population'] -= int(peoples)
        cities_dict[city]['gold'] -= int(gold)
        print(f"{city} plundered! {gold} gold stolen, {peoples} citizens killed.")
        if cities_dict[city]['population'] == 0 or cities_dict[city]['gold'] == 0:
            del cities_dict[city]
            print(f"{city} has been wiped off the map!")

    elif action == 'Prosper':
        city, gold = current_command[1], current_command[2]
        if int(gold) < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities_dict[city]['gold'] += int(gold)
            print(f"{gold} gold added to the city treasury. {city} now has {cities_dict[city]['gold']} gold.")
    command = input()

if len(cities_dict) > 0:
    print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
    for key, value in cities_dict.items():
        print(f"{key} -> Population: {cities_dict[key]['population']} citizens, Gold: {cities_dict[key]['gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")