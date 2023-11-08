string_line = input().split()
result = ''
for word in string_line:
    res = word * len(word)
    result += res

print(result)