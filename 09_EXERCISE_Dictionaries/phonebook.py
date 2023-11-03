phonebook = {}
while True:
    entry = input()

    if '-' not in entry:
        break

    name, phone_number = entry.split('-')
    phonebook[name] = phone_number

for search in range(int(entry)):
    searched_name = input()
    if searched_name not in phonebook:
        print(f"Contact {searched_name} does not exist.")
    else:
        print(f"{searched_name} -> {phonebook[searched_name]}")