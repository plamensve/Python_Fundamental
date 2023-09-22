number = int(input())

for i in range(number):
    current_message = int(input())

    if current_message == 88:
        print('Hello')

    if current_message == 86:
        print('How are you?')

    if current_message != 88 and current_message != 86 and current_message < 88:
        print('GREAT!')

    if current_message > 88:
        print('Bye.')
