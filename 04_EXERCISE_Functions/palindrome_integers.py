def reversed_numbers(parameter):
    true_or_false_list = []
    for num in parameter:
        if num == num[::-1]:
            true_or_false_list.append(True)
        else:
            true_or_false_list.append(False)
    return true_or_false_list


numbers = input().split(', ')
results = reversed_numbers(numbers)

for result in results:
    print(result)
