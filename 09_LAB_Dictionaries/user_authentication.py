user_credentials = {}
user_info = {}


def user_registration():
    user_name = input('Add your user name: ')
    if user_name in user_credentials:
        print('User name already exist. Please choose other username')
    else:
        password = input('Add your password: ')
        user_credentials[user_name] = password
        email = input('Please add your e-mail: ')
        phone = input('Please add your phone number: ')
        user_info[user_name] = email, phone
        print('Your account has been created!')


def user_login():
    user = input('Please enter your username: ')
    user_pass = input('Please enter your password: ')
    if user in user_credentials:
        if user_credentials[user] != user_pass:
            print('Your password is wrong!')
        else:
            print('Successful login')
            user_info_result = user_profile(user)  # Получаване на информацията за потребителя
            if user_info_result:
                email, phone = user_info_result
                print(f'User info: Email: {email}, Phone: {phone}')
            else:
                print('User not found')
    else:
        print('Your username is not found! Please, create an account!')


def user_profile(user):
    return user_info.get(user)


def show_credential():
    print(user_credentials)
    print(user_info)


def exit_system():
    print('Goodbye!')
    exit()


while True:
    print(f'\nUser authentication')
    print(f'1. User Registration')
    print(f'2. User Login')
    print(f'3. Exit')
    print(f'4. Show credential')

    choice = input('Enter your choise (1/2/3/4): ')

    if choice == '1':
        user_registration()
    elif choice == '2':
        user_login()
    elif choice == '3':
        exit_system()
    elif choice == '4':
        show_credential()
    else:
        print('Invalid choise. Please select 1, 2 or 3.')
