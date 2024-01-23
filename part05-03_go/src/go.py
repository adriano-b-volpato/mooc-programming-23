# Write your solution here


def who_won(game_board: list):
    score_player_1 = 0
    score_player_2 = 0
    for row in game_board:
        for element in row:
            if element == 1:
                score_player_1 += 1
            if element == 2:
                score_player_2 += 1
    if score_player_1 > score_player_2:
        return 1
    if score_player_2 > score_player_1:
        return 2
    else:
        return 0
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    board = [[1, 2, 0],[2, 0, 0]]
    print(who_won(board))
    