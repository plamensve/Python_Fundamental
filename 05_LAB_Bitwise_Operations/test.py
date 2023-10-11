number = int(input())
binary_list = []

while number > 0:
    result = number % 2
    binary_list.append(int(result))
    number = number // 2

binary_list.reverse()
print(*binary_list)
