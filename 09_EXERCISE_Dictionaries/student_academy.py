line = int(input())
all_grades = {}
for _ in range(line):
    name = input()
    grade = float(input())
    if name in all_grades:
        all_grades[name].append(grade)
    else:
        all_grades[name] = [grade]

higher_grade = {}
for k, v in all_grades.items():
    avg = sum(v) / len(v)
    if avg >= 4.50:
        higher_grade[k] = avg

for k, v in higher_grade.items():
    print(f"{k} -> {v:.2f}")


