collection_of_items = input().split("|")
budget = float(input())

price_list = []
profit = 0
sum_of_all_new_prices = 0
check_item_price = []
flag = False
new_budget = 0

for item in collection_of_items:
    new_item = item.split("->")
    check_item = new_item[0]
    sub_price = item.split(">")[-1]
    check_item_price.append(check_item)

    if (check_item == 'Clothes' and float(sub_price) <= 50) or \
            (check_item == 'Shoes' and float(sub_price) <= 35) or \
            (check_item == 'Accessories' and float(sub_price) <= 25.50):
        flag = True

    if flag is True:
        if float(sub_price) <= float(budget):
            budget -= float(sub_price)
            new_price = float(sub_price) * 1.4
            price_list.append(f"{new_price:.2f}")
            sum_of_all_new_prices += float(new_price)
            price_diff = float(new_price) - float(sub_price)
            profit += price_diff
            flag = False
        else:
            continue

new_budget = budget + sum_of_all_new_prices

print(*price_list, sep=" ")
print(f"Profit: {profit:.2f}")
if new_budget >= 150:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")
