command = input()
my_dict = {}

while command != 'end':
    current_command = command.split(' : ')
    course, name = current_command
    if course not in my_dict:
        my_dict[course] = []
    my_dict[course] += name,
    command = input()

for k, v in my_dict.items():
    print(f"{k}: {len(v)}")
    for name in v:
        print(f"-- {name}")



