money_as_string = input().split(", ")
number_of_beggars = int(input())
money_as_integer = []

for current_money in money_as_string:
    money_as_integer.append(int(current_money))
starting_intex = 0
final_sum = []

while starting_intex < number_of_beggars:
    current_beggar_sum = 0

    for current_index in range(starting_intex, len(money_as_integer), number_of_beggars):
        current_beggar_sum += money_as_integer[current_index]
    final_sum.append(current_beggar_sum)
    starting_intex += 1

print(final_sum)