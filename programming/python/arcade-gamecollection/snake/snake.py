# python game "Snake" in shell
# 10.11.2022 Leon Kohlhaußen

# <<<<<<<<<<< imports >>>>>>>>>>>>>>>>>
# https://hellocoding.de/blog/coding-language/python/farben-im-terminal
# https://www.geeksforgeeks.org/print-colors-python-terminal/

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
# Copyright (c) 2020-2022, Leon Kohlhaussen, contributors Janneck Lehmann
#
import time
import os
import curses
import random  # random module to start with a random player
from colorama import *  # colorama module to print colors in the terminal
# there is no need of reset every color effekt in the code duo this setting
init(autoreset=True)

# <<<<<<<<<< variables >>>>>>>>>>>>>>>>>
gameOver = False             # variable to check if a player has won
snakeLength = 1
snakeHead = [0, 0]
snakeBody = [snakeHead]
food = (", ")
score = 0
speed = 1


# <<<<<<<<<< functions >>>>>>>>>>>>>>>>>

# game field with high and width
def gameField():
    screen = curses.initscr()
    screen.keypad(True)
    screen.border(0)
    screen.addstr(0, 2, "Score: " + str(score) + " ")
    screen.addstr(0, 27, " SNAKE ")
    screen.timeout(150)
    return screen


# <<<<<<<<<< main >>>>>>>>>>>>>>>>>


# <<<<<<<<<< end >>>>>>>>>>>>>>>>>


gameField()
