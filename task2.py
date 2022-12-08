# Создайте программу для игры в ""Крестики-нолики"".(в консоли происходит выбор позиции)

import os

res = [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22'],
       ['00', '10', '20'], ['01', '11', '21'], ['02', '12', '22'],
       ['00', '11', '22'], ['20', '11', '02']]
vin = False
board = [' ', 'O', '1', '2']
desk = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def gameBot(res, vin, board, desk):
    if vin == False:
        draw_board(board)
        player = AI()
        print(AI())
        x = int(player[0])
        y = int(player[1])

        desk[x][y] = '0'
        draw_board(board)
        for i in range(len(res)):
            for j in range(len(res[i])):
                if res[i][j] == player:
                    res[i][j] = '0'
        tmp = ['0', '0', '0']
        for i in range(len(res)):
            if res[i] == tmp:
                draw_board(board)
                print('Ура! SkyNet выиграл!')
                vin = True
    return vin


def AI():

    step = ""

    step = check_line(2, 0)

    if step == "":
        step = check_line(0, 2)

    if step == "":
        step = check_line(1, 0)

    if step == "":
        if desk[1][1] != "x" and desk[1][1] != "0":
            step = '11'

    if step == "":
        if desk[0][0] != "x" and desk[0][0] != "0":
            step = '00'

    return step


def check_line(sum_O, sum_X):

    step = ""
    for i in range(8):
        o = 0
        x = 0

        for j in range(3):
            if res[i][j] == "0":
                o += 1
            if res[i][j] == "x":
                x += 1

            if o == sum_O and x == sum_X:
                for m in range(3):
                    if res[i][m] != "0" and res[i][m] != "x":
                        step = res[i][m]
    return step


def draw_board(board):
    def clear(): return os.system('cls')
    clear()
    print("-----------------")
    print("|", ' ', "|", board[1], "|", board[2], "|", board[3], "|")
    print("-----------------")

    for i in range(3):
        print("|", board[i+1], "|", desk[i][0],
              "|", desk[i][1], "|", desk[i][2], "|")
        print("-----------------")


def game(res, vin, board, desk, user, symbol):
    if vin == False:
        draw_board(board)
        player = input(f'Игрок {user}! Введите координаты ячейки  ')
        x = int(player[0])
        y = int(player[1])
        while desk[x][y] != ' ':
            draw_board(board)
            player = input(
                'Ячейка занята ! Введите координаты  другой ячейки  ')
            x = int(player[0])
            y = int(player[1])
        desk[x][y] = symbol
        draw_board(board)
        for i in range(len(res)):
            for j in range(len(res[i])):
                if res[i][j] == player:
                    res[i][j] = symbol
        tmp = [symbol, symbol, symbol]
        for i in range(len(res)):
            if res[i] == tmp:
                draw_board(board)
                print(f'Ура! Игрок{user} выиграл!')
                vin = True
    return vin


for i in range(4):
    vin = game(res, vin, board, desk, 1, 'x')
    # vin = game(res, vin, board, desk, 2, '0')   # Активируйте,чтоб включить 2 игрока
    vin = gameBot(res, vin, board, desk)
    if vin == True:
        break
else:
    draw_board(board)
    print('!!! Ничья !!!')
