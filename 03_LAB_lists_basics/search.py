lines = int(input())
magic_word = input()

my_list = []

for _ in range(lines):
    data = input()
    my_list.append(data)

print(my_list)

filtered_strings = []

for current_string in my_list:
    if magic_word in current_string:
        filtered_strings.append(current_string)

print(filtered_strings)
