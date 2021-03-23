# Game Board
board = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_']


# Display Game Board
def display_board():
    print(board[0], '|', board[1], '|', board[2])
    print(board[3], '|', board[4], '|', board[5])
    print(board[6], '|', board[7], '|', board[8])


if __name__ == '__main__':
    display_board()
