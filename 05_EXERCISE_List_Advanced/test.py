sequence_of_integers = [int(number) for number in input().split()]
popped_indexes = []
result = 0

while sequence_of_integers:
    popped_index_number = int(input())

    if popped_index_number < 0:
        popped_value = sequence_of_integers.pop(0)
        popped_indexes.append(popped_value)
        sequence_of_integers = [x + popped_value for x in sequence_of_integers]

    elif popped_index_number >= len(sequence_of_integers):
        popped_value = sequence_of_integers.pop()
        popped_indexes.append(popped_value)
        sequence_of_integers = [x + popped_value for x in sequence_of_integers]

    else:
        popped_value = sequence_of_integers.pop(popped_index_number)
        popped_indexes.append(popped_value)
        sequence_of_integers = [x + popped_value if x <= popped_value else x - popped_value for x in sequence_of_integers]

new_list = sequence_of_integers + popped_indexes
for num in new_list:
    result += num
print(result)

