def ab_pos(character):
    position = ord(character)
    real_position_is = position - 64
    return real_position_is


char = input()
result = ab_pos(char)
print(result)
