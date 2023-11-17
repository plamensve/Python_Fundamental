import re

names = input()

regex = f'\\b[A-Z][a-z]+ [A-Z][a-z]+\\b'

match = re.findall(regex, names)

for name in match:
    print(f"{''.join(name)}", end=' ')