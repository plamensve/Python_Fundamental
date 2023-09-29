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

# n = int(input())
# COMMAND_EVEN = 'even'
# COMMAND_ODD = 'odd'
# COMMAND_NEGATIVE = 'negative'
# COMMAND_POSITIVE = 'positive'
#
# numbers = [int(input()) for _ in range(n)]
# filtered_numbers = []
#
# command = input()
#
# for num in numbers:
#     filtered_command = ((command == COMMAND_EVEN and num % 2 == 0) or
#                         (command == COMMAND_ODD and num % 2 != 0) or
#                         (command == COMMAND_POSITIVE and num >= 0) or
#                         (command == COMMAND_NEGATIVE and num < 0)
#     )
#
#     if filtered_command:
#         filtered_numbers.append(num)
#
# print(filtered_numbers)
