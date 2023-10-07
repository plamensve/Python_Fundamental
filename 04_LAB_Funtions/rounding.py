def rounded_numbers(parameter: list):
    return [round(float(num)) for num in parameter]


numbers = input().split()
my_list = rounded_numbers(numbers)
print(my_list)
