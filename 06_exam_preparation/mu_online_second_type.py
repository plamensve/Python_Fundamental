initial_health = 100
bitcoins = 0
dungeon_rooms = input().split("|")
current_health = initial_health
best_room = 0
you_win = True

for room in dungeon_rooms:
    best_room += 1
    action, points = room.split()

    if action == 'potion':
        healed = min(int(points), initial_health - current_health) # Проверка, дали надвишаваме 100 initial_health
        current_health += healed
        if initial_health > 100:
            initial_health = 100
        amount = initial_health - current_health
        print(f"You healed for {healed} hp.")
        print(f"Current health: {current_health} hp.")

    elif action == 'chest':
        bitcoins += int(points)
        print(f"You found {points} bitcoins.")

    else:
        current_health -= int(points)
        if not current_health <= 0:
            print(f"You slayed {action}.")
        else:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {best_room}")
            you_win = False
            break

if you_win:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {current_health}")