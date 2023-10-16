sequence_of_integers = [int(number) for number in input().split()]
other_items = []
popped_indexes = []
result = 0

while len(sequence_of_integers) >= 1:
    index = int(input())
    length = len(sequence_of_integers) - 1

    if 0 <= index < len(sequence_of_integers):
        popped_value = sequence_of_integers.pop(index)
        popped_indexes.append(popped_value)
        sequence_of_integers = [x + popped_value if x <= popped_value else x - popped_value for x in
                                sequence_of_integers]

    elif index < 0:
        num_to_add = sequence_of_integers[-1]
        num = sequence_of_integers[0]
        popped_indexes.append(num)
        sequence_of_integers[0] = sequence_of_integers[-1]

    else:
        num_to_add = sequence_of_integers[0]
        num = sequence_of_integers[-1]
        sequence_of_integers[-1] = sequence_of_integers[0]
        popped_indexes.append(num)
        sequence_of_integers = [x + sequence_of_integers[-1] for x in sequence_of_integers]

new_list = sequence_of_integers + popped_indexes
for num in new_list:
    result += num
print(result)
