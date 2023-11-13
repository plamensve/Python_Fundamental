text = input()
ind = []
for index in range(len(text)):
    if text[index] == ':':
        first_symbol = text[index]
        second_symbol = text[index + 1]
        add_symbol = first_symbol + second_symbol
        ind.append(add_symbol)

for x in ind:
    print(f"{x}")
