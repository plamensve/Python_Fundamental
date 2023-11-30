import re

places = input()

pattern = r'([=|\/])([A-Z][A-Za-z]{2,})\1'

matches = re.findall(pattern, places)

lengths_sum = 0
destinations = []
for match in matches:
    lengths_sum += int(len(match[1]))
    destinations.append(match[1])

print(f"Destinations: {', '.join(destinations)}\nTravel Points: {lengths_sum}")
