from tic_tac_toe.board_logic import minimax


def get_best_move(board):
    best_score = -1000
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                board[row][col] = 'O'
                score = minimax(board, 'O')
                board[row][col] = None

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move
