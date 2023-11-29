import re

text_string = input()

pattern = r'(?i)([#|])([a-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)([0-9]+)(\1)'
matches = re.findall(pattern, text_string)

total_calories = 0
for match in matches:
    total_calories += int(match[5])
print(f"You have food to last you for: {total_calories // 2000} days!")

for match in matches:
    item = match[1]
    best_before = match[3]
    calories = match[5]
    print(f"Item: {item}, Best before: {best_before}, Nutrition: {calories}")
#