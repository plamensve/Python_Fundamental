import math
from math import floor

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())


x1y1 = (num_1, num_2)
x2y2 = (num_3, num_4)
x1y1_x2y2_distance = ((num_3 - num_1) ** 2) + ((num_4 - num_2) ** 2)
distance_1 = math.sqrt(x1y1_x2y2_distance)
print(distance_1)