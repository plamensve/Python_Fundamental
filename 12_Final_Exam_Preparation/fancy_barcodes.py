import re

number_line = int(input())
for _ in range(number_line):
    barcode = input()
    pattern = '@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'
    match = re.fullmatch(pattern, barcode)

    if match:
        barcode_group = ''
        for char in barcode:
            if char.isdigit():
                barcode_group += char
        if len(barcode_group) > 0:
            print(f'Product group: {barcode_group}')
        else:
            print(f'Product group: 00')
    else:
        print(f'Invalid barcode')