plants_n = int(input())
plants_collection = {}
for _ in range(plants_n):
    plant_info = input().split("<->")
    name, rarity = plant_info[0], int(plant_info[1])
    plants_collection[name] = {"rarity": rarity, "ratings": [0]}

while True:
    command = input().split()
    if command[0] == "Exhibition":
        break
    elif command[0] == "Rate:":
        plant_name = command[1]
        plant_rating = int(command[3])
        if plant_name in plants_collection:
            plants_collection[plant_name]["ratings"].append(plant_rating)
        else:
            print("error")
    elif command[0] == "Update:":
        plant_name = command[1]
        new_rarity = int(command[3])
        if plant_name in plants_collection:
            plants_collection[plant_name]["rarity"] = new_rarity
        else:
            print("error")
    elif command[0] == "Reset:":
        plant_name = command[1]
        if plant_name in plants_collection:
            plants_collection[plant_name]["ratings"] = [0]
        else:
            print("error")

print("Plants for the exhibition:")
for item_name, plant_information in plants_collection.items():
    if len(plant_information['ratings']) <= 1:
        average_rating = 0
    else:
        average_rating = sum(plant_information['ratings']) / (len(plant_information['ratings']) - 1)
    print(f"- {item_name}; Rarity: {plant_information['rarity']}; Rating: {average_rating:.2f}")