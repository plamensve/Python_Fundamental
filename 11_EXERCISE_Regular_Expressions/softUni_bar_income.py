import re

string_line = input()
dict_name_product_quantity_price = {}
total_income = 0
while string_line != 'end of shift':
    regex_name = r'%([A-Z][a-z]+)%'
    regex_product = r'<([A-Za-z]+)>'
    regex_quantity = r'\|(\d+)\|'
    regex_price = r'(?:<[^>]+>\|)?([\d.]+)\$'

    matches_name = re.findall(regex_name, string_line)
    matches_product = re.findall(regex_product, string_line)
    matches_quantity = re.findall(regex_quantity, string_line)
    matches_price = re.findall(regex_price, string_line)

    for name in matches_name:
        for product in matches_product:
            for quantity in matches_quantity:
                for price in matches_price:
                    total_income += float(quantity) * float(price)
                    print(f'{name}: {product} - {float(quantity) * float(price):.2f}')

    string_line = input()
print(f'Total income: {total_income:.2f}')


