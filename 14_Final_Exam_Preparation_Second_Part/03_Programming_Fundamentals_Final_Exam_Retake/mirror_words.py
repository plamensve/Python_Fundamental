import re

text_string = input()

pattern = r'(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
matches = re.findall(pattern, text_string)

if len(matches) == 0:
    print(f"No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

match_dict = {}
for match in matches:
    match_dict[match[1]] = match[2]

final_list = []
for k, v in match_dict.items():
    if k[::-1] == v:
        final_list.append(f"{k} <=> {v}")

if len(final_list) > 0:
    print('The mirror words are:')
    print(', '.join(final_list))
else:
    print(f"No mirror words!")