age = int(input())

if age <= 14:
    print(f'drink toddy')

elif 18 >= age > 14:
    print('drink coke')

elif 21 >= age > 18:
    print('drink beer')

else:
    print('drink whisky')