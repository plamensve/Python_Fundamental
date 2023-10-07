def price(product, quantity):
    return {
        'coffee': quantity * 1.50,  # 1.50 price of the coffee
        'coke': quantity * 1.40,  # 1.40 price of the coke
        'water': quantity * 1.00,  # 1.00 price of the water
        'snacks': quantity * 2.00  # 2.00 price of the snacks
    }.get(product)


type_of_product = input()
quantity_of_product = float(input())

total_price = price(type_of_product, quantity_of_product)
print(f'{total_price:.2f}')
