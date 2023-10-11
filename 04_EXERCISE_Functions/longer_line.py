import math
from math import floor


def coordinate_system(number_1, number_2, number_3, number_4):
    x1y1 = (number_1 ** 2) + (number_2 ** 2)
    x1y1_distance = math.sqrt(x1y1)
    x2y2 = (number_3 ** 2) + (number_4 ** 2)
    x2y2_distance = math.sqrt(x2y2)

    if x1y1 == x2y2:
        return f"{(number_1, number_2)}"
    if x1y1 < x2y2:
        return f"{(number_1, number_2)}{(number_3, number_4)}"
    return f"{(number_3, number_4)}{(number_1, number_2)}"


def distance_calculate(number_1, number_2, number_3, number_4, number_5, number_6, number_7, number_8):
    x1y1 = (number_1, number_2)
    x2y2 = (number_3, number_4)
    x1y1_x2y2_distance = ((number_3 - number_1) ** 2) + ((number_4 - number_2) ** 2)
    distance_1 = math.sqrt(x1y1_x2y2_distance)  # Distance between two points

    x3y3 = (number_5, number_6)
    x4y4 = (number_7, number_8)
    x3y3_x4y4_distance = ((number_7 - number_5) ** 2) + ((number_8 - number_6) ** 2)
    distance_2 = math.sqrt(x3y3_x4y4_distance)  # Distance between two points

    if distance_1 > distance_2:
        n1, n2, n3, n4, n5, n6, n7, n8 = number_1, number_2, number_3, number_4, number_5, number_6, number_7, number_8
        return coordinate_system(n1, n2, n3, n4)
    else:
        n1, n2, n3, n4, n5, n6, n7, n8 = number_1, number_2, number_3, number_4, number_5, number_6, number_7, number_8
        return coordinate_system(n5, n6, n7, n8)


num_x1 = math.floor(float(input()))
num_y1 = math.floor(float(input()))
num_x2 = math.floor(float(input()))
num_y2 = math.ceil(float(input()))

num_x3 = math.floor(float(input()))
num_y3 = math.floor(float(input()))
num_x4 = math.floor(float(input()))
num_y4 = math.floor(float(input()))
print(distance_calculate(num_x1, num_y1, num_x2, num_y2, num_x3, num_y3, num_x4, num_y4))
