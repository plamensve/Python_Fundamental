import re

regex = r'\b(w{3}\.([A-Za-z0-9\-\.]+)\.([a-z]+))\b'
string_line = input()
while string_line:
    matches = re.findall(regex, string_line)
    for match in matches:
        print(match[0])
    string_line = input()



