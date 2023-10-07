list_with_numbers = input().split()
opposite_numbers = []

for num in list_with_numbers:
    current_number = -int(num)
    opposite_numbers.append(current_number)

print(opposite_numbers)
