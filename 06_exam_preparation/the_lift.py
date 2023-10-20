people_waiting = int(input())
lift_states = list(map(int, input().split(" ")))

for cab in range(len(lift_states)):
    can_load = min(4 - lift_states[cab], people_waiting)
    lift_states[cab] += can_load
    people_waiting -= can_load

empty_spot = 0
for spot in lift_states:
    if spot < 4:
        empty_spot += 1
if empty_spot > 0:
    print(f'The lift has empty spots!')
    print(*lift_states)

elif people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(*lift_states)

elif people_waiting == 0 or empty_spot == 0:
    print(*lift_states)