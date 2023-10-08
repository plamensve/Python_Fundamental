def check_password(parameter):
    pass_len = False
    pass_digit = False
    symbol_consist = False

    # Check for the length of the password
    if 6 <= len(parameter) <= 10:
        pass_len = True

    # Checking for how many symbols are consist
    symbol = 0
    for char in parameter:
        if not char.isalnum():
            symbol += 1
            symbol_consist = True

    # Checking for how many digits are consist
    digit_counter = 0
    for char in parameter:
        if char.isdigit():
            digit_counter += 1

    if digit_counter >= 2:
        pass_digit = True

    if pass_len and pass_digit and not symbol_consist:
        return "Password is valid"
    else:
        error_messages = []

        if not pass_len:
            error_messages.append("Password must be between 6 and 10 characters")

        if symbol_consist:
            error_messages.append("Password must consist only of letters and digits")

        if not pass_digit:
            error_messages.append("Password must have at least 2 digits")

        return "\n".join(error_messages)


password = input()
result = check_password(password)
print(result)
