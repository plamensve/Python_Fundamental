import re

count_of_barcodes = int(input())
for _ in range(count_of_barcodes):
    current_barcode = input()
    pattern = r'([@]{1}[#]{1,})([A-Z][A-Za-z0-9]{4,}[A-Z])([@]{1}[#]{1,})'
    match = re.findall(pattern, current_barcode)

    if match:
        barcode_group = ''
        for char in current_barcode:
            if char.isdigit():
                barcode_group += char
        if len(barcode_group) > 0:
            print(f'Product group: {barcode_group}')
        else:
            print(f'Product group: 00')
    else:
        print(f'Invalid barcode')