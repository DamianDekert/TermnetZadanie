'''Checking is there is a winning conifguration'''


def check_win(board):
    # Check rows
    for row in board:
        if all(cell == "X" for cell in row) or \
                all(cell == "O" for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == "X" for row in range(3)) or \
                all(board[row][col] == "O" for row in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and \
            (board[0][0] == "X" or board[0][0] == "O"):
        return True
    if board[0][2] == board[1][1] == board[2][0] and \
            (board[0][2] == "X" or board[0][2] == "O"):
        return True

    return False


if __name__ == "__main__":
    check_win()
