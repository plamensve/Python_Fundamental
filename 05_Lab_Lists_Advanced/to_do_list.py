# command = input()
# to_do_list = []
# while command != 'End':
#     to_do_list.append(command)
#     command = input()
#
# to_do_list.sort()
# task_list = []
# for task in to_do_list:
#     split_task = task.split('-')
#     index = len(split_task)
#     task_list.append(split_task[index - 1])
#
# print(task_list)


def process_todo_note():
    todo_note = []

    while True:
        note = input()

        if note == 'End':
            break

        todo_note.append(note)

    sorted_notes = sorted(todo_note, key=lambda x: int(x.split('-')[0]))
    return [note.split('-')[1] for note in sorted_notes]


result = process_todo_note()
print(result)
