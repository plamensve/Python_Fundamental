import re
input_string = input()
digits = []

while input_string:

    regex = r'\d+'
    matches = re.findall(regex, input_string)
    digits.append(matches)

    input_string = input()

for index in digits:
    for digit in index:
        print(digit, end=' ')