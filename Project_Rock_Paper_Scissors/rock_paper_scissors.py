rock_choice = 'r'  # Rock
paper_choice = 'p'  # Paper
scissors_choice = 's'  # Scissors
# Rock beat Scissors - rs
# Paper beat Rock - pr
# Scissors beat Paper - sp
# Drow - rr, pp, ss

command = input()  # Write 'Play' to start the game or 'End' to end the game!
game = ''

while True:
    if command == 'End':
        break
    else:
        player_one = input()
        player_two = input()
        game += player_one
        game += player_two

    if player_one != rock_choice and player_one != paper_choice and player_one != scissors_choice:
        print(
            "Your choice is invalide, please make your choice again!\nYou need to choose one of this options: 'r', 'p', 's' ")
        break

    if player_two != rock_choice and player_two != paper_choice and player_two != scissors_choice:
        print(
            "Your choice is invalide, please make your choice again!\nYou need to choose one of this options: 'r', 'p', 's' ")
        break

    if game == 'rs' or game == 'pr' or game == 'sp':
        print(f'The winner is Player one!')

    if game == 'sr' or game == 'rp' or game == 'ps':
        print(f'The winner is Player two!')

    if game == 'rr' or game == 'pp' or game == 'ss':
        print(f'Drow Game!')