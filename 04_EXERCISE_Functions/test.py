number = int(input())

divisor_sum = 0
for divisor in range(1, number):
    if number % divisor == 0:
        divisor_sum += divisor
