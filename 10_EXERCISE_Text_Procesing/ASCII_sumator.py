first_line = input()
second_line = input()
random_string = input()

ascii_code_start = ord(first_line)
ascii_code_end = ord(second_line)

ascii_list = []
for char in random_string:
    if ascii_code_start < ord(char) < ascii_code_end:
        ascii_list.append(char)

ascii_sum = 0
for number in ascii_list:
    if number in random_string:
        ascii_sum += ord(number)

print(ascii_sum)
#test