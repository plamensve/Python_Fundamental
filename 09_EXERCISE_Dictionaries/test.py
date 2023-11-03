phonebook = {}

while True:
    contact = input()
    if '-' not in contact:
        break
    else:
        result = contact.split('-')
        key = result[0]
        value = result[1]
        phonebook[key] = value

name = input()

# Проверете дали името съществува в телефонния указател
if name in phonebook:
    print(f'{name} -> {phonebook[name]}')
else:
    print(f"Contact {name} does not exist.")

name = input()