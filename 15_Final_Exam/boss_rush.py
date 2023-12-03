import re

number_of_inputs = int(input())

for _ in range(number_of_inputs):
    validation = input()
    pattern = r'\|([A-Z]{4,})\|:#([A-Za-z]+)\s([A-Za-z]+)#'
    match = re.findall(pattern, validation)
    if match:
        for m in match:
            print(f"{m[0]}, The {m[1]} {m[2]}")
            print(f">> Strength: {len(m[0])}")
            print(f">> Armor: {len(m[1]) + len(m[2]) + 1}")
    else:
        print(f"Access denied!")