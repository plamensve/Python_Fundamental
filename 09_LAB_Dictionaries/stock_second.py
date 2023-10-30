line = input().split()
stocks = {}

for i in range(0, len(line), 2):
    product = line[i]
    quantity = line[i + 1]
    stocks[product] = int(quantity)

searched_product = input().split()

for product in searched_product:
    if product in stocks:
        print(f"We have {stocks[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")