def fire_action(index_action, damage_action):
    if 0 <= index_action < len(warship):
        warship[index_action] -= damage_action
        if warship[index_action] <= 0:
            print(f"You won! The enemy ship has sunken.")
            exit()


def defend_action(pirate_ship, startIndex, endIndex, damage):
    if 0 <= startIndex < len(pirate_ship) and 0 <= endIndex < len(pirate_ship):
        for i in range(startIndex, endIndex + 1):
            pirate_ship[i] -= damage
            if pirate_ship[i] <= 0:
                print(f"You lost! The pirate ship has sunken.")
                exit()


def repair_action(pirate_ship, index_pirate, health_pirate):
    if 0 <= index_pirate < len(pirate_ship):
        pirate_ship[index_pirate] = min(pirate_ship[index_pirate] + health_pirate, maximum_health_capacity)


pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
maximum_health_capacity = int(input())

command = input()
while command != 'Retire':
    current_command = command.split()
    action = current_command[0]

    if action == 'Fire':  # The pirate ship attacks the warship with the given damage at that section
        index, damage = int(current_command[1]), int(current_command[2])
        fire_action(index, damage)

    elif action == 'Defend':  # The warship attacks the pirate ship with the given damage at that range
        start_index, end_index, damage = int(current_command[1]), int(current_command[2]), int(current_command[3])
        defend_action(pirate_ship, start_index, end_index, damage)

    elif action == 'Repair':
        index, health = int(current_command[1]), int(current_command[2])
        repair_action(pirate_ship, index, health)

    elif action == 'Status':
        count = 0
        for section in pirate_ship:
            if section / maximum_health_capacity * 100 < 20:
                count += 1
        print(f"{count} sections need repair.")

    command = input()

print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship)}")