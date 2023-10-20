initial_energy = int(input())
count_of_won_battles = 0
command = input()

while command != 'End of battle':
    current_command = int(command)

    if initial_energy < int(command):
        print(f"Not enough energy! Game ends with {count_of_won_battles} won battles and {initial_energy} energy")
        break
    else:
        initial_energy -= current_command
        count_of_won_battles += 1

    if count_of_won_battles % 3 == 0:
        initial_energy += count_of_won_battles

    command = input()
if command == 'End of battle':
    print(f"Won battles: {count_of_won_battles}. Energy left: {initial_energy}")

