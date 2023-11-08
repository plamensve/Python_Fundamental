fruits = [{'name': 'apple', 'price': 0.5}, {'name': 'banana', 'price': 0.25}, {'name': 'cherry', 'price': 1.0}]
sorted_fruits = sorted(fruits, key=lambda x: x['price'])  # Сортиране по цена
print(sorted_fruits)