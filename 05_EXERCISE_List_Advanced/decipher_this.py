secret_message_is = input().split()

left_side = []
right_side = []
final_string = []
for word in secret_message_is:
    for letter in word:
        if letter.isdigit():
            left_side.append(letter)
        else:
            right_side.append(letter)

    left_side_in_chars = "".join(left_side)
    left_side_in_chars_in_integer = int(left_side_in_chars)
    result = chr(left_side_in_chars_in_integer)
    left_side = result

    x = right_side[0]
    y = right_side[-1]
    x, y = y, x
    right_side[0] = x
    right_side[-1] = y

    new_list = [x for n in (left_side, right_side) for x in n]
    result = "".join(new_list)
    final_string.append(result)
    left_side = []
    right_side = []

final_result = " ".join(final_string)
print(final_result)