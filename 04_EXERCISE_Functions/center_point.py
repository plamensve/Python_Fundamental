import math
from math import floor


def coordinate_system(number_1, number_2, number_3, number_4):
    x1y1 = (number_1 ** 2) + (number_2 ** 2)
    x1y1_distance = math.sqrt(x1y1)
    x2y2 = (number_3 ** 2) + (number_4 ** 2)
    x2y2_distance = math.sqrt(x2y2)

    if x1y1 <= x2y2:
        return f"({int(number_1)}, {int(number_2)})"
    return f"({int(number_3)}, {int(number_4)})"


num_x1 = math.floor(float(input()))
num_y1 = math.floor(float(input()))
num_x2 = math.floor(float(input()))
num_y2 = math.floor(float(input()))

print(coordinate_system(num_x1, num_y1, num_x2, num_y2))
