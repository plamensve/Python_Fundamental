number_of_lines = int(input())

tank_capacity = 255
pour_into_tank = 0

for i in range(number_of_lines):
    poured_quantity = int(input())

    if tank_capacity < poured_quantity:
        print(f"Insufficient capacity!")
        continue
    else:
        tank_capacity -= poured_quantity
        pour_into_tank += poured_quantity

print(pour_into_tank)
