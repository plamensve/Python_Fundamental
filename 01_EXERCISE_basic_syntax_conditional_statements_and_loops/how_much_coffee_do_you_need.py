command = input()
coffee_counter = 0

while command != 'END':
    if command.lower() == 'coding' \
            or command.lower() == 'dog' \
            or command.lower() == 'cat' \
            or command.lower() == 'movie':

        if command.isupper():
            coffee_counter += 2

        elif command.islower():
            coffee_counter += 1

    if coffee_counter > 5:
        print('You need extra sleep')
        break

    command = input()

if command == 'END':
    print(coffee_counter)
