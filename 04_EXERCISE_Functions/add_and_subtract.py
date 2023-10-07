def add_and_subtract(first, second, third):
    returned_result = sum_numbers(first, second)
    final_result = subtract(returned_result, number_3)
    return final_result


def sum_numbers(first, second):
    return first + second


def subtract(result, third):
    return result - third


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(add_and_subtract(number_1, number_2, number_3))


# def add_and_subtract(num_1, num_2, num_3):
#     return sum_numbers
#
#
# def sum_numbers(first_one, first_two):
#     return first_one + first_two
#
#
# def subtract(parameter_1, parameter_2):
#     return parameter_1 - parameter_2
#
#
# number_1 = int(input())
# number_2 = int(input())
# number_3 = int(input())
#
# first_two_integers = sum_numbers(number_1, number_2)
# subtract_func = subtract(first_two_integers, number_3)
# print(subtract_func)
