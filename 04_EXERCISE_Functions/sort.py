numbers = input().split()

numbers_list = []
for num in numbers:
    data = numbers_list.append(int(num))

result = sorted(numbers_list, reverse=False)
print(result)
