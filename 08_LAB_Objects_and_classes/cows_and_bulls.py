player_1 = [int(number) for number in input(f"Player 1, write your numbers and press enter: ").split()]
while True:
    current_guess = [int(number) for number in input(f"Guess the numbers: ").split()]
    if current_guess == player_1:
        break

    bulls = 0
    cows = 0
    for x in current_guess:
        for y in player_1:
            if current_guess.index(x) == player_1.index(y):
                bulls += 1

            elif x == y:
                cows += 1


print(f'You win')
