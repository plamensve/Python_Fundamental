employee_efficiency_1 = int(input())
employee_efficiency_2 = int(input())
employee_efficiency_3 = int(input())
students_count = int(input())

students_per_hour = employee_efficiency_1 + employee_efficiency_2 + employee_efficiency_3
counter = 0

while students_count > 0:
    counter += 1
    if counter % 4 == 0:
        continue

    students_count -= students_per_hour

print(f"Time needed: {counter}h.")
