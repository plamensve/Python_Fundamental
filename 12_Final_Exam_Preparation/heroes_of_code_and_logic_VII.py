number_of_heroes = int(input())

heroes = {}
for i in range(number_of_heroes):
    all_hero = input().split()
    hero_name, health, mana = all_hero[0], int(all_hero[1]), int(all_hero[2])
    heroes[hero_name] = {'health': health, 'mana': mana}

command = input()
while True:
    if command == 'End':
        break
    current_command = command.split(' - ')

    if current_command[0] == 'CastSpell':
        hero_name_for_action, mp_needed, spell_name = current_command[1], int(current_command[2]), current_command[3]
        if heroes[hero_name_for_action]['mana'] >= mp_needed:
            heroes[hero_name_for_action]['mana'] -= mp_needed
            print(f"{hero_name_for_action} has successfully cast {spell_name} and now has {heroes[hero_name_for_action]['mana']} MP!")
        else:
            print(f"{hero_name_for_action} does not have enough MP to cast {spell_name}!")

    elif current_command[0] == 'TakeDamage':
        hero_name_for_action, damage, attacker = current_command[1], int(current_command[2]), current_command[3]
        heroes[hero_name_for_action]['health'] -= damage
        if heroes[hero_name_for_action]['health'] > 0:
            print(f"{hero_name_for_action} was hit for {damage} HP by {attacker} and now has {heroes[hero_name_for_action]['health']} HP left!")
        else:
            print(f"{hero_name_for_action} has been killed by {attacker}!")
            removed = heroes.pop(hero_name_for_action)

    elif current_command[0] == 'Recharge':
        hero_name_for_action, amount_of_mana = current_command[1], int(current_command[2])
        heroes[hero_name_for_action]['mana'] += amount_of_mana
        if heroes[hero_name_for_action]['mana'] > 200:
            over_quantity_mana = heroes[hero_name_for_action]['mana'] - 200
            result = amount_of_mana - over_quantity_mana
            print(f"{hero_name_for_action} recharged for {result} MP!")
            heroes[hero_name_for_action]['mana'] = 200
        else:
            print(f"{hero_name_for_action} recharged for {amount_of_mana} MP!")

    elif current_command[0] == 'Heal':
        hero_name_for_action, amount_of_health = current_command[1], int(current_command[2])
        heroes[hero_name_for_action]['health'] += amount_of_health
        if heroes[hero_name_for_action]['health'] > 100:
            over_quantity_health = heroes[hero_name_for_action]['health'] - 100
            result = amount_of_health - over_quantity_health
            print(f"{hero_name_for_action} healed for {result} HP!")
            heroes[hero_name_for_action]['health'] = 100
        else:
            print(f"{hero_name_for_action} healed for {amount_of_health} HP!")

    command = input()

for k, v in heroes.items():
    print(f"{k}\nHP: {v['health']}\nMP: {v['mana']}")
