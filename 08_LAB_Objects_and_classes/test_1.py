# numbers = [int(num) for num in input(f"Computer numbers: ").split()]
# x_nums = [int(x) for x in input(f"Your suggestion: ").split()]

numbers = [1, 2, 3, 4]
x_nums = [1, 1, 1, 1]
cows = 0
bulls = 0
for i in x_nums:
    if i in numbers:
        if x_nums.index(i) == numbers.index(i):
            bulls += 1
        if x_nums.index(i) != numbers.index(i) and i in numbers:
            cows += 1

print(f"Cows: {cows}")
print(f"Bulls: {bulls}")