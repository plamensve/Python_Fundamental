lines = int(input())
positive = []
negative = []
count_positive = 0
sum_negative = 0

for _ in range(lines):
    data = int(input())

    if data >= 0:
        positive.append(data)
        count_positive += 1
    else:
        negative.append(data)
        sum_negative += data

print(positive)
print(negative)
print(f"Count of positives: {count_positive}\nSum of negatives: {sum_negative}")