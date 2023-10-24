numbers = [1, 2, 3, 4]
x_nums = [2, 6, 2, 2]
cows = 0
bulls = 0

if x_nums[0] == numbers[0]:
    bulls += 1
elif x_nums[0] != numbers[0] and x_nums[0] in numbers:
    cows += 1

if x_nums[1] == numbers[1]:
    bulls += 1
elif x_nums[1] != numbers[1] and x_nums[1] in numbers:
    cows += 1

if x_nums[2] == numbers[2]:
    bulls += 1
elif x_nums[2] != numbers[2] and x_nums[2] in numbers:
    cows += 1

if x_nums[3] == numbers[3]:
    bulls += 1
elif x_nums[3] != numbers[3] and x_nums[3] in numbers:
    cows += 1

print(f"Cows: {cows}")
print(f"Bulls: {bulls}")