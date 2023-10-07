numbers = input().split(' ')
some_string = input()

sum_numbers = []
counter = 0
total_sum = []
for number in numbers:
    sum_numbers.append(number)
    for i in range(len(number)):
        current_num = int(number[i])
        counter += current_num
    total_sum.append(counter)
    counter = 0

string_list = list(some_string)
length_of_string = len(some_string)
result_list = []

for num in total_sum:
    if num > length_of_string:
        result = num - length_of_string
        result_list.append(result)
    else:
        result = num
        result_list.append(result)

result_word_list = []
for index in result_list:
    popped_item = string_list.pop(index)
    result_word_list.append(popped_item)

print(''.join(result_word_list))

# # Четене на входните данни
# numbers = input().split(' ')
# some_string = input()
#
# message = []
#
# for number in numbers:
#     index = sum(int(digit) for digit in number)  # Изчисляваме сумата на цифрите на числото
#     index %= len(some_string)  # Взимаме остатъка при деление, за да се гарантира валиден индекс
#     char = some_string[index]  # Взимаме символа от индекса
#     message.append(char)  # Добавяме символа към съобщението
#     some_string = some_string[:index] + some_string[index + 1:]  # Премахваме символа от текста
#
# # Принтираме финалното съобщение
# print(''.join(message))
