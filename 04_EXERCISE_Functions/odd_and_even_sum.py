def sum_of_all_even_and_odd(number: str):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in single_number:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)
    return sum_of_odd_digits, sum_of_even_digits


single_number = input()
odd_digit, even_digit = sum_of_all_even_and_odd(single_number)
print(f"Odd sum = {odd_digit}, Even sum = {even_digit}")

