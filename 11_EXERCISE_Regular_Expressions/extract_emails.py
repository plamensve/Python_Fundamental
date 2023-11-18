import re
string_line = input()

regex = r'(\s([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z0-9\-]+)(\.[a-z]+)+)'
matches = re.findall(regex, string_line)
for match in matches:
    print(match[0])


