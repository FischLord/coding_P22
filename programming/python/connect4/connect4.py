# python game "4 winns" in shell
# 07.11.2022 Leon Kohlhaußen
# contributors Janneck Lehmann


from colorama import * #https://hellocoding.de/blog/coding-language/python/farben-im-terminal
init(autoreset=True) #there is no need of reset every color effekt in the code duo this setting






#define the board as a list in a 8x8 matrix
def board():
    lf = "  " #lf = leeres feld
    grid = []
    for x in range(64):
        grid.append(lf)
    print("+----+----+----+----+----+----+----+----+")
    print("|",grid[0],"|",grid[1],"|",grid[2],"|",grid[3],"|",grid[4],"|",grid[5],"|",grid[6],"|",grid[7],"|")
    print("+----+----+----+----+----+----+----+----+")
    print("|",grid[8],"|",grid[9],"|",grid[10],"|",grid[11],"|",grid[12],"|",grid[13],"|",grid[14],"|",grid[15],"|")
    print("+----+----+----+----+----+----+----+----+")
    print("|",grid[16],"|",grid[17],"|",grid[18],"|",grid[19],"|",grid[20],"|",grid[21],"|",grid[22],"|",grid[23],"|")
    print("+----+----+----+----+----+----+----+----+")
    print("|",grid[24],"|",grid[25],"|",grid[26],"|",grid[27],"|",grid[28],"|",grid[29],"|",grid[30],"|",grid[31],"|")
    print("+----+----+----+----+----+----+----+----+")
    print("|",grid[32],"|",grid[33],"|",grid[34],"|",grid[35],"|",grid[36],"|",grid[37],"|",grid[38],"|",grid[39],"|")
    print("+----+----+----+----+----+----+----+----+")
    print("|",grid[40],"|",grid[41],"|",grid[42],"|",grid[43],"|",grid[44],"|",grid[45],"|",grid[46],"|",grid[47],"|")
    print("+----+----+----+----+----+----+----+----+")
    print("|",grid[48],"|",grid[49],"|",grid[50],"|",grid[51],"|",grid[52],"|",grid[53],"|",grid[54],"|",grid[55],"|")
    print("+----+----+----+----+----+----+----+----+")
    print("|",grid[56],"|",grid[57],"|",grid[58],"|",grid[59],"|",grid[60],"|",grid[61],"|",grid[62],"|",grid[63],"|")
    print(Back.GREEN + "| 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  |")


# check if the game is won
# check if a row is full
# check if a column is full
# check if a diagonal is full
# check if the game is a draw



# welcome message when game is started
print("Welcome to 4wins!")
print("the rules:")
print("1. You can only place a stone in a column that is not full.")
print("2. You can only put a stone in the lowest row of a column. ")
print("3. You can only win if you have 4 stones in a row, column or diagonal.")
board()