text = input()
my_dict = {}

for char in text:
    if char != ' ':
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1

for k, v in my_dict.items():
    print(f"{k} -> {v}")
