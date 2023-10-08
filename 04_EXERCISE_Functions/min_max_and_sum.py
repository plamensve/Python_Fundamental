def min_max_sum(parameter):
    list_with_numbers = []
    for num in parameter:
        data = list_with_numbers.append(int(num))

    return min(list_with_numbers), max(list_with_numbers), sum(list_with_numbers)


number = input().split()
min_num, max_num, sum_num = min_max_sum(number)
print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {sum_num}")

