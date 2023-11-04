number = int(input())
cars = {}

for index in range(number):
    command = input().split()

    if command[1] in cars and command[0] == 'register':
        print(f"ERROR: already registered with plate number {cars[command[1]]}")
        continue

    elif command[0] == 'register':
        print(f"{command[1]} registered {command[2]} successfully")
        cars[command[1]] = command[2]

    elif command[0] == 'unregister':
        if command[1] in cars:
            print(f"{command[1]} unregistered successfully")
            del cars[command[1]]
        else:
            print(f"ERROR: user {command[1]} not found")


for k, v in cars.items():
    print(f"{k} => {v}")