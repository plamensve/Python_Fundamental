some_string = input()
removing_vowels = 'a', 'o', 'u', 'e', 'i'

for_remove = [x for x in some_string if x.lower() not in removing_vowels]
result_string = ''.join(for_remove)
print(result_string)
