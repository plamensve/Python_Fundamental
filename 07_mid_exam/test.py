price_ratings = [int(num) for num in input().split(", ")]
entry_point = int(input())
type_of_item = input()

left_side = price_ratings[:entry_point]
right_side = price_ratings[entry_point + 1:]
entry_number = price_ratings[entry_point]

left = 0
right = 0

for num in left_side:
    if type_of_item == 'cheap' and num < entry_number:
        left += num
    elif type_of_item == 'expensive' and num > entry_number:
        left += num

for num in right_side:
    if type_of_item == 'cheap' and num < entry_number:
        right += num
    elif type_of_item == 'expensive' and num > entry_number:
        right += num

if left >= right:
    print(f"Left - {left}")
elif right > left:
    print(f"Right - {right}")

