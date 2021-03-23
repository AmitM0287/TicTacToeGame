from random import randrange
from logging_configuration import logging_config

# get logger from logging configuration
logger = logging_config.get_logger()

# Declare player & computer variable
player = ''
computer = ''

# Game Board
board = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_']


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


if __name__ == '__main__':
    try:
        print('\nWelcome To Tic Tac Toe Game\n')
        # Display fresh board
        print('Fresh Board : ')
        display_board()
        # Assigned letter to computer & player
        assigned_letter()
        print('\nComputer Plays : ', computer)
        print('\nPlayer Plays: ', player)
    except Exception as e:
        print('Oops! Something went wrong! Try again...')
        logger.exception(e)
