import re

text_string = input()
pattern = r'(?i)([#|])([a-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)([0-9]+)(\1)'

matches = re.findall(pattern, text_string)
total_calories = 0
for match in matches:
    total_calories += int(match[5])

days = total_calories // 2000  # 2000 calories per day are needed
print(f"You have food to last you for: {days} days!")

for match in matches:
    item = match[1]
    best_before = match[3]
    nutrition = int(match[5])
    print(f"Item: {item}, Best before: {best_before}, Nutrition: {nutrition}")