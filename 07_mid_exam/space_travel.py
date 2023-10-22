rout = input().split("||")
fuel = int(input())
ammunition = int(input())


while True:
    command = rout[0]
    if command == 'Titan':
        print(f"You have reached Titan, all passengers are safe.")
        break
    current_command = command.split()
    action = current_command[0]
    quantity = current_command[1]

    if current_command[0] == "Travel":
        fuel -= int(quantity)
        if fuel >= 0:
            print(f"The spaceship travelled {quantity} light-years.")
        else:
            print(f"Mission failed.")
            break

    elif current_command[0] == 'Enemy':
        if ammunition >= int(quantity):
            ammunition -= int(quantity)
            print(f"An enemy with {quantity} armour is defeated.")
        else:
            fuel -= int(quantity) * 2
            if fuel >= 0:
                print(f"An enemy with {quantity} armour is outmaneuvered.")
            else:
                print(f"Mission failed.")
                break

    elif current_command[0] == 'Repair':
        fuel += int(quantity)
        ammunition = int(quantity) * 2
        print(f"Ammunitions added: {int(quantity) * 2}.")
        print(f"Fuel added: {quantity}.")

    rout.pop(0)