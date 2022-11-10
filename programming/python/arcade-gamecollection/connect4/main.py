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
    global amountPlayer
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
    for x in range(amountPlayer):
        print("Player", x+1, "do you have an account, or do you want to play as a guest?")
        print("1. I have an account")
        print("2. I want to create an account")
        print("3. I want to play as a guest")
        playerAnswer = input(">>> ")
        try:
            playerAnswer = int(playerAnswer)
            if not playerAnswer in range(1,4):
                print("Please enter a number between 1 and 3!")
                playerAccountQuestion()
            elif playerAnswer == 1:
                login()
            elif playerAnswer == 2:
                register()
            elif playerAnswer == 3:
                chooseName()
            
        except ValueError:
            print("Please enter a number!")
            playerAccountQuestion()

def login():
    print("Please enter your username")
    username = input(">>> ")
    print("Please enter your password")
    password = input(">>> ")


def register():
    print("Please enter your username")
    username = input(">>> ")
    print("Please enter your password")
    password = input(">>> ")
    print("Please enter your password again")
    password2 = input(">>> ")
    if password == password2:
        pass
    else:
        print("Your passwords don't match!")
        register()


def chooseName():
    print("Please enter your name")
    nameGuest = input(">>> ")
    print("Your name is", nameGuest)


# choose game based on the current amount of players
def chooseGame():
    print("Please choose a game from the list below.")
    if amountPlayer == 1:
        pass
    elif amountPlayer == 2:
        pass
    elif amountPlayer == 3:
        pass
    elif amountPlayer == 4:
        pass
    elif amountPlayer == 5:
        pass


