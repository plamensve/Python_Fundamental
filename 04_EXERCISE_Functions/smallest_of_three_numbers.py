def smallest_number(numbers: list): # -> int
    return min(numbers)


n_1 = int(input())
n_2 = int(input())
n_3 = int(input())

result = smallest_number([n_1, n_2, n_3])
print(result)