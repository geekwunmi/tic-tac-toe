# This part of the game needs to be reviewed to make work
# It is an attempt to re-create the functions of the base game into a unique
# ggame. Please rework and add into main game or delete entirely if not needed

player1 = input("Please pick a marker 'X' or 'O'")

position = int(input('Please enter a number '))

from IPython.display import clear_output


def display_board(gameboard):
    clear_output()

    print('   |   |')
    print(' ' + gameboard[1] + ' | ' + gameboard[2] + ' | ' + gameboard[3])
    print('   |   |')
    print('************')
    print(' ' + gameboard[4] + ' | ' + gameboard[5] + ' | ' + gameboard[6])
    print('   |   |')
    print('************')
    print(' ' + gameboard[7] + ' | ' + gameboard[8] + ' | ' + gameboard[9])
    print('   |   |')


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']

display_board(test_board)

game_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)


display_game(game_list)


def position_choice():
    choice = 'wrong'

    while choice not in ['0', '1', '2']:

        choice = input("Pick a position (0,1,2): ")

        if choice not in ['0', '1', '2']:
            print("Sorry, invalid choice! ")

    return int(choice)


position_choice()

position_choice()


def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")

    game_list[position] = user_placement

    return game_list


replacement_choice(game_list, 1)


def gameon_choice():
    choice = 'wrong'

    while choice not in ['Y'.casefold(), 'N'.casefold()]:

        choice = input("Keep playing? (Y or N) ")

        if choice not in ['Y'.casefold(), 'N'.casefold()]:
            print("Sorry, I dont understand, please choose Y or N ")

    if choice == "Y".casefold():
        return True
    else:
        return False


gameon_choice()

game_on = True
game_list = [0, 1, 2]

while game_on:
    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list, position)

    display_game(game_list)

    game_on = gameon_choice()

# this part of the code needs to be reviewed and updated to work
# after which alterations should be made to make it run differently from
# the base game create don the course

from IPython.display import clear_output


def display_board(gameboard):
    clear_output()

    print('   |   |')
    print(' ' + gameboard[1] + ' | ' + gameboard[2] + ' | ' + gameboard[3])
    print('   |   |')
    print('************')
    print(' ' + gameboard[4] + ' | ' + gameboard[5] + ' | ' + gameboard[6])
    print('   |   |')
    print('************')
    print(' ' + gameboard[7] + ' | ' + gameboard[8] + ' | ' + gameboard[9])
    print('   |   |')


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']

display_board(test_board)

gameboard = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?').casefold()

    if marker == 'X'.casefold():
        return ('X', 'O')
    else:
        return ('O', 'X')


player_input()


def place_marker(board, marker, position):
    board[position] = marker


place_marker(gameboard, '$', 8)
display_board(gameboard)

place_marker(gameboard, '$', 8)
display_board(gameboard)


def win_check(board, mark):
    mark = ''
    positions = []
    for mark in board[]:
        position = position.append(board[])
        if sum(board[]) % 3 == 0:
            return True


win_check(test_board, 'X')

import random


def choose_first():
    if random.randint(0, 1) == 0:
        return "SecondPlayer"
    else:
        return "FirstPlayer"


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position)
        position = int(input('Pick position: (1-9)'))


def replyay():
    return input('continue playing? Yes or No: ').casefold().startwith('y')


print('Welcome to Tic Tac Toe')

while True:
    thegameboard = [' '] * 10
    player1_play, player2_play = player_input()
    turn = choose_first()
    print(turn + 'will go first.')

    play_game = input('Ready? Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    elif play_game.lower()[0] == 'n':
        game_on = False
    else:
        return play_game[]

    while game_on:
        if turn == 'FirstPlayer':

            gameboard(thegameboard)
            position = player_choice(thegameboard)
            place_market(thegameboard, firstplayer_marker, position)

            if win_check(thegameboard, firstplayer_marker):
                display_board(thegameboard)
                print('Yooo! you smashed it')
                game_on = False
            else:
                if full_board_check(thegameboard):
                    display_board(thegameboard)
                    print('you both lose')
                    break
                else:
                    turn = "SecondPlayer"
        else:
            display_board(thegameboard)
            position = player_choice(thegameboard)
            place_marker(thegameboard, secondplayer_marker, position)

            if win_check(thegameboard, secondplayer_marker):
                display_board(thegameboard)
                print("second player won you knob")
                game_on = False
            else:
                if full_board_check(thegameboard):
                    display_board(thegameboard)
                    print('you both lose')
                    break
                else:
                    turn = 'Firstplayer'
    if not replay():
        break

