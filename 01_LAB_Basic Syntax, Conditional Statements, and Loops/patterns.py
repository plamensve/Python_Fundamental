number = int(input())
first_row = '*'
second_row = '*'

for a in range(1, number + 1):
    print(first_row * a)

for a in range(number - 1, 0, -1):
    print(second_row * a)