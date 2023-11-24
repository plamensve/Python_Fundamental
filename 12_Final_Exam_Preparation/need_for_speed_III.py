number_of_cars = int(input())
list_with_cars = []


def create_car(name, mileage, fuel):
    car_name = name
    car_mileage = mileage
    car_fuel = fuel
    list_with_cars.append({'name': car_name, 'mileage': car_mileage, 'fuel': car_fuel})


def drive(car_name, mileage, fuel):
    for current_car in list_with_cars:
        if current_car['name'] == car_name:
            current_car['mileage'] = int(current_car['mileage'])
            current_car['fuel'] = int(current_car['fuel'])
            if current_car['fuel'] >= fuel:
                current_car['fuel'] -= fuel
                current_car['mileage'] += mileage
                if current_car['mileage'] > 100000:
                    print(f"{car_name} driven for {mileage} kilometers. {fuel} liters of fuel consumed.")
                    print(f"Time to sell the {car_name}!")
                    list_with_cars.remove(current_car)
                else:
                    print(f"{car_name} driven for {mileage} kilometers. {fuel} liters of fuel consumed.")
            else:
                print(f"Not enough fuel to make that ride")


def refuel(car_name, add_fuel):
    for current_car in list_with_cars:
        current_car['mileage'] = int(current_car['mileage'])
        current_car['fuel'] = int(current_car['fuel'])
        if current_car['name'] == car_name:
            current_quantity = current_car['fuel']
            if current_quantity + add_fuel > 75:
                current_car['fuel'] = 75
                added_quantity = 75 - current_quantity
                print(f"{car_name} refueled with {added_quantity} liters")
            else:
                current_car['fuel'] = current_car['fuel'] + add_fuel
                print(f"{car_name} refueled with {add_fuel} liters")


def revert(car_name, mileage):
    for current_car in list_with_cars:
        current_car['mileage'] = int(current_car['mileage'])
        current_car['fuel'] = int(current_car['fuel'])
        if current_car['name'] == car_name:
            if current_car['mileage'] - mileage < 10000:
                current_car['mileage'] = 10000
            else:
                current_car['mileage'] = current_car['mileage'] - mileage
                print(f"{car_name} mileage decreased by {mileage} kilometers")


for car in range(number_of_cars):
    car_info = input().split('|')
    create_car(car_info[0], car_info[1], car_info[2])

command = input()
while True:
    if command == 'Stop':
        break
    current_command = command.split(' : ')

    if current_command[0] == 'Drive':
        drive(current_command[1], int(current_command[2]), int(current_command[3]))

    elif current_command[0] == 'Refuel':
        refuel(current_command[1], int(current_command[2]))

    elif current_command[0] == 'Revert':
        revert(current_command[1], int(current_command[2]))

    command = input()

for current_car_info in list_with_cars:
    print(f"{current_car_info['name']} -> Mileage: {current_car_info['mileage']} kms, Fuel in the tank: {current_car_info['fuel']} lt.")

