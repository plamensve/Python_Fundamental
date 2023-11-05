contests = {}
submissions = {}

while True:
    data = input()
    if data == "end of contests":
        break
    contest, password = data.split(":")
    contests[contest] = password

while True:
    data = input()
    if data == "end of submissions":
        break
    contest, password, username, points = data.split("=>")
    points = int(points)

    if contest in contests and contests[contest] == password:
        if username not in submissions:
            submissions[username] = {}
        if contest not in submissions[username] or points > submissions[username][contest]:
            submissions[username][contest] = points

best_candidate = max(submissions, key=lambda x: sum(submissions[x].values()))
total_points = sum(submissions[best_candidate].values())

print(f"Best candidate is {best_candidate} with total {total_points} points.")
print("Ranking:")

for username, contests_data in sorted(submissions.items(), key=lambda x: x[0]):
    print(username)
    for contest, points in sorted(contests_data.items(), key=lambda x: (-x[1], x[0])):
        print(f"#  {contest} -> {points}")

