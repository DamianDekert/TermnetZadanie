from tic_tac_toe.board_logic import check_win


# AI always play as a "O" player
def minimax(board, turn):
    if check_win(board):
        if turn == 'O':
            return 1
        else:
            return -1
    elif all(cell is not None for row in board for cell in row):
        return 0

    if turn == 'O':
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    board[row][col] = 'O'
                    score = minimax(board, 'X')
                    board[row][col] = None
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    board[row][col] = 'X'
                    score = minimax(board, 'O')
                    board[row][col] = None
                    best_score = min(best_score, score)
        return best_score
