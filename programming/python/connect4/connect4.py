# python game "4 wins/connect4/4 Gewinnt" in shell
# 07.11.2022 Leon Kohlhaußen
# contributors Janneck Lehmann

# <<<<<<<<<<< imports >>>>>>>>>>>>>>>>>
# https://hellocoding.de/blog/coding-language/python/farben-im-terminal
import random  # random module to start with a random player
from colorama import *
# there is no need of reset every color effekt in the code duo this setting
init(autoreset=True)


# <<<<<<<<<< variables >>>>>>>>>>>>>>>>>
gamenotover = True
players = ["🟡", "🔴"] 
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




# welcome message when game is started

def startMessage():
    print("Welcome to 4wins!")
    print("the rules:")
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
        print("you chose column", pickedField)
        try:
            pickedField = int(pickedField)
            if pickedField > 8 or pickedField < 1:
                print(Fore.RED + "please enter a number between 1 and 8")
            else:
                break
        except ValueError:
            print(Fore.RED + "please enter a number")


            


# player choose a column and the stone is placed in the lowest row of the column
def placeStone():
    for x in range(rows):
        if gameBoard[x][pickedField-1] == "🟡" or gameBoard[x][pickedField-1] == "🔴":
            gameBoard[x-1][pickedField-1] = players[0]
            print("choose another column")
            playerinput()
            break
        elif x == 5:
            gameBoard[x][pickedField-1] = players[0]
            break



# if the column is full the player has to choose another column


#check if the selected column is available
# def checkColumn():
#     if colum1[1]

#??????????? zweite liste paralel zur anzeigeliste muss erstellt werden, asbosnten muss symbol in die Liste eingesetzt werden


#player choose a column
def move():
    while gamenotover:
        playerinput()
        placeStone()
        switchPlayer()

# check if column is full and if not place a stone in the lowest row


# grid will be filled with the players color when this is an right move


# <<<<<<<<<<<<<<< wincheck >>>>>>>>>>>>>>>>>>

# check if the game is won
# check if a row is full
# check if a column is full
# check if a diagonal is full
# check if the game is a draw





startMessage()
randomPlayer()
printGameBoard()

while gamenotover:
    playerinput()
    placeStone()
    switchPlayer()
    printGameBoard()