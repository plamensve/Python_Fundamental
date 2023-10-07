numbers = input().split(' ')

opposite_numbers = []
for num in numbers:
    current_num = int(num) * -1
    opposite_numbers.append(current_num)

print(opposite_numbers, sep=", ")


