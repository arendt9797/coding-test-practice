def solution(players, callings):
    rankings = { player: i for i, player in enumerate(players) }
    
    for called_player in callings:
        player_rank = rankings[called_player]
        front_player = players[player_rank - 1]
        players[player_rank - 1], players[player_rank] = players[player_rank], players[player_rank - 1]
        
        rankings[called_player] -= 1
        rankings[front_player] += 1
    
    return players
    