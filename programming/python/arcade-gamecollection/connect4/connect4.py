# python game "4 wins/connect4/4 Gewinnt" in shell
# 07.11.2022-10.11.2022 Leon Kohlhaußen
# contributors Janneck Lehmann

# <<<<<<<<<<< imports >>>>>>>>>>>>>>>>>
# https://hellocoding.de/blog/coding-language/python/farben-im-terminal
# https://www.geeksforgeeks.org/print-colors-python-terminal/

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
# Copyright (c) 2020-2022, Leon Kohlhaussen, contributors Janneck Lehmann
#
import time
import os
import random  # random module to start with a random player
from colorama import *  # colorama module to print colors in the terminal
# there is no need of reset every color effekt in the code duo this setting
init(autoreset=True)


# <<<<<<<<<< variables >>>>>>>>>>>>>>>>>
won = False             # variable to check if a player has won
players = ["🟡", "🔴"]  # player 1 is yellow and player 2 is red
gameBoard = [
            ["", "", "", "", "", "", ""],   #7 collumns and 6 rows
            ["", "", "", "", "", "", ""], 
            ["", "", "", "", "", "", ""], 
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""], 
            ["", "", "", "", "", "", ""]
            ]


rows = 6    #definiton of rows in the grid              ⬅️➡️
columns = 7    #definition of collumns in the grid      ⬆️⬇️

# print the board with given rows and columns
def printGameBoard():
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(" ", " |", end="")
        for y in range(columns):
            if (gameBoard[x][y] == "🟡"):               #if there is a yellow stone print yellow
                print("", gameBoard[x][y], end=" |")
            elif (gameBoard[x][y] == "🔴"):             #if there is a red stone print red
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")  #if there is no stone print empty
    print("\n   +----+----+----+----+----+----+----+")
    print("      1    2    3    4    5    6    7  \n", end="")





    #?? now we have coordinates for the gameboard and it is easy to check if a player has won
    #?? +3x or +3y or +3xy or -3xy


#welcome message when game is started
def startMessage():
    print("Welcome to 4wins!")
    print("The rules:")
    print("1. You can only place a stone in a column that is not full.")
    print("2. You can only put a stone in the lowest row of a column. ")
    print("3. You can only win if you have 4 stones in a row, column or diagonal.")

#set a random player to start the game
def randomPlayer():
    players[0] = random.choice(players)
    if players[0] == "🟡":
        print(Fore.YELLOW + "yellow starts")
    else:
        print(Fore.RED + "red starts")

#switching player after each move 
def switchPlayer():
    if players[0] == "🟡":
        players[0] = "🔴"
        print(Fore.RED + "red's turn")
    else:
        players[0] = "🟡"
        print(Fore.YELLOW + "yellow's turn")

# player input for column question and validation
def playerinput():
    while True:
        global pickedField
        print(Back.WHITE + " choose a column")
        pickedField = input(Fore.BLUE + ">>> ")
        try:
            pickedField = int(pickedField)
            if pickedField > 8 or pickedField < 1:
                print(Fore.RED + "please enter a number between 1 and 8")
            else:
                print("you chose column", pickedField)
                break
        except ValueError:
            print(Fore.RED + "please enter a number")
        except IndexError():
            print(Fore.RED + "please enter a number between 1 and 8")


            
# player choose a column and the stone is placed in the lowest row of the column if the column is full the player has to choose another column
def placeStone():
    for x in range(rows):
        if gameBoard[0][pickedField-1] == "🟡" or gameBoard[0][pickedField-1] == "🔴":
            print(Fore.RED + "this column is full, please choose another column")
            playerinput()
        elif gameBoard[x][pickedField-1] == "🟡" or gameBoard[x][pickedField-1] == "🔴":
            gameBoard[x-1][pickedField-1] = players[0]
            break
        elif x == 5:
            gameBoard[x][pickedField-1] = players[0]
            break
    
# <<<<<<<<<<<<<<< wincheck >>>>>>>>>>>>>>>>>>
        
# check if a row has 4 stones in a row return win true
def rowCheck():
    rowCheck = False
    for x in range(rows):
        for y in range(columns-3):
            if gameBoard[x][y] == gameBoard[x][y+1] == gameBoard[x][y+2] == gameBoard[x][y+3] == "🟡" or gameBoard[x][y] == gameBoard[x][y+1] == gameBoard[x][y+2] == gameBoard[x][y+3] == "🔴":
                return True


# check if a column has 4 stones in a row return win true
def columnCheck():
    columnCheck = False
    for x in range(rows-3):
        for y in range(columns):
            if gameBoard[x][y] == gameBoard[x+1][y] == gameBoard[x+2][y] == gameBoard[x+3][y] == "🟡" or gameBoard[x][y] == gameBoard[x+1][y] == gameBoard[x+2][y] == gameBoard[x+3][y] == "🔴":
                return True


# check if diagonal from left to right has 4 stones in a row return win true
def diagonalCheck1():
    diagonalCheck1 = False
    for x in range(rows-3):
        for y in range(columns-3):
            if gameBoard[x][y] == gameBoard[x+1][y+1] == gameBoard[x+2][y+2] == gameBoard[x+3][y+3] == "🟡" or gameBoard[x][y] == gameBoard[x+1][y+1] == gameBoard[x+2][y+2] == gameBoard[x+3][y+3] == "🔴":
                return True  


# check if diagonal from right to left has 4 stones in a row return win true
def diagonalCheck2():
    diagonalCheck2 = False
    for x in range(rows-3):
        for y in range(columns-3):
            if gameBoard[x][y+3] == gameBoard[x+1][y+2] == gameBoard[x+2][y+1] == gameBoard[x+3][y] == "🟡" or gameBoard[x][y+3] == gameBoard[x+1][y+2] == gameBoard[x+2][y+1] == gameBoard[x+3][y] == "🔴":
                return True

# check if the game is a draw
def drawCheck():
    drawCheck = False
    for x in range(rows):
        for y in range(columns):
            if gameBoard[x][y] == "🟡" or gameBoard[x][y] == "🔴":
                return True
def winVarCheck():
    drawCheck()
    diagonalCheck1()
    diagonalCheck2()
    columnCheck()
    rowCheck()

# check if the game is won and print the winner
def winCheck():
    global won
    winVarCheck()
    if rowCheck() == True or columnCheck() == True or diagonalCheck1() == True or diagonalCheck2() == True:
        if players[0] == "🟡":
            print(Fore.YELLOW + "yellow won")
        else:
            print(Fore.RED + "red won")
        won = True
    else:
        won = False

#not finished yet
def mainGame():
    os.system("cls")
    startMessage()
    randomPlayer()
    printGameBoard()
    while True:
        playerinput()
        placeStone()
        winCheck()
        printGameBoard()
        if won == True:
            print("game over")
            break
        if drawCheck() == False:
            print(Fore.RED + "draw")
            break
        switchPlayer()

mainGame()
