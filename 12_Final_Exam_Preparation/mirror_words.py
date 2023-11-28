import re
command = input()
list_matches = []
new_list_matches = []
pattern = r"([@#])([A-Za-z]{3,})(\1)(\1)([A-Za-z]{3,})(\1)"
matches = re.findall(pattern, command)

for match in matches:
    list_matches.append(match[1])
    list_matches.append(match[4])

if len(list_matches) != 0:
    print(f"{int((len(list_matches))/2)} word pairs found!")
else:
    print(f"No word pairs found!")

for i in range(1, len(list_matches), 2):
    if (list_matches[i][::-1]) == (list_matches[i-1]) and (list_matches[i-1][::-1]) == (list_matches[i]):
        new_list_matches.append(list_matches[i-1]+" <=> " + list_matches[i])

if len(new_list_matches) > 0:
    print("The mirror words are:")
    print(', '.join(new_list_matches))
else:
    print("No mirror words!")


