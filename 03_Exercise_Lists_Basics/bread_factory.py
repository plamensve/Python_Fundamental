working_day_events = input().split("|")
initial_energy = 100
initial_coins = 100
day_completed = True

for day in working_day_events:
    current_day = day.split("-")
    type_of_event = current_day[0]
    event_value = int(current_day[1])

    if type_of_event == 'rest':
        current_energy = initial_energy
        initial_energy += event_value
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    elif current_day[0] == 'order':
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            initial_energy += 50
            print(f"You had to rest!")

    else:
        if initial_coins >= event_value:
            initial_coins -= event_value
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            day_completed = False
            break

if day_completed is True:
    print(f"Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")



