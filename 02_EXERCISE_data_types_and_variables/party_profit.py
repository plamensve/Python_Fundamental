from math import floor
group_size = int(input())
days = int(input())

earn_coins = 0
spend_for_companions = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        group_size = group_size - 2

    if i % 15 == 0:
        group_size = group_size + 5

    earn_coins += 50
    spend_for_companions += 2 * group_size

    if i % 3 == 0:
        spend_for_companions += 3 * group_size

    if i % 5 == 0:
        earn_coins += 20 * group_size
        if i % 3 == 0:
            spend_for_companions += 2 * group_size

diff = earn_coins - spend_for_companions
coins_per_companions = diff / group_size
print(f"{group_size} companions received {floor(coins_per_companions)} coins each.")