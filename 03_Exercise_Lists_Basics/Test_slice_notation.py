collection_of_items = input().split("|")
budget = float(input())

item_list = []
price_list = []

for item in collection_of_items:
    item_list.append(item)

for price in item_list:
    # Използвайте slice notation [-4:] за изваждане на последните четири символа
    last_four_characters = price[-4:]
    print(last_four_characters)
