journal = input().split(", ")
command = input()

while command != 'Craft!':
    current_command = command.split(" - ")
    action = current_command[0]
    item = current_command[1]

    if action == 'Collect':
        if item not in journal:
            journal.append(item)

    elif action == 'Drop':
        if item in journal:
            journal.remove(item)

    elif action == 'Combine Items':
        old_item, new_item = item.split(":")
        if old_item in journal:
            index = journal.index(old_item)
            journal.insert(int(index + 1), new_item)

    elif action == 'Renew':
        if item in journal:
            index = int(journal.index(item))
            journal.append(item)
            journal.remove(item)

    command = input()

print(", ".join(journal))
