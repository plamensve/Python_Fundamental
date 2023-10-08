def factorial(number):
    result = 1
    for num in range(1, number + 1):
        result *= num
    return result


first_number = int(input())
second_number = int(input())

divided = factorial(first_number) // factorial(second_number)
print(f"{divided:.2f}")
