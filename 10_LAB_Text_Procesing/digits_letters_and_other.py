single_string = input()
number = ''
alpha = ''
symbol = ''

for char in single_string:
    if char.isdigit():
        number += char
    elif char.isalpha():
        alpha += char
    else:
        symbol += char

print(number)
print(alpha)
print(symbol)
