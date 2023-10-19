dungeon_rooms = input().split("|")
initial_health = 100
bitcoins = 0
best_room = 0
you_win = True

for room in dungeon_rooms:
    best_room += 1
    action, points = room.split()

    if action == 'potion':
        # healed = min(int(points), initial_health - current_health)
        current_health = initial_health
        initial_health += int(points)
        if initial_health > 100:
            initial_health = 100
        amount = initial_health - current_health
        print(f"You healed for {amount} hp.")
        print(f"Current health: {initial_health} hp.")

    elif action == 'chest':
        bitcoins += int(points)
        print(f"You found {points} bitcoins.")

    else:
        initial_health -= int(points)
        if initial_health > 0:
            print(f"You slayed {action}.")
        else:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {best_room}")
            you_win = False
            break

if you_win:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {initial_health}")

