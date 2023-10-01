fire_cells = input().split('#')
water = int(input())
water_quantity = []

for current_type_of_fire in fire_cells:
    cell = current_type_of_fire.split()
    needed_water = int(cell[2])
    type_fire = cell[0]

    if type_fire == 'High':
        if 81 <= int(needed_water) <= 125:
            quantity = int(cell[2])
            water_quantity.append(quantity)
        else:
            continue

    if type_fire == 'Medium':
        if 51 <= int(needed_water) <= 80:
            quantity = int(cell[2])
            water_quantity.append(quantity)
        else:
            continue

    if type_fire == 'Low':
        if 1 <= int(needed_water) <= 50:
            quantity = int(cell[2])
            water_quantity.append(quantity)
        else:
            continue

print('Cells:')
total_fire = 0
for current_quantity_of_water in water_quantity:

    if current_quantity_of_water > water:
        water_quantity.remove(current_quantity_of_water)
    else:
        water -= current_quantity_of_water
        total_fire += current_quantity_of_water
        print(f"- {current_quantity_of_water}")

effort = total_fire * 0.25
print(f"Effort: {effort:.2f} ")
print(f"Total Fire: {total_fire}")



