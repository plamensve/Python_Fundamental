command = input()
price_without_taxes = 0

while command != 'special' and command != 'regular':
    try:
        if float(command) < 0:
            print(f"Invalid price!")
        else:
            price = float(command)
            price_without_taxes += price
    except ValueError:
        print(f"Invalid order!")

    command = input()

taxes = price_without_taxes * 0.2
total_price = price_without_taxes + taxes
discount = total_price * 0.1
total_price_with_discount = total_price - discount

if command == 'special':
    if price_without_taxes == 0:
        print(f"Invalid order!")
    else:
        print(f"Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {price_without_taxes:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print(f"-----------")
        print(f"Total price: {total_price_with_discount:.2f}$")

elif command == 'regular':
    if price_without_taxes == 0:
        print(f"Invalid order!")
    else:
        print(f"Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {price_without_taxes:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print(f"-----------")
        print(f"Total price: {total_price:.2f}$")

