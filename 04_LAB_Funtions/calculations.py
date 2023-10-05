def calculator(action, num_a, num_b):
    """
    Calculate - multiply, divide, add, subtract { '*', '/', '+', '-' }
    """
    return {
        'multiply': num_a * num_b,
        'divide': int(num_a / num_b),
        'add': num_a + num_b,
        'subtract': num_a - num_b
    }.get(action)
    # if action == 'multiply':
    #     return num_a * num_b
    # elif action == 'divide':
    #     return num_a / num_b
    # elif action == 'add':
    #     return num_a + num_b
    # elif action == 'subtract':
    #     return num_a - num_b


operator = input()
first_number = int(input())
second_number = int(input())

result = calculator(operator, first_number, second_number)
print(int(result))
