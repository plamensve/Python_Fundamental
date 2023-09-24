lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shild_price = float(input())
armor_price = float(input())

helmet_repair = 0
sword_repair = 0
shild_repair = 0

for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0:
        helmet_repair += 1

    if fight % 3 == 0:
        sword_repair += 1

    if fight % 2 == 0 and fight % 3 == 0:
        shild_repair += 1

armor_repair = shild_repair // 2
total_sum = (helmet_repair * helmet_price) + (sword_repair * sword_price) + (shild_repair * shild_price) + (
            armor_repair * armor_price)
print(f"Gladiator expenses: {total_sum:.2f} aureus")
