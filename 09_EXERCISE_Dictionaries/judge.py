contests = {}
users = {}

while True:
    input_line = input()
    if input_line == "no more time":
        break

    username, contest, points = input_line.split(" -> ")
    points = int(points)

    if contest not in contests:
        contests[contest] = []

    found_user = None
    for entry in contests[contest]:
        if entry[0] == username:
            found_user = entry
            break

    if found_user is None:
        contests[contest].append((username, points))
    else:
        if found_user[1] < points:
            found_user = (username, points)

    if username not in users:
        users[username] = 0
    users[username] += points

# Sort and print contest results
for contest, participants in contests.items():
    print(f"{contest}: {len(participants)} participants")
    sorted_participants = sorted(participants, key=lambda x: (-x[1], x[0]))
    for i, (username, points) in enumerate(sorted_participants, start=1):
        print(f"{i}. {username} <::> {points}")

# Sort and print individual standings
print("Individual standings:")
sorted_users = sorted(users.items(), key=lambda x: (-x[1], x[0]))
for i, (username, total_points) in enumerate(sorted_users, start=1):
    print(f"{i}. {username} -> {total_points}")







