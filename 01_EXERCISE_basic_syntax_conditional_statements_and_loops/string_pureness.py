string_lines = int(input())

for _ in range(string_lines):
    command = input()
    check_pureness = 0

    for char in command:
        if char == ',' or char == '.' or char == '_':
            check_pureness += 1
            break

    if check_pureness > 0:
        print(f"{command} is not pure!")
    else:
        print(f"{command} is pure.")
