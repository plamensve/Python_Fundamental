import math
from math import ceil

capacity_of_people = int(input())
number_of_people = int(input())

courses = capacity_of_people / number_of_people
print(math.ceil(courses))