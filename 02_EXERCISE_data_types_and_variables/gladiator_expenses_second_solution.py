lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shild_price = float(input())
armor_price = float(input())

helmet_repair = lost_fights_count // 2
sword_repair = lost_fights_count // 3
shild_repair = lost_fights_count // (2 * 3)
armor_repair = shild_repair // 2

total_sum = (helmet_repair * helmet_price) + (sword_repair * sword_price) + (shild_repair * shild_price) + (
        armor_repair * armor_price)
print(f"Gladiator expenses: {total_sum:.2f} aureus")
