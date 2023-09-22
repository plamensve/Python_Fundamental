age = int(input())

if 0 < age < 3:
    print('baby')

elif 3 <= age <= 13:
    print('child')

elif 14 <= age <= 19:
    print('teenager')

elif 20 <= age <= 65:
    print('adult')

elif age >= 65:
    print('elder')

