# -*- coding: utf-8 -*-
"""RockPaperScissors-Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yefpN7fnmKRAgqUHbsznEgcszqnrXwp0
"""

#This is RockPaperScissors game,where we will have 3 conditions
#1)Rock wins against Scissors
#2)Scissors win against Paper
#3)Paper wins against Rock

import random

user_choice=int(input('Enter your choice: enter 0 for Rock,enter 1 for Paper,enter 2 for Scissors:'))
if user_choice>=3 or user_choice<0:
  print("you entered invalid number,you lost the game")
else:
  computer_choice=random.randint(0,2)
  print("computer choice",computer_choice)
  if computer_choice==user_choice:
      print("it's a draw")
  elif computer_choice<user_choice:
      print('Congratulations,you won the game!!!')
  elif computer_choice>user_choice:
      print('unfortunately ,you lost the game.')
  elif computer_choice==0 and user_choice==2:
      print('unfortunately ,you lost the game.')
  elif computer_choice==2 and user_choice==0:
      print('Congratulations,you won!!!')

###########complete##########

