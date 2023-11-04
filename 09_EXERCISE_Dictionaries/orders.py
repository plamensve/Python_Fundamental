command = input()
products = {}

while command != 'buy':
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if product not in products.keys():
        products[product] = [price, quantity]
    else:
        products[product][0] = price
        products[product][1] += quantity

    command = input()

total = {}
for k, v in products.items():
    total[k] = float(v[0]) * float(v[1])

for x, y in total.items():
    print(f"{x} -> {y:.2f}")
