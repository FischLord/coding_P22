# python game "4 wins/connect4/4 Gewinnt" in shell
# 07.11.2022 Leon Kohlhaußen
# contributors Janneck Lehmann

# <<<<<<<<<<< imports >>>>>>>>>>>>>>>>>
import os                   # os for cleanup the shell
import random               # random module to start with a random player
from colorama import *      # https://hellocoding.de/blog/coding-language/python/farben-im-terminal
init(autoreset=True)        # there is no need of reset every color effekt in the code duo this setting



# <<<<<<<<<< variables >>>>>>>>>>>>>>>>>
gamenotover = True
player = ("🔴")
lf = ""   
possibleLetters = ["1", "2", "3", "4", "5", "6", "7"]
gameBoard = [[lf, lf, lf, lf, lf, lf, lf], [lf, lf, lf, lf, lf, lf, lf], [lf, lf, lf, lf, lf, lf, lf], [
    lf, lf, lf, lf, lf, lf, lf], [lf, lf, lf, lf, lf, lf, lf], [lf, lf, lf, lf, lf, lf, lf]]
rows = 6                    #definiton of rows in the grid              ⬅️➡️
columns = 7                 #definition of collumns in the grid      ⬆️⬇️

# print the board with given rows and columns in an coordinate system
def printGameBoard():
    os.system("cls") 
    print("\n     1    2    3    4    5    6    7  ", end=lf)
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x + 1, " |", end=lf)
        for y in range(columns):
            if (gameBoard[x][y] == "🔵"):
                print(" ", gameBoard[x][y], end=" |")
            elif (gameBoard[x][y] == "🔴"):
                print(" ", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")


# start with a random player
def randomPlayer():
    global player
    player = random.choice(player)

#switching player after each move 
def switchPlayer():
    if player == "🔴":
        player = "🟡"
    else:
        player = "🔴"
        
# welcome message when game is started
def startMessage():
    print("Welcome to 4wins!")
    print("the rules:")
    print("1. You can only place a stone in a column that is not full.")
    print("2. You can only put a stone in the lowest row of a column. ")
    print("3. You can only win if you have 4 stones in a row, column or diagonal.")
    print(player + " starts the game")




# player input for column question and validation
def playerinput():
    global column
    while True:
        print(Back.WHITE + player + " choose a column")
        column = input(Fore.BLUE + ">>> ")
        try:
            column = int(column)
            if column > 8 or column < 1:
                print(Fore.RED + "please enter a number between 1 and 8")
            else:
                if checkColumFull():
                    continue
                else:
                    set(column)
        except ValueError:
            print(Fore.RED + "please enter a number")

#check if the selected column is available
def checkColumFull():
    if gameBoard[column - 1][0] != lf:
        print(Fore.RED + "this column is full")
        return True

#player choose a column
def move():
    while gamenotover:
        printGameBoard()
        playerinput()
        switchPlayer()

#place a stone in the choosen column at the lowest row
def set(xcolumn):
    for x in range (rows):
        if not gameBoard[xcolumn -1] == lf:
            gameBoard[xcolumn -1][x-1] = player
            finished = True
            break
    if not finished:
        gameBoard[xcolumn -1][6] = player
    print("stone placed")
# grid will be filled with the players color when this is an right move


# <<<<<<<<<<<<<<< wincheck >>>>>>>>>>>>>>>>>>

# check if the game is won
# check if a row is full
# check if a column is full
# check if a diagonal is full
# check if the game is a draw

move()