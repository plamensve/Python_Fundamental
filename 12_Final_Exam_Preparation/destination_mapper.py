import re
string_line = input()
patter = r"(=|/)([A-Z][A-Za-z]{2,})\1"

matches = re.findall(patter, string_line)
counter = 0
destinations = []
for match in matches:
    counter += int(len(match[1]))
    destinations.append(match[1])

if len(destinations) > 0:
    print(f'Destinations: {", ".join(destinations)}')
    print(f'Travel Points: {counter}')
else:
    print(f'Destinations:')
    print(f'Travel Points: {counter}')