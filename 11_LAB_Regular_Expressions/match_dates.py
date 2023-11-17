import re

regex = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'
date_info = input()


matches = re.findall(regex, date_info)

for match in matches:
    day, month, year = match[0], match[2], match[3]
    print(f'Day: {day}, Month: {month}, Year: {year}')
