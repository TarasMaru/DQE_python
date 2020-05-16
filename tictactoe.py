import os


def clear():
    os.system('cls')


def show_game_board():
    print("-------------")
    for i in range(3):
        rowl = '|'
        for row in game_board[i]:
            rowl += f' {row} |'
        print(rowl)
        print("-------------")


def convert_number_coord(numb):

    for i in range(3):
        coun = -1
        for row in game_board[i]:
            coun += 1
            if numb == row:
                x, y = i, coun
                game_board_available.remove(f'{numb}')
    return x, y


def update_game_board(coordd, player):
    row, column = coordd
    if player == 'O':
        game_board[row][column] = f'\033[31m{player}\033[0m'
    else:
        game_board[row][column] = f'\033[34m{player}\033[0m'


def check_if_win(player):
    if not player == 'O':
        player = f'\033[34m{player}\033[0m'
    else:
        player = f'\033[31m{player}\033[0m'
    if game_board[0] == [f'{player}', f'{player}', f'{player}'] or game_board[1] == [f'{player}', f'{player}', f'{player}'] or game_board[2] == [f'{player}', f'{player}', f'{player}']:
        print(f'\033[32mPlayer {player}\033[32m won! \033[0m')
    elif game_board[0][0] == game_board[1][0] == game_board[2][0]:
        print(f'\033[32mPlayer {player}\033[32m won! \033[0m')
    elif game_board[0][1] == game_board[1][1] == game_board[2][1]:
        print(f'\033[32mPlayer {player}\033[32m won! \033[0m')
    elif game_board[0][2] == game_board[1][2] == game_board[2][2]:
        print(f'\033[32mPlayer {player}\033[32m won! \033[0m')
    elif game_board[0][0] == game_board[1][1] == game_board[2][2]:
        print(f'\033[32mPlayer {player}\033[32m won! \033[0m')
    elif game_board[0][2] == game_board[1][1] == game_board[2][0]:
        print(f'\033[32mPlayer {player}\033[32m won! \033[0m')
    else:
        return 0


def check_first_go():
    while True:
        first_go = input('Please choose your marker - O / X   ')
        if first_go in ['O', 'X']:
            clear()
            return first_go


def get_user_number(player):
    if not player == 'O':
        player = f'\033[34m{player}\033[0m'
    else:
        player = f'\033[31m{player}\033[0m'
    numb = input(f"{player} -\033[32m Player please enter a number \033[0m")
    while numb not in [1, 2, 3, 4, 5, 6, 7, 8, 9] and numb not in game_board_available:
        numb = input(f"{player} -\033[32m please enter a VALID number \033[0m")
    return numb


game_board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
game_board_available = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
first = check_first_go()
if first == 'X':
    second = 'O'
else:
    second = 'X'
show_game_board()

counter = 0
while True:

    Player_f = get_user_number(player=first)
    coord = convert_number_coord(Player_f)
    update_game_board(coord, f'{first}')
    counter += 1
    clear()
    show_game_board()

    if counter > 4:
        if check_if_win(f'{first}') != 0:
            break
    if counter > 8:
        if len(game_board_available) == 0:
            print('\033[32m    Draw \033[0m')
            break
    Player_s = get_user_number(player=second)
    coord = convert_number_coord(Player_s)
    update_game_board(coord, f'{second}')
    counter += 1
    clear()
    show_game_board()
    if counter > 4:
        if check_if_win(f'{second}') != 0:
            break












