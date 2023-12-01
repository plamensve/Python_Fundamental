number_of_cars = int(input())
cars_info = {}

for _ in range(number_of_cars):
    current_car = input().split('|')
    car_name, mileage, fuel = current_car
    cars_info[car_name] = {'mileage': int(mileage), 'fuel': int(fuel)}

command = input()
while True:
    if command == 'Stop':
        break
    current_command = command.split(' : ')

    if current_command[0] == 'Drive':
        car, distance, fuel = current_command[1], int(current_command[2]), int(current_command[3])
        if cars_info[car]['fuel'] > fuel:
            cars_info[car]['mileage'] += distance
            cars_info[car]['fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_info[car]['mileage'] > 100000:
                print(f"Time to sell the {car}!")
                del cars_info[car]
        else:
            print(f"Not enough fuel to make that ride")

    elif current_command[0] == 'Refuel':
        car, fuel = current_command[1], int(current_command[2])
        current_fuel = cars_info[car]['fuel']
        cars_info[car]['fuel'] += fuel
        if cars_info[car]['fuel'] > 75:
            refueled = current_fuel + fuel
            needed_fuel_a = refueled - 75
            needed_fuel_b = fuel - needed_fuel_a
            cars_info[car]['fuel'] = 75
            print(f"{car} refueled with {needed_fuel_b} liters")
        else:
            print(f"{car} refueled with {fuel} liters")

    elif current_command[0] == 'Revert':
        car, km = current_command[1], int(current_command[2])
        cars_info[car]['mileage'] -= km
        if cars_info[car]['mileage'] < 10000:
            cars_info[car]['mileage'] = 10000
        else:
            print(f"{car} mileage decreased by {km} kilometers")
    command = input()

for k, v in cars_info.items():
    print(f"{k} -> Mileage: {cars_info[k]['mileage']} kms, Fuel in the tank: {cars_info[k]['fuel']} lt.")