def positive(parameter):
    positive_list = []
    for number in parameter:
        if int(number) >= 0:
            positive_list.append(int(number))
    return positive_list


def negative(parameter):
    negative_list = []
    for number in parameter:
        if int(number) < 0:
            negative_list.append(int(number))
    return negative_list


def even(parameter):
    even_list = []
    for number in parameter:
        if int(number) % 2 == 0:
            even_list.append(int(number))
    return even_list


def odd(parameter):
    odd_list = []
    for number in parameter:
        if int(number) % 2 != 0:
            odd_list.append(int(number))
    return odd_list


string_text = input().split(", ")
positive_str = ', '.join(map(str, positive(string_text)))
negative_str = ', '.join(map(str, negative(string_text)))
even_str = ', '.join(map(str, even(string_text)))
odd_str = ', '.join(map(str, odd(string_text)))

print(f"Positive: {positive_str}")
print(f"Negative: {negative_str}")
print(f"Even: {even_str}")
print(f"Odd: {odd_str}")

