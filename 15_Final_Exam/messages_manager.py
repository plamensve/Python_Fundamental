capacity_messages = int(input())
user_info = {}

command = input()
while True:
    if command == 'Statistics':
        break
    current_command = command.split('=')

    if current_command[0] == 'Add':
        user_name = current_command[1]
        sent = int(current_command[2])
        received = int(current_command[3])

        if user_name not in user_info:
            user_info[user_name] = {'sent': sent, 'received': received}

    elif current_command[0] == 'Message':
        sender = current_command[1]
        receiver = current_command[2]
        if sender in user_info and receiver in user_info:
            user_info[sender]['sent'] += 1
            user_info[receiver]['received'] += 1

            sender_total = user_info[sender]['sent'] + user_info[sender]['received']
            receiver_total = user_info[receiver]['sent'] + user_info[receiver]['received']

            if sender_total >= capacity_messages:
                del user_info[sender]
                print(f"{sender} reached the capacity!")
            if receiver_total >= capacity_messages:
                print(f"{receiver} reached the capacity!")
                del user_info[receiver]

    elif current_command[0] == 'Empty':
        user_name_for_delete = current_command[1]
        if user_name_for_delete.startswith('All'):
            user_info.clear()

        elif user_name_for_delete in user_info:
            del user_info[user_name_for_delete]

    command = input()
if len(user_info) > 0:
    print(f"Users count: {len(user_info)}")
    for k, v in user_info.items():
        total_sum = user_info[k]['sent'] + user_info[k]['received']
        print(f"{k} - {total_sum}")