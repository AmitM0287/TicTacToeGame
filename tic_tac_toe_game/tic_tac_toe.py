from random import randrange
from logging_configuration import logging_config

# Get logger from logging configuration.
logger = logging_config.get_logger()

# Declare player & computer variable.
player = ''
computer = ''

# Game Board.
board = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_']

# Game is still going is set by default True.
game_still_going = True

# Declare current player variable.
current_player = ''

# Declare winner variable.
winner = None


def display_board():
    """
    This function is used to display the game board.
    :return: None
    """
    print(board[0], '|', board[1], '|', board[2])
    print(board[3], '|', board[4], '|', board[5])
    print(board[6], '|', board[7], '|', board[8])


def assigned_letter():
    """
    This function is used to assigned letter 'X' or 'O' to the player.
    :return: None
    """
    random = randrange(0, 2)
    if random == 0:
        globals()['player'] = 'X'
        globals()['computer'] = 'O'
    else:
        globals()['player'] = 'O'
        globals()['computer'] = 'X'


def who_plays_first():
    """
    This function is used to determine who plays first.
    :return: It's return the player who plays first.
    """
    random = randrange(0, 2)
    if random == 0:
        return globals()['computer']
    else:
        return globals()['player']


def handle_turn(player_):
    """
    This function is used to handle turn of the players.
    :param player_: It's accept player object as a parameter.
    :return: None
    """
    if player_ == computer:
        print('\nNow ', player_ + "'s turn.")
        position = randrange(0, 9)
        while board[position] not in ['_']:
            position = randrange(0, 9)
        board[position] = computer
        display_board()
    if player_ == player:
        print('\nNow ', player_ + "'s turn.")
        position = int(input('Choose a position from 1-9 (available): '))
        while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            position = int(input('Invalid Input. Choose a position from 1-9: '))
        position = position - 1
        while board[position] not in ['_']:
            position = int(input('Position is already taken. Choose from available positions: '))
            position = position - 1
        board[position] = player
        display_board()


def flip_player():
    """
    This function is used to flip the player.
    :return: None
    """
    global current_player
    # If current player is 'X', then set current player to 'O'.
    if current_player == 'X':
        current_player = 'O'
    # If current player is 'O', then set current player to 'X'.
    elif current_player == 'O':
        current_player = 'X'


def play_game():
    """
    This function is used to play Tic Tac Toe game.
    :return: None
    """
    # Display board.
    display_board()
    # While game is still going.
    while game_still_going:
        # Handle a single turn of an arbitrary player.
        handle_turn(current_player)
        # Flip to another player.
        flip_player()
        # Check weather game is over or not.
        check_if_game_over()


def check_if_game_over():
    """
    This function is used to check game is over or not.
    :return: None
    """
    # Calling check for winners.
    check_for_winner()
    # Calling check it's tie or not.
    check_if_tie()


def check_for_winner():
    """
    This function is used to check who is winner or not.
    :return: None
    """
    global winner
    # Check rows.
    row_winner = check_rows()
    # Check columns.
    column_winner = check_columns()
    # Check diagonals.
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_if_tie():
    """
    This function is used to check weather it's a tie or not.
    :return: None
    """
    global game_still_going
    if '_' not in board:
        game_still_going = False


def check_rows():
    """
    This function is used to check row-wise winner.
    :return: It's return the winner.
    """
    global game_still_going
    # Check if any of the rows have all the same value.
    row1 = board[0] == board[1] == board[2] != '_'
    row2 = board[3] == board[4] == board[5] != '_'
    row3 = board[6] == board[7] == board[8] != '_'
    # If any row does have a match, then game still going to False.
    if row1 or row2 or row3:
        game_still_going = False
    # Return winner 'X' or 'O'.
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]


def check_columns():
    """
    This function is used to check column-wise winner.
    :return: It's return the winner.
    """
    global game_still_going
    # Check if any of the rows have all the same value.
    column1 = board[0] == board[3] == board[6] != '_'
    column2 = board[1] == board[4] == board[7] != '_'
    column3 = board[2] == board[5] == board[8] != '_'
    # If any column does have a match, then game still going to False.
    if column1 or column2 or column3:
        game_still_going = False
    # Return winner 'X' or 'O'.
    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[2]


def check_diagonals():
    """
    This function is used to check diagonal-wise winner.
    :return: It's return the winner.
    """
    global game_still_going
    # Check if any of the rows have all the same value.
    diagonal1 = board[0] == board[4] == board[8] != '_'
    diagonal2 = board[6] == board[4] == board[2] != '_'
    # If any diagonals does have a match, then game still going to False.
    if diagonal1 or diagonal2:
        game_still_going = False
    # Return winner 'X' or 'O'.
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[6]


if __name__ == '__main__':
    try:
        print('\nWelcome To Tic Tac Toe Game\n')
        # Display fresh board.
        print('Fresh Board : ')
        display_board()
        # Assigned letter to computer & player.
        assigned_letter()
        print('\nComputer Plays : ', computer)
        print('Player Plays: ', player)
        # Begin toss to who plays first.
        if who_plays_first() == globals()['computer']:
            print('\nComputer plays first!')
            # Set the current player as computer.
            globals()['current_player'] = globals()['computer']
        else:
            print('\nPlayer plays first!')
            # Set the current player as player.
            globals()['current_player'] = globals()['player']
        # Play Tic Tac Toe Game.
        play_game()
        # Game has Ended.
        if winner == 'X' or winner == 'O':
            print('\n', winner, ' won the match!')
        elif winner is None:
            print("It's a Tie.")
    except Exception as e:
        print('Oops! Something went wrong! Try again...')
        logger.exception(e)
