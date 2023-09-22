orders = int(input())
total_amount = 0

for i in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    needed_capsules_per_day = int(input())

    if needed_capsules_per_day < 1 or needed_capsules_per_day > 2000:
        continue
    elif price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    elif days < 1 or days > 31:
        continue

    total = price_per_capsule * (days * needed_capsules_per_day)
    print(f"The price for the coffee is: ${total:.2f}")
    total_amount += total

print(f'Total: ${total_amount:.2f}')