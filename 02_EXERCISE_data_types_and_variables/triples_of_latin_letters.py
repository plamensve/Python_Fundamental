number_of_lines = int(input())

for first_symbol in range(number_of_lines):
    for second_symbol in range(number_of_lines):
        for third_symbol in range(number_of_lines):
            print(f"{chr(97 + first_symbol)}{chr(97 + second_symbol)}{chr(97 + third_symbol)}")

