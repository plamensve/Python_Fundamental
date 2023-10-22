price_raitings = [int(num) for num in input().split(", ")]
entry_point = int(input())
type_of_item = input()

if type_of_item == 'cheap':

    left_side = price_raitings[:entry_point]
    right_side = price_raitings[entry_point + 1:]
    entry_number = price_raitings[entry_point]

    left = 0
    for num in left_side:
        if int(num) < int(entry_number):
            left += abs(int(num))

    right = 0
    for num in right_side:
        if int(num) < int(entry_number):
            right += abs(int(num))

    if left >= right:
        print(f"Left - {left}")

    elif right > left:
        print(f"Right - {right}")

elif type_of_item == 'expensive':

    left_side = price_raitings[:entry_point]
    right_side = price_raitings[entry_point + 1:]
    entry_number = price_raitings[entry_point]

    left_s = 0
    for num in left_side:
        if int(num) > int(entry_number):
            left_s += abs(int(num))

    right_s = 0
    for num in right_side:
        if int(num) > int(entry_number):
            right_s += abs(int(num))

    if left_s >= right_s:
        print(f"Left - {left_s}")

    elif right_s > left_s:
        print(f"Right - {right_s}")



