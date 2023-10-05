def calculator(option, num_1, num_2):
    return {
        '1': num_1 + num_2,
        '2': num_1 - num_2,
        '3': num_1 * num_2,
        '4': num_1 / num_2,
        '5': exit()
    }.get(option)


name = input('Please enter your name:\n')
print(f'Menu:\n\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Quit\n')
using_option = (input('Enter your choice (1/2/3/4/5):'))
if using_option < '5':
    number_1 = int(input())
    number_2 = int(input())
    result = calculator(using_option, number_1, number_2)
    print(result)
else:
    print(f'Goodbye!')
    exit()


