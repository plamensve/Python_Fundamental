numbers = input().split()

numbers_list = []
for num in numbers:
    data = numbers_list.append(int(num))

is_even = lambda x: x % 2 == 0
result = filter(is_even, numbers_list)
print(list(result))
