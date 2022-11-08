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
player = "player1"      
possibleLetters = ["1", "2", "3", "4", "5", "6", "7"]
gameBoard = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], [
    "", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]


rows = 6    #definiton of rows in the grid              ⬅️➡️
columns = 7    #definition of collumns in the grid      ⬆️⬇️

# print the board with given rows and columns


def printGameBoard():
    print("\n     1    2    3    4    5    6    7  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(columns):
            if (gameBoard[x][y] == "🔵"):
                print("", gameBoard[x][y], end=" |")
            elif (gameBoard[x][y] == "🔴"):
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

    #?? now we have coordinates for the gameboard and it is easy to check if a player has won
    #?? +3x or +3y or +3xy or -3xy




# welcome message when game is started

def startMessage():
    print("Welcome to 4wins!")
    print("the rules:")
    print("1. You can only place a stone in a column that is not full.")
    print("2. You can only put a stone in the lowest row of a column. ")
    print("3. You can only win if you have 4 stones in a row, column or diagonal.")


# define the board as a list in a 8x8 matrix
#def board():
#    lf = " 🔴 "  # lf = leeres feld

#create list for the 8x8 gameboard
#def createGrid():
#    lf = "  " #lf = leeres feld
#    global grid
#    grid = []
#    for x in range(64):
#        grid.append(lf)



# #upddate every single column after each move
# def updateColumn():
#     global colum1, colum2, colum3, colum4, colum5, colum6, colum7, colum8
#     colum1 = [grid[0],grid[8],grid[16],grid[24],grid[32],grid[40],grid[48],grid[56]]
#     colum2 = [grid[1],grid[9],grid[17],grid[25],grid[33],grid[41],grid[49],grid[57]]
#     colum3 = [grid[2],grid[10],grid[18],grid[26],grid[34],grid[42],grid[50],grid[58]]
#     colum4 = [grid[3],grid[11],grid[19],grid[27],grid[35],grid[43],grid[51],grid[59]]
#     colum5 = [grid[4],grid[12],grid[20],grid[28],grid[36],grid[44],grid[52],grid[60]]
#     colum6 = [grid[5],grid[13],grid[21],grid[29],grid[37],grid[45],grid[53],grid[61]]
#     colum7 = [grid[6],grid[14],grid[22],grid[30],grid[38],grid[46],grid[54],grid[62]]
#     colum8 = [grid[7],grid[15],grid[23],grid[31],grid[39],grid[47],grid[55],grid[63]]



# #shows the gameboard and refreshes the colums after each move
# def board():
#     print("+----+----+----+----+----+----+----+----+")
#     print("|", grid[0], "|", grid[1], "|", grid[2], "|", grid[3],
#           "|", grid[4], "|", grid[5], "|", grid[6], "|", grid[7], "|")
#     print("+----+----+----+----+----+----+----+----+")
#     print("|", grid[8], "|", grid[9], "|", grid[10], "|", grid[11],
#           "|", grid[12], "|", grid[13], "|", grid[14], "|", grid[15], "|")
#     print("+----+----+----+----+----+----+----+----+")
#     print("|", grid[16], "|", grid[17], "|", grid[18], "|", grid[19],
#           "|", grid[20], "|", grid[21], "|", grid[22], "|", grid[23], "|")
#     print("+----+----+----+----+----+----+----+----+")
#     print("|", grid[24], "|", grid[25], "|", grid[26], "|", grid[27],
#           "|", grid[28], "|", grid[29], "|", grid[30], "|", grid[31], "|")
#     print("+----+----+----+----+----+----+----+----+")
#     print("|", grid[32], "|", grid[33], "|", grid[34], "|", grid[35],
#           "|", grid[36], "|", grid[37], "|", grid[38], "|", grid[39], "|")
#     print("+----+----+----+----+----+----+----+----+")
#     print("|", grid[40], "|", grid[41], "|", grid[42], "|", grid[43],
#           "|", grid[44], "|", grid[45], "|", grid[46], "|", grid[47], "|")
#     print("+----+----+----+----+----+----+----+----+")
#     print("|", grid[48], "|", grid[49], "|", grid[50], "|", grid[51],
#           "|", grid[52], "|", grid[53], "|", grid[54], "|", grid[55], "|")
#     print("+----+----+----+----+----+----+----+----+")
#     print("|", grid[56], "|", grid[57], "|", grid[58], "|", grid[59],
#           "|", grid[60], "|", grid[61], "|", grid[62], "|", grid[63], "|")
#     print("+----+----+----+----+----+----+----+----+")
#     print(Back.GREEN + "| 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  |")




#switching player after each move 
def switchPlayer():
    global player
    if player == "player1":
        player = "player2"
    else:
        player = "player1"

# player input for column question and validation


def playerinput():
    while True:
        print(Back.WHITE + player + " choose a column")
        column = input(Fore.BLUE + ">>> ")
        try:
            column = int(column)
            if column > 8 or column < 1:
                print(Fore.RED + "please enter a number between 1 and 8")
            else:
                break
        except ValueError:
            print(Fore.RED + "please enter a number")

# player choose a column


#check if the selected column is available
# def checkColumn():
#     if colum1[1]

#??????????? zweite liste paralel zur anzeigeliste muss erstellt werden, asbosnten muss symbol in die Liste eingesetzt werden


#player choose a column
def move():
    while gamenotover:
        playerinput()
        switchPlayer()

# check if column is full and if not place a stone in the lowest row


# grid will be filled with the players color when this is an right move


# <<<<<<<<<<<<<<< wincheck >>>>>>>>>>>>>>>>>>

# check if the game is won
# check if a row is full
# check if a column is full
# check if a diagonal is full
# check if the game is a draw


