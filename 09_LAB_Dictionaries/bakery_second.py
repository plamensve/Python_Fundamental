line = input().split()
stocks = {}

for i in range(0, len(line), 2):
    product = line[i]
    quantity = line[i + 1]
    stocks[product] = int(quantity)
print(stocks)
