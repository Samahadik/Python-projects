# -*- coding: utf-8 -*-
"""Snake_dice game

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wyLqQbfYazYgNRQPfQIFwrlwK0CLAXnL
"""

import random

ladder={2:23,6:45,20:59,52:72,57:96,71:92}
snake={43:17,50:5,56:8,73:15,84:58,87:49,98:40}

pos1=0
pos2=0

def movement(pos):
    dice=random.randint(1,6)
    print('Dice:{}'.format(dice))
    pos=pos+dice
    if pos in ladder:
       print('climbed by ladder')
       pos=ladder[pos]
       print('position:{}'.format(pos))
    elif pos in snake:
       print('bitten by snake')
       pos=snake[pos]
       print('pos:{}'.format(pos))
    else:
       print('position:{}'.format(pos))
    print('\n')
    return pos
while True:
     a=input("player 1 enter 'a' to throw dice:")
     pos1=movement(pos1)
     if pos1>=100:
       print("game over!!!,\n player 1 won the game")
       break
     b=input("player2 enter'b' to throw dice:")
     pos2=movement(pos2)
     if pos2>=100:
        print("Game Over!!! \n Player 2 won the game")
        break

#################complete############





