number_of_electrons = int(input())
electron_count = number_of_electrons
electron_shell = 1
inserted_electrons = []

while True:
    if electron_count <= 0:
        print(inserted_electrons)
        break

    insert = 2 * electron_shell ** 2
    if insert <= electron_count:
        inserted_electrons.append(insert)
        electron_count -= insert
        electron_shell += 1
    else:
        inserted_electrons.append(electron_count)
        print(inserted_electrons)
        break
