stock_product = input().split()

stock = {}

for i in range(0, len(stock_product), 2):
    product = stock_product[i]
    quantity = int(stock_product[i + 1])
    stock[product] = quantity

product_to_search = input().split()

for product in product_to_search:
    if product in stock_product:
        print(f'We have {stock[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")