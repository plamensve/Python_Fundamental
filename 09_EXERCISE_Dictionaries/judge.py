user_stat = {}
contest_stat = {}
while True:
    line = input()
    if line == 'no more time':
        break

    username, contest, points = line.split(' -> ')
    points = int(points)

    if username not in user_stat:  # User stats points
        user_stat[username] = points
    else:
        user_stat[username] += points

    if contest not in contest_stat:  # Contests stats
        contest_stat[contest] = [username, points]
    else:
        contest_stat[contest].append(username)
        contest_stat[contest].append(points)

for k, v in contest_stat.items():
    counter = 1
    print(f"{k}: {len(contest_stat[k]) // 2} participants")
    for index in range(0, len(v), 2):
        name = index
        point = index + 1
        print(f"{counter}. {v[name]} <::> {v[point]}")
        counter += 1

print(f"Individual standings:")
counter2 = 1
for key, value in user_stat.items():
    print(f"{counter2}. {key} -> {value}")
    counter2 += 1