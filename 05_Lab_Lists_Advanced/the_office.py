def check_employee_happiness():
    happiness_list = list(map(int, input().split()))
    happiness_factor = int(input())

    improved_happiness = [happiness * happiness_factor for happiness in happiness_list]
    average_happiness = sum(improved_happiness) / len(happiness_list)
    happy_count = sum(employee >= average_happiness for employee in improved_happiness)
    total_employee = len(happiness_list)
    message = 'happy' if happy_count >= total_employee / 2 else 'not happy'
    result = f"Score: {happy_count}/{total_employee}. Employees are {message}!"
    return result


check_function = check_employee_happiness()
print(check_function)

