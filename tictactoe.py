from os import system  # Common for both games
from random import choice  # Pertain to two players game


def clear():  # Common for both games
    system('cls')


def show_game_board():  # Common for both games
    print("-------------")
    for i in range(3):
        rowl = '|'
        for row in game_board[i]:
            rowl += f' {row} |'
        print(rowl)
        print("-------------")


def convert_number_coord(numb):  # Common for both games
    for i in range(3):
        coun = -1
        for row in game_board[i]:
            coun += 1
            if numb == row:
                x, y = i, coun
                game_board_available.remove(f'{numb}')
    return x, y


def convert_number_coord_(numb):  # Pertain to two players game
    for i in range(3):
        coun = -1
        for row in game_board_[i]:
            coun += 1
            if numb == row:
                x, y = i, coun
    return x, y


def update_game_board(coord, player):  # Common for both games
    row, column = coord
    if player == 'O':
        game_board[row][column] = f'\033[31m{player}\033[0m'
    else:
        game_board[row][column] = f'\033[34m{player}\033[0m'


def check_if_win(player):  # Common for both games
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


def check_first_go():  # Common for both games
    while True:
        first_go = input('Please choose your marker - O / X | ')
        if first_go in ['O', 'X']:
            clear()
            return first_go


def define_mode(mode_=0):  # Common for both games
    while int(mode_) not in [1, 2]:
        mode_ = input('Please enter 1 for a play with computer or 2 - with another player | ')
    return int(mode_)


def get_user_number(player):  # Common for both games
    if not player == 'O':
        player = f'\033[34m{player}\033[0m'
    else:
        player = f'\033[31m{player}\033[0m'
    numb = input(f"{player} -\033[32m Player please enter a number | \033[0m")
    while numb not in [1, 2, 3, 4, 5, 6, 7, 8, 9] and numb not in game_board_available:
        numb = input(f"{player} -\033[32m Player please enter a VALID number |  \033[0m")
    return numb


def gener_numb_attack(symbol):  # Pertain to two players game (computer step generation_1)
    if symbol == 'X':
        symbol_ = f'\033[31mO\033[0m'
        symbol = f'\033[34mX\033[0m'
    else:
        symbol_ = f'\033[34mX\033[0m'
        symbol = f'\033[31mO\033[0m'
    times = 0
    free = []
    for range_ in for_check:
        first_, last_, step_ = range_
        for i in range(first_, last_, step_):
            row, column = convert_number_coord_(f'{i}')
            if game_board[row][column] == symbol:
                times += 1
            else:
                if game_board[row][column] != symbol_:
                    free.append(f'{i}')

            if times >= 2 and len(free) > 0:
                game_board_available.remove(f'{free[0]}')
                rn = f'{free[0]}'
                return rn
        free.clear()
        times = 0
    return gener_numb_defence(symbol, symbol_)


def gener_numb_defence(comp, my):  # Pertain to two players game (computer step generation_2)
    times = 0
    free = []
    for range_ in for_check:
        first_, last_, step_ = range_
        for i in range(first_, last_, step_):
            row, column = convert_number_coord_(f'{i}')
            if game_board[row][column] == my:
                times += 1
            else:
                if game_board[row][column] != comp:
                    free.append(f'{i}')
            if times == 2 and len(free) > 0:
                game_board_available.remove(f'{free[0]}')
                return f'{free[0]}'
        free.clear()
        times = 0
    if '5' in game_board_available and '1' and '3' and '7' and '9' not in game_board_available:
        game_board_available.remove('5')
        return '5'
    if game_board[1][0] == my and len(set(game_board_available).intersection({'1', '7'})) > 0:
        rn = choice(list(set(game_board_available).intersection({'1', '7'})))
    elif game_board[2][1] == my and len(set(game_board_available).intersection({'7', '9'})) > 0:
        rn = choice(list(set(game_board_available).intersection({'7', '9'})))
    elif game_board[1][2] == my and len(set(game_board_available).intersection({'3', '9'})) > 0:
        rn = choice(list(set(game_board_available).intersection({'3', '9'})))
    elif game_board[0][1] == my and len(set(game_board_available).intersection({'1', '3'})) > 0:
        rn = choice(list(set(game_board_available).intersection({'1', '3'})))
    elif len(set(game_board_available).intersection({'1', '3', '7', '9'})) > 0:
        rn = choice(list(set(game_board_available).intersection({'1', '3', '7', '9'})))
    else:
        rn = choice(list(game_board_available))
    game_board_available.remove(f'{rn}')
    return str(rn)


def game(first, num_of_players):  # Common for both games
    if first == 'X':
        second = 'O'
    else:
        second = 'X'
    show_game_board()
    counter = 0
    while True:
        player_f = get_user_number(player=first)
        coord = convert_number_coord(player_f)
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
        if num_of_players == 1:
            player_s = gener_numb_attack(second)

            coord = convert_number_coord_(player_s)
        else:
            player_s = get_user_number(player=second)
            coord = convert_number_coord(player_s)
        update_game_board(coord, f'{second}')
        counter += 1
        clear()
        show_game_board()
        if counter > 4:
            if check_if_win(f'{second}') != 0:
                break


# START OF EXECUTION
for_check = ((1, 10, 4), (3, 8, 2), (1, 8, 3), (2, 9, 3), (3, 10, 3), (1, 4, 1), (4, 7, 1), (7, 10, 1))  # Common for both games
game_board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]  # pertain to one player game
game_board_ = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]  # Pertain to two players game
game_board_available = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # Common for both games
if define_mode() == 1:
    step = check_first_go()
    game(step, 1)
    while True:
        a = input(f"\033[32mWould you like to continue? (Y/N) | \033[0m")
        clear()
        if a == 'Y':
            game_board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            game_board_available = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            game(step, 1)
        else:
            print('\033[32m    Bye\033[0m')
            break
else:
    step = check_first_go()
    game(step, 2)
    while True:
        a = input(f"\033[32mWould you like to continue? (Y/N) | \033[0m")
        clear()
        if a == 'Y':
            game_board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            game_board_available = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            game(step, 2)
        else:
            print('\033[32m    Bye\033[0m')
            break












