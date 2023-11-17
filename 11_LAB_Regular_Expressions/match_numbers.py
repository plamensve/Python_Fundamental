import re

numbers_info = input()
regex = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'

matches = re.finditer(regex, numbers_info)
for match in matches:
    print(match.group(), end=' ')
