import math


def cartesian_distance_center(x, y):
    # Calculate the distance from a given point to the center of the coordinate system
    distance_to_center = math.sqrt(x ** 2 + y ** 2)
    return distance_to_center


def print_longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    distance1 = cartesian_distance_center(x1, y1)
    distance2 = cartesian_distance_center(x2, y2)
    distance3 = cartesian_distance_center(x3, y3)
    distance4 = cartesian_distance_center(x4, y4)

    line1_length = distance1 + distance2
    line2_length = distance3 + distance4

    if line1_length >= line2_length:
        if distance1 <= distance2:
            print(f'({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})')
        else:
            print(f'({int(x2)}, {int(y2)})({int(x1)}, {int(y1)})')
    else:
        if distance3 <= distance4:
            print(f'({int(x3)}, {int(y3)})({int(x4)}, {int(y4)})')
        else:
            print(f'({int(x4)}, {int(y4)})({int(x3)}, {int(y3)})')


x1 = math.floor(float(input()))
y1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y2 = math.floor(float(input()))
x3 = math.floor(float(input()))
y3 = math.floor(float(input()))
x4 = math.floor(float(input()))
y4 = math.floor(float(input()))

distance1 = cartesian_distance_center(x1, y1)
distance2 = cartesian_distance_center(x2, y2)
distance3 = cartesian_distance_center(x3, y3)
distance4 = cartesian_distance_center(x4, y4)

line1_length = distance1 + distance2
line2_length = distance3 + distance4

print_longer_line(x1, y1, x2, y2, x3, y3, x4, y4)