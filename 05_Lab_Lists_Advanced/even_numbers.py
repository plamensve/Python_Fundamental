# numbers = input().split(', ')
# even_list = []
# for num in numbers:
#     if int(num) % 2 == 0:
#         even_list.append(num)
#
# index_list = []
# for num in even_list:
#     for number in numbers:
#         if num == number:
#             result = numbers.index(number)
#             index_list.append(result)
#
# print(index_list)


numbers = input().split(',')
even_list = [int(num) for num in numbers if int(num) % 2 == 0]
index_list = [index for index, num in enumerate(numbers) if int(num) in even_list]
print(index_list)
