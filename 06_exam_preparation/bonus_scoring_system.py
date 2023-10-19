from math import ceil

number_of_students = int(input())
number_of_the_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_lectures = 0

for student in range(1, number_of_students + 1):
    attendances = int(input())
    total_bonus = attendances / number_of_the_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
    if attendances > max_lectures:
        max_lectures = attendances

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_lectures} lectures.")