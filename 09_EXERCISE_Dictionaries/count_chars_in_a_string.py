text = list(input())
my_dict = {}
for char in text:
    if char.isalpha():
        point = text.count(char)
        my_dict[char] = point

for k, v in my_dict.items():
    print(f"{k} -> {v}")
