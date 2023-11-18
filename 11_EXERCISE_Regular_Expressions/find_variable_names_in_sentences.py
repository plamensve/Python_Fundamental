import re
string_line = input()
regex = r'\b_([a-zA-Z0-9]+)\b'

matches = re.findall(regex, string_line)
print(','.join(matches))
