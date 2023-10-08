# numbers = input().split()
#
# numbers_list = []
# for num in numbers:
#     data = numbers_list.append(int(num))
#
# is_even = lambda x: x % 2 == 0
# result = filter(is_even, numbers_list)
# print(list(result))

def is_even(num):
    if num % 2 == 0:
        return True
    return False


numbers = input().split()
numbers_list = []
for num in numbers:
    data = numbers_list.append(int(num))

result = []
for element in numbers_list:
    if is_even(element):
        result.append(element)

print(result)