import math
from math import floor


def coordinate_system(number_1, number_2, number_3, number_4, number_5, number_6, number_7, number_8):
    x1y1 = abs(number_1) + abs(number_2)
    x2y2 = abs(number_3) + abs(number_4)
    x3y3 = abs(number_5) + abs(number_6)
    x4y4 = abs(number_7) + abs(number_8)
    longer_line = sorted([x1y1, x2y2, x3y3, x4y4], reverse=True)

    first_line = []
    for num in longer_line:
        if x1y1 == num:
            first_line.append(number_1)
            first_line.append(number_2)
        elif x2y2 == num:
            first_line.append(number_3)
            first_line.append(number_4)
        elif x3y3 == num:
            first_line.append(number_5)
            first_line.append(number_6)
        elif x4y4 == num:
            first_line.append(number_7)
            first_line.append(number_8)
    return f"{(first_line[2], first_line[3])}{(first_line[0], first_line[1])}"


num_x1 = math.floor(float(input()))
num_y1 = math.floor(float(input()))
num_x2 = math.floor(float(input()))
num_y2 = math.floor(float(input()))
num_x3 = math.floor(float(input()))
num_y3 = math.floor(float(input()))
num_x4 = math.floor(float(input()))
num_y4 = math.floor(float(input()))
print(coordinate_system(num_x1, num_y1, num_x2, num_y2, num_x3, num_y3, num_x4, num_y4))
#test