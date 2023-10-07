char_1 = input()
char_2 = input()

single_string = []
for char in range(ord(char_1) + 1, ord(char_2)):
    single_string.append(chr(char))

print(single_string)