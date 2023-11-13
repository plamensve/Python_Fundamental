def ab_pos(character):  # -> return real alphabetic position (If char is A - return 1 etc)
    position = ord(character)
    real_position_is = position - 64
    return real_position_is


some_string = input().split()
firs_char = ''
last_char = ''
nums = ''
resulting_number = 0
total = []

for word in some_string:
    firs_char = word[0]
    last_char = word[-1]
    char_string = ''
    for char in word:
        if char.isdigit():
            nums += char

# First operation-----------------------------------------
    if firs_char.isupper():
        result = ab_pos(firs_char)
        total_result = int(nums) / result
        resulting_number = total_result

    elif firs_char.islower():
        result = ab_pos(firs_char.upper())
        total_result = int(nums) * result
        resulting_number = total_result

# Second operation ---------------------------------------
    if last_char.islower():
        result = ab_pos(last_char.upper())
        tot = resulting_number + result
        total.append(tot)

    elif last_char.isupper():
        result = ab_pos(last_char)
        tot = resulting_number - result
        total.append(tot)

    nums = ''

total_calculation = 0
for num in total:
    total_calculation += num
print(f"{total_calculation:.2f}")
