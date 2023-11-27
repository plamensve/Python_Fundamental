num = int(input())
plants_data = {}

for _ in range(num):
    plant, rarity = input().split("<->")
    plants_data[plant] = {"rarity": rarity, "ratings": []}

command = input()

while command != "Exhibition":
    command_parts = command.split(" ")

    if command_parts[0] == "Rate:":
        _, plant, _, rating = command_parts
        if plant in plants_data:
            plants_data[plant]["ratings"].append(int(rating))
        else:
            print("error")

    elif command_parts[0] == "Update:":
        _, plant, _, new_rarity = command_parts
        if plant in plants_data:
            plants_data[plant]["rarity"] = new_rarity
        else:
            print("error")

    elif command_parts[0] == "Reset:":
        _, plant = command_parts
        if plant in plants_data:
            plants_data[plant]["ratings"] = []
        else:
            print("error")

    command = input()

print("Plants for the exhibition:")
for plant, data in plants_data.items():
    avg_rating = sum(data["ratings"]) / len(data["ratings"]) if data["ratings"] else 0
    print(f"- {plant}; Rarity: {data['rarity']}; Rating: {avg_rating:.2f}")