from math import ceil
budget = float(input())
students = int(input())
price_flour = float(input())
price_single_egg = float(input())
price_single_apron = float(input())

free_package_flour = 0
for student in range(1, students + 1):
    if student % 5 == 0:
        free_package_flour += 1

total_price = price_single_apron * ceil(students * 1.2) + price_single_egg * 10 * students + price_flour * (students - free_package_flour)
diff = abs(budget - total_price)
if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{diff:.2f}$ more needed.")

