# janneck lehmann - 11.11.2022
# co author: leon kohlhaußen - 11.11.2022
# tic-tac-toe game for "the game collection"

import random

player1 = "test"
player2 = "test2"

# create and print playground of an 3x3 tic-tac-toe game filled with numbers
def createPlayground():
    global playground
    playground = [[1,2,3],[4,5,6],[7,8,9]]
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

#asks player how much wins does one player need to win the game
def askPlayerHowManyWins():
    global wins
    wins = input("How many wins does one player need to win the game? ")
    try:
        wins = int(wins)
        if wins > 0 and wins < 10:
            print("The game will be played until one player has", wins, "wins.")
        else:
            print("Please enter a number between 1 and 9")
            askPlayerHowManyWins()
    except ValueError:
        print("Please enter a number")
        askPlayerHowManyWins()





#player names needs to be read from the function call, her names need to be set
def playerNames(p1name,p2name):
    global player1Name, player2Name
    player1Name = p1name
    player2Name = p2name

def randomBegin():
    global player1symbol, player2symbol, currentPlayer
    begin = random.randint(1,2)
    if begin == 1:
        player1symbol = "X"
        player2symbol = "O"
        currentPlayer = player1Name
    else:
        player1symbol = "O"
        player2symbol = "X"
        currentPlayer = player2Name

#switch between player 1 and player 2 after each turn
def switchPlayer():
    global currentPlayer
    if currentPlayer == player1Name:
        currentPlayer = player2Name
    else:
        currentPlayer = player1Name


#check if the number is available and not already taken
#place the symbol of the player on the playground on the chosen number
#player chooses a number between 1 and 9
def playerTurn():
    global playground
    print(f"{currentPlayer} it's your turn")
    print("Choose a number between 1 and 9")
    turn = input(">>> ")
    try:
        turn = int(turn)
        if turn > 0 and turn < 10:
            if turn == 1:
                if playground[0][0] == 1:
                    playground[0][0] = currentPlayer
                else:
                    print("This field is already taken")
                    playerTurn()
            elif turn == 2:
                if playground[0][1] == 2:
                    playground[0][1] = currentPlayer
                else:
                    print("This field is already taken")
                    playerTurn()
            elif turn == 3:
                if playground[0][2] == 3:
                    playground[0][2] = currentPlayer
                else:
                    print("This field is already taken")
                    playerTurn()
            elif turn == 4:
                if playground[1][0] == 4:
                    playground[1][0] = currentPlayer
                else:
                    print("This field is already taken")
                    playerTurn()
            elif turn == 5:
                if playground[1][1] == 5:
                    playground[1][1] = currentPlayer
                else:
                    print("This field is already taken")
                    playerTurn()
            elif turn == 6:
                if playground[1][2] == 6:
                    playground[1][2] = currentPlayer
                else:
                    print("This field is already taken")
                    playerTurn()
            elif turn == 7:
                if playground[2][0] == 7:
                    playground[2][0] = currentPlayer
                else:
                    print("This field is already taken")
                    playerTurn()
            elif turn == 8:
                if playground[2][1] == 8:
                    playground[2][1] = currentPlayer
                else:
                    print("This field is already taken")
                    playerTurn()
            elif turn == 9:
                if playground[2][2] == 9:
                    playground[2][2] = currentPlayer
                else:
                    print("This field is already taken")
                    playerTurn()
        else:
            print("Please enter a number between 1 and 9")
            playerTurn()
    except ValueError:
        print("Please enter a number between 1 and 9")

#check if there are 3 symbols in a row

def checkRow():
    global playground
    for i in range(0,3):
        if playground[i][0] == playground[i][1] == playground[i][2]:
            return True
    return False

#check if there are 3 symbols in a column

def checkColumn():
    global playground
    for i in range(0,3):
        if playground[0][i] == playground[1][i] == playground[2][i]:
            return True
    return False

#check if there are 3 symbols in a diagonal

def checkDiagonal():
    global playground
    for i in range(0,3):
        if playground[i][0] == playground[i][1] == playground[i][2]:
            return True
        if playground[0][i] == playground[1][i] == playground[2][i]:
            return True
    return False




#check if a player has won the game
def playerWon():
    if checkRow() or checkColumn() or checkDiagonal():
        print(f"{currentPlayer} has won the game")
        return True
    return False
#check if the game is a draw


#main function with the game logic
def main(player1,player2):
    askPlayerHowManyWins()
    createPlayground()
    playerNames(player1,player2)
    randomBegin()
    print("Welcome to the tic-tac-toe game")
    print("The game will begin now")
    print("The player who begins is chosen randomly")
    if player1symbol == "X":
        print(f"{player1Name} begins with the symbol",player1symbol)
    else:
        print(f"{player2Name} begins with the symbol",player2symbol)
    


main(player1,player2)