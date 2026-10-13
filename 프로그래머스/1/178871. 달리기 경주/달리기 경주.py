

def solution(players, callings):
    
    new_players = {player : i for i, player in enumerate(players)}
    for i in range(len(callings)):
        temp = callings[i]
        idx = new_players[temp]
        bf = players[idx-1]
        t = players[idx-1]
        players[idx - 1] = players[idx]
        players[idx] = t
        new_players[temp] = idx-1
        new_players[bf] = idx
    
    return players