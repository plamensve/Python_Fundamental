def calculator(action, num_a, num_b):
    if action == 'multiply':
        return num_a * num_b
    elif action == 'divide':
        return num_a / num_b
    elif action == 'add':
        return num_a + num_b
    elif action == 'subtract':
        return num_a - num_b


operator = input()
first_number = int(input())
second_number = int(input())

result = calculator(operator, first_number, second_number)
print(int(result))
