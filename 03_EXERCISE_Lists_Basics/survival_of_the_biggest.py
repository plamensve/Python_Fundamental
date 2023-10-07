numbers = input().split(" ")
count_of_numbers_to_remove = int(input())

remove_numbers = []
new_list = []
min_num = 0

for num_for_remove in range(count_of_numbers_to_remove):
    min_num = 0
    remove_numbers = []

    for current_num in numbers:
        remove_numbers.append(int(current_num))
        min_num = min(remove_numbers)

    remove_numbers.remove(int(min_num))
    numbers = remove_numbers

print(*remove_numbers, sep=", ")