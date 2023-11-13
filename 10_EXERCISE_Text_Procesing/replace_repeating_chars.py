symbols = input()
string_symbols = ''
last_added_symbol = ''

for symbol in symbols:
    if symbol != last_added_symbol:
        string_symbols += symbol
        last_added_symbol = symbol

print(string_symbols)