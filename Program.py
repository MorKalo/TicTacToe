import random
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

the_board_isnt_full = True
winner = None
now_playing = "X"


def play_game():
    print_board()
    while the_board_isnt_full:
        if now_playing=='X':
            turn(now_playing)
        else:
            computer_turn()
        check_if_game_over()
        replace_player()
        print('**********************************')
    if winner == "X" or winner == "O":
        print('******************')
        print('*THE WINNER IS ', winner, ' *')
        print('******************')
    elif winner == None:
        print('there is a TIE')


def print_board():
    print(board[0], ' | ' , board[1] , ' | ' , board[2], '     1 | 2 | 3')
    print(board[3], ' | ' , board[4] , ' | ' , board[5], '     4 | 5 | 6')
    print(board[6], ' | ' , board[7] , ' | ' , board[8], '     7 | 8 | 9')


def turn(player):
    print('it''s', player, 'turn')
    choose = input('Which cube do you choose?  ')
    valid = False
    while not valid:
        while choose not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            choose = input("Choose a cube between 1-9 ")
        choose = int(choose) - 1
        if board[choose] == '-':
            valid = True
        else:
            print('This cube is hooked, please select another cube')
    board[choose] = player
    print_board()


def check_if_game_over():
    check_win()
    check_tie()


def check_win():
    global winner
    row_win = check_rows()
    column_win = check_columns()
    diagonal_win = check_diagonals()
    if row_win:
        winner = row_win
    elif column_win:
        winner = column_win
    elif diagonal_win:
        winner = diagonal_win
    else:
        winner = None


def check_rows():
    global the_board_isnt_full
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    if row1 or row2 or row3:
        the_board_isnt_full = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None


def check_columns():
    global the_board_isnt_full
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'
    if column1 or column2 or column3:
        the_board_isnt_full = False
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    else:
        return None


def check_diagonals():
    global the_board_isnt_full
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'
    if diagonal1 or diagonal2:
        the_board_isnt_full = False
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    else:
        return None


def check_tie():
    global the_board_isnt_full
    if '-' not in board:
        the_board_isnt_full = False
        return True
    else:
        return False


def replace_player():
    global now_playing
    if now_playing == 'X':
        now_playing = 'O'
    elif now_playing == 'O':
        now_playing = 'X'

def computer_turn(player='O'):
    print('it"s the COMPUTER turn')
    choose =random.randint(0,8)
    valid = False
    while not valid:
        if board[choose] == '-':
            valid = True
        else:
            choose = random.randint(0, 8)
    board[choose] = player
    print_board()


play_game()