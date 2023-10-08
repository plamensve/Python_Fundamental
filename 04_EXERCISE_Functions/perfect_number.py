def perfect_number(number):
    divisor_sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            divisor_sum += divisor
    if some_number == divisor_sum:
        return "We have a perfect number!"
    return "It's not so perfect."


some_number = int(input())
print(perfect_number(some_number))