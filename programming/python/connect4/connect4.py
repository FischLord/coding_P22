# python game "4 winns" in shell
# 07.11.2022 Leon Kohlhaußen
# contributors Janneck Lehmann
from colorama import *
init(autoreset=True) #there is no need of reset every color effekt in the code duo this setting

# define the board
def board():
    print("+---+---+---+---+---+---+---+---+")
    print("| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |")
    print("+---+---+---+---+---+---+---+---+")
    print("| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |")
    print("+---+---+---+---+---+---+---+---+")
    print("| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |")
    print("+---+---+---+---+---+---+---+---+")
    print("| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |")
    print("+---+---+---+---+---+---+---+---+")
    print("| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |")
    print("+---+---+---+---+---+---+---+---+")
    print("| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |")
    print("+---+---+---+---+---+---+---+---+")
    print(Back.GREEN + "| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")



# welcome message when game is started
print("Welcome to 4wins!")
print("the rules:")
print("1. You can only place a stone in a column that is not full.")
print("2. You can only put a stone in the lowest row of a column. ")
print("3. You can only win if you have 4 stones in a row, column or diagonal.")
board()