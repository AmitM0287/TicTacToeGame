from random import randrange
from logging_configuration import logging_config

# Get logger from logging configuration
logger = logging_config.get_logger()

# Declare player & computer variable
player = ''
computer = ''

# Game Board
board = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_']

# Game is still going is set by default True.
game_still_going = True

# Declare current player variable
current_player = ''


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
    This function is used to assigned letter X or O to the player.
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
    if player_ == 'X':
        print('\nNow ', player_ + "'s turn.")
        position = randrange(0, 9)
        while board[position] not in ['_']:
            position = randrange(0, 9)
        board[position] = player_
        display_board()
    if player_ == 'O':
        print('\nNow ', player_ + "'s turn.")
        position = int(input('Choose a position from 1-9 (available): '))
        while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            position = int(input('Invalid Input. Choose a position from 1-9:'))
        position = position - 1
        while board[position] not in ['_']:
            position = int(input('Position is already taken. Choose from available positions: '))
            position = position - 1
        board[position] = player_
        display_board()


def flip_player():
    """
    This function is used to flip the player.
    :return: None
    """
    global current_player
    # If current player is X, then set current player to O.
    if current_player == 'X':
        current_player = 'O'
    # If current player is O, then set current player to X.
    elif current_player == 'O':
        current_player = 'X'


def play_game():
    """
    This function is used to play Tic Tac Toe game.
    :return: None
    """
    # Display board
    display_board()
    # While game is still going
    while game_still_going:
        handle_turn(current_player)
        flip_player()


if __name__ == '__main__':
    try:
        print('\nWelcome To Tic Tac Toe Game\n')
        # Display fresh board
        print('Fresh Board : ')
        display_board()
        # Assigned letter to computer & player
        assigned_letter()
        print('\nComputer Plays : ', computer)
        print('Player Plays: ', player)
        # Begin toss to who plays first
        if who_plays_first() == globals()['computer']:
            print('\nComputer plays first!')
            # Set the current player as computer
            globals()['current_player'] = globals()['computer']
        else:
            print('\nPlayer plays first!')
            # Set the current player as player
            globals()['current_player'] = globals()['player']
        # Play Tic Tac Toe Game
        play_game()
    except Exception as e:
        print('Oops! Something went wrong! Try again...')
        logger.exception(e)
