#  Создайте программу для игры с конфетами человек против человека.
#  Условие задачи: На столе лежит 117 конфет. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход.

import random
import os

candies = 117
clear = lambda: os.system('cls')
clear()

while candies > 0:
    print(f'Общее количество конфет  ', candies)
    player = int(input('Какое количество конфет,от 1 до 28,вы возьмёте?  '))
    clear = lambda: os.system('cls')
    clear()
    while player < 1 or player > 28:
        player = int(input('Количество конфет должно быть от 1 до 28 !!!  '))
        clear = lambda: os.system('cls')
        clear()
    candies -= player
    if candies == 0:
        print('Вам сегодня везет !')
    elif candies > 0:
        x = candies % 29
        
        if x == 0:
            x = random.randint(1, 28)
            print(f'Крупье забирает ', x)
            candies -= x
        else:
            print(f'Крупье забирает ', x)
            candies -= x
            if candies == 0:
                print('Казино опять в плюсе !')
