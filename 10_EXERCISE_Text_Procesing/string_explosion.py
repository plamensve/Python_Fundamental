explosion_line = input()
exploded_string = ''
explosion_power = 0

for index in range(len(explosion_line)):
    if explosion_power > 0 and explosion_line[index] != '>':
        explosion_power -= 1
    elif explosion_line[index] == '>':
        exploded_string += explosion_line[index]
        explosion_power += int(explosion_line[index + 1])
    else:
        exploded_string += explosion_line[index]

print(exploded_string)
