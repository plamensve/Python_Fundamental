stock_data = input().split()

stock = {}

for i in range(0, len(stock_data), 2):
    product = stock_data[i]
    quantity = int(stock_data[i + 1])
    stock[product] = quantity

print(stock)
