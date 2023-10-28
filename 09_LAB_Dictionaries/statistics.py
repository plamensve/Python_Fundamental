stock = {}
while True:
    line = input()
    if line == 'statistics':
        break

    product, quantity = line.split(": ")

    if product in stock:
        stock[product] += int(quantity)
    else:
        stock[product] = int(quantity)

total_products = len(stock.keys())
total_quantity = sum(stock.values())

print(f'Products in stock:')
for product, quantity in stock.items():
    print(f'- {product}: {quantity}')

print(f'Total Products: {total_products}')
print(f'Total Quantity: {total_quantity}')