lines = int(input())
my_list = []

for _ in range(lines):
    current_num = int(input())
    my_list.append(current_num)

command = input()

filtered_string = []

if command == 'even':
    for current_num in my_list:
        if current_num % 2 == 0 or current_num == 0:
            filtered_string.append(current_num)

elif command == 'odd':
    for current_num in my_list:
        if current_num % 2 != 0:
            filtered_string.append(current_num)

elif command == 'negative':
    for current_num in my_list:
        if current_num < 0:
            filtered_string.append(current_num)

elif command == 'positive':
    for current_num in my_list:
        if current_num >= 0:
            filtered_string.append(current_num)

print(filtered_string)