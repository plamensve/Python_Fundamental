import re

phone_numbers = input()
regex = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'

match = re.findall(regex, phone_numbers)

# for number in match:
#     print(number, end=' ')

print(f"{', '.join(match)}")