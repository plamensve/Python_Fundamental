fist_symbol = int(input())
last_symbol = int(input())

for character in range(fist_symbol, last_symbol + 1):
    current_symbol = character
    print(f'{chr(character)}', end=' ')