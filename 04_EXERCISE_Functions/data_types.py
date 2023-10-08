def depending_on_firs_line(parameter_1, parameter_2):
    if parameter_1 == 'int':
        return int(parameter_2) * 2
    elif parameter_1 == 'real':
        return f"{(float(parameter_2) * 1.5):.2f}"
    elif parameter_1 == 'string':
        return f"${parameter_2}$"


initial_string = input()
number = input()
print(depending_on_firs_line(initial_string, number))
