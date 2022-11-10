# janneck lehmann - 10.11.2022
# game collection menu/overlay






# welcome message
def welcomeMessage():
    print("Welcome to the Acade Game Collection")
    print("")
    print("This collection is developed by Leon Kohlhaußen and Janneck Lehmann")
    print("If you want to see more information about the game collection, please visit our github page or type 'help' in the console.")
# help messages with list of commands and their description    
# how many players?
def howManyPlayers():
    print("How many players do you want to play with?")
    amountPlayer = input(">>> ")
    try:
        amountPlayer = int(amountPlayer)
        if amountPlayer > 5:
            print("You can only play with 5 players maximum.")
            howManyPlayers()
        elif amountPlayer < 1:
            print("You can only play with 1 player minimum.")
            howManyPlayers()
        else:
            print("You are playing with", amountPlayer, "players.")
            return amountPlayer
    except ValueError:
        print("Please enter a number!")
        howManyPlayers()

# does all player got an account or is it a guest?
def playerAccountQuestion():
    print("Do all players have an account, or do you want to continue as a guest?")
    
# if not an guest, login
# choose game based on the current amount of players



howManyPlayers()