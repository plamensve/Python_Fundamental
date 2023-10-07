numbers = input().split(",")
my_list = []

for number in numbers:
    my_list.append(int(number))

repetition = my_list.count(0)
for _ in range(repetition):
    my_list.remove(0)
    my_list.insert(len(my_list), 0)
print(my_list)




