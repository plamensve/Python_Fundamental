user_guess = input().split(', ')
check_1 = False
check_2 = False
check_3 = False

username = []
for user in user_guess:
    if 3 <= len(user) <= 16:
        check_1 = True
    else:
        continue

    for char in user:
        if char.isalpha() or char.isdigit() or char == "-" or char == "_":
            check_2 = True
        else:
            check_2 = False

    for char in user:
        if not (char.isalpha() or char.isdigit() or char == "-" or char == "_"):
            check_3 = False
            break
        else:
            check_3 = True

    if check_1 and check_2 and check_3:
        username.append(user)

for item in username:
    print(item)
