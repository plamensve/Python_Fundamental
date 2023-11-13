text = input()
lst_ords = []

for char in text:
    crypt = ord(char) + 3
    lst_ords.append(crypt)

for x in lst_ords:
    print(f"{chr(x)}", end='')