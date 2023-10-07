def characters_between(character_1: str, character_2: str):
    single_string = []
    for char in range(ord(character_1) + 1, ord(character_2)):
        single_string.append(chr(char))
    return single_string


first_char = input()
second_char = input()
print(*characters_between(first_char, second_char))