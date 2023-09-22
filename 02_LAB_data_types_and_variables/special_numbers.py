number = int(input())
new_string = ''
sum_of_string = 0

for i in range(1, number + 1):
    new_string = str(i)

    for char in new_string:
        sum_of_string += int(char)
        continue

    if sum_of_string == 5 or sum_of_string == 7 or sum_of_string == 11:
        print(f'{new_string} -> True')
    else:
        print(f'{new_string} -> False')

    sum_of_string = 0













