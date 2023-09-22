command = input()

while command != 'End':
    if command != 'SoftUni':
        new_string = ''

        for char in command:
            new_string += char * 2

        print(new_string)

    command = input()
