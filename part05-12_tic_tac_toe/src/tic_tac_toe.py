# Write your solution here

def play_turn(game_board: list, x: int, y: int, piece: str):
    if 0 <= x < 3 and 0 <= y < 3:
        if game_board[y][x] == "":
            game_board[y][x] = piece
            return True
    
    
    return False
    




if __name__ == "__main__":
    game_board = [['', '', ''], ['X', 'O', ''], ['', 'O', '']]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)