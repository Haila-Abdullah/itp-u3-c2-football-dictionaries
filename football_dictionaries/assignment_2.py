def players_by_position(squads_list):
    def players_grouped_by_position(squads_list):
    grouped_players = {}
    for player in squads_list:
        player_dict = {
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8],
        }

        position = player[1]
        if position not in grouped_players:
            grouped_players[position] = []
        grouped_players[position].append(player_dict)

    return grouped_players

grouped_by_position = players_grouped_by_position(squads_list)
print(grouped_by_position)
