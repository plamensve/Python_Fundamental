def existing_player():
    if player not in players_dict:
        players_dict[player] = [position, skill]
    else:
        check_position()


def check_position():
    if players_dict[player][0] == position:
        if players_dict[player][1] < skill:
            players_dict[player][1] = skill
    else:
        players_dict[player].append(position)
        players_dict[player].append(skill)


def dict_content():
    final_result = {}
    for key, value in players_dict.items():
        counter = 0
        for index in range(0, len(value), 2):
            posit = value[index]
            points = value[index + 1]
            counter += points
        final_result[key] = counter

    sorted_result = dict(sorted(final_result.items(), key=lambda item: item[1], reverse=True))
    sorted_players = {key: players_dict[key] for key in sorted_result.keys()}

    for k, v in sorted_players.items():
        print(f"{k}:")
        sorted_positions = [(v[i], v[i + 1]) for i in range(0, len(v), 2)]
        sorted_positions.sort(key=lambda x: (-x[1], x[0]))
        for position_v, points_v in sorted_positions:
            print(f"- {position_v} <::> {points_v}")


players_dict = {}
while True:
    line = input()
    if line == "Season end":
        break

    player, position, skill = line.split(' -> ')
    skill = int(skill)
    existing_player()

dict_content()

# players = {}
# common_positions = {}

# while True:
#     command = input()
#     if command == "Season end":
#         break
#
#     if "vs" in command:
#         player1, player2 = command.split(" vs ")
#         if player1 in players and player2 in players:
#             common_positions = set(players[player1].keys()) & set(players[player2].keys())
#             if common_positions:
#                 total_skill_player1 = sum(players[player1][pos] for pos in common_positions)
#                 total_skill_player2 = sum(players[player2][pos] for pos in common_positions)
#
#                 if total_skill_player1 > total_skill_player2:
#                     del players[player2]
#                 elif total_skill_player1 < total_skill_player2:
#                     del players[player1]
#         continue
#
#     player, position, skill = command.split(" -> ")
#     skill = int(skill)
#
#     if player not in players:
#         players[player] = {position: skill}
#     else:
#         if position not in players[player]:
#             players[player][position] = skill
#         else:
#             if players[player][position] < skill:
#                 players[player][position] = skill
#
# # Sort players by total skill points (descending) and player name (ascending)
# sorted_players = sorted(players.keys(), key=lambda x: (-sum(players[x].values()), x))
#
# for player in sorted_players:
#     total_skill = sum(players[player].values())
#     print(f"{player}: {total_skill} skill")
#
#     sorted_positions = sorted(players[player].keys(), key=lambda x: (-players[player][x], x))
#     for position in sorted_positions:
#         print(f"- {position} <::> {players[player][position]}")
