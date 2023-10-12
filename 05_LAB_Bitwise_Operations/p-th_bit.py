def decimal_to_binary(parameter):
    binary_list = []
    number = parameter
    while number > 0:
        result = number % 2
        binary_list.append(int(result))
        number = number // 2

    binary_list.reverse()
    return binary_list


decimal_binary = int(input())
binary_digits = decimal_to_binary(decimal_binary)
count_zero = binary_digits.count(0)
binary_str = ''.join(map(str, binary_digits))

print(f"Binary number: {binary_str}")
print(f"Zero count: {count_zero}")

bit_position = int(input())
position_in_string = -bit_position-1

try:
    bit_on_position_one = binary_digits[position_in_string]
    print(f"Bit on position 1 is: {bit_on_position_one}")
except IndexError:
    print("Bit on position 1 is: 0")
