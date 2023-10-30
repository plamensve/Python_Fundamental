line = input()
stocks = {}
while True:
    if line == 'statistics':
        break

    product, quantity = line.split(': ')
    if product in stocks:
        stocks[product] += int(quantity)
    else:
        stocks[product] = int(quantity)

    line = input()
total_products = len(stocks)
total_quantity = 0

print(f'Products in stock:')
for product in stocks:
    print(f"- {product}: {stocks[product]}")
    total_quantity += stocks[product]

print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")


# Second solution ------------------------------------------------------

# stock = {}
# while True:
#     line = input()
#     if line == 'statistics':
#         break
#
#     product, quantity = line.split(": ")
#
#     if product in stock:
#         stock[product] += int(quantity)
#     else:
#         stock[product] = int(quantity)
#
# total_products = len(stock.keys())
# total_quantity = sum(stock.values())
#
# print(f'Products in stock:')
# for product, quantity in stock.items():
#     print(f'- {product}: {quantity}')
#
# print(f'Total Products: {total_products}')
# print(f'Total Quantity: {total_quantity}')