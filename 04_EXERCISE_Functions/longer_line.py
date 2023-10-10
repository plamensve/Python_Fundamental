import math
from math import floor


def coordinate_system(number_1, number_2, number_3, number_4, number_5, number_6, number_7, number_8):
    x1y1 = abs(number_1) + abs(number_2)
    x2y2 = abs(number_3) + abs(number_4)
    x3y3 = abs(number_5) + abs(number_6)
    x4y4 = abs(number_7) + abs(number_8)
    longer_line = sorted([x1y1, x2y2, x3y3, x4y4], reverse=True)
    for i in longer_line:
        if longer_line.count(i) > 1:
            longer_line.remove(i)

    first_list = []
    for j in longer_line[:2]:
        if j == x1y1:
            x1_y1 = (number_1, number_2)
            first_list.append(x1_y1)
        elif j == x2y2:
            x2_y2 = (number_3, number_4)
            first_list.append(x2_y2)
        elif j == x3y3:
            x3_y3 = (number_5, number_6)
            first_list.append(x3_y3)
        elif j == x4y4:
            x4_y4 = (number_7, number_8)
            first_list.append(x4_y4)

    first_list = sorted(first_list, key=lambda x: sum(map(abs, x)))
    return first_list


num_x1 = math.floor(float(input()))
num_y1 = math.floor(float(input()))
num_x2 = math.floor(float(input()))
num_y2 = math.floor(float(input()))
num_x3 = math.floor(float(input()))
num_y3 = math.floor(float(input()))
num_x4 = math.floor(float(input()))
num_y4 = math.floor(float(input()))
result = (coordinate_system(num_x1, num_y1, num_x2, num_y2, num_x3, num_y3, num_x4, num_y4))
formatted_result = ''.join([f"({x}, {y})" for x, y in result])
print(formatted_result)
