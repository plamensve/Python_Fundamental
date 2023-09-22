budget = int(input())
command = input()

while command != 'End':
    current_product_price = int(command)
    budget -= current_product_price

    if budget < 0:
        print('You went in overdraft!')
        break

    command = input()

if command == 'End':
    print(f'You bought everything needed.')




