# janneck lehmann - 10.11.2022
# co author: leon kohlhaußen - 10.11.2022
# game collection menu/overlay

# import modules
import time
import os


# main menu
def mainMenu():
    os.system('cls')
    # print big ASCII art
    print("            _____    _____            _____   ______ ")
    print("     /\    |  __ \  / ____|    /\    |  __ \ |  ____|")
    print("    /  \   | |__) || |        /  \   | |  | || |__   ")
    print("   / /\ \  |  _  / | |       / /\ \  | |  | ||  __|  ")
    print("  / ____ \ | | \ \ | |____  / ____ \ | |__| || |____ ")
    print(" /_/    \_\|_|  \_\ \_____|/_/    \_\|_____/ |______|")
    print("                                                     ")
    print("Welcome to the main menu")
    print("1. Play a game")
    print("2. View your statistics")
    print("3. View your account")
    print("4. View the game collection")
    print("5. View the game collection on github")
    print("6. Exit the game collection")
    mainMenuAnswer = input(">>> ")
    try:
        mainMenuAnswer = int(mainMenuAnswer)
        if mainMenuAnswer == 1:
            main()
        elif mainMenuAnswer == 2:
            viewStatistics()
        elif mainMenuAnswer == 3:
            viewAccount()
        elif mainMenuAnswer == 4:
            viewGameCollection()
        elif mainMenuAnswer == 5:
            viewGithub()
        elif mainMenuAnswer == 6:
            exit()
    except ValueError:
        print("Please enter a number!")
        mainMenu()

# welcome message


def welcomeMessage():
    print("Welcome to the Acade Game Collection")
    print()
    print("This collection is developed by:")
    name = "Janneck Lehmann"
    target = "https://www.github.com/FischLord"
    print(f"\u001b]8;;{target}\u001b\\{name}\u001b]8;;\u001b\\")
    name1 = "Leon Kohlhaußen"
    target1 = "https://www.github.com/LeonKohli"
    print(f"\u001b]8;;{target1}\u001b\\{name1}\u001b]8;;\u001b\\")
    print()
    print("If you want to see more information about the game collection, please visit our github page \nor type 'help' in the console.")
# help messages with list of commands and their description

# how many players?


def howManyPlayers():
    global amountPlayer
    print("\n\nHow many players do you want to play with?")
    amountPlayer = input(">>> ")
    try:
        amountPlayer = int(amountPlayer)
        print("You are playing with", amountPlayer, "players.")
        return amountPlayer
    except ValueError:
        print("Please enter a number!")
        howManyPlayers()
    except IndexError():
        print(Fore.RED + "please enter a number between 1 and 5")
        howManyPlayers()


# does all player got an account or is it a guest?


def playerAccountQuestion():
    for x in range(amountPlayer):
        print("Player", x+1,
              "do you have an account, or do you want to play as a guest?")
        print("1. I have an account")
        print("2. I want to create an account")
        print("3. I want to play as a guest")
        playerAnswer = input(">>> ")
        try:
            playerAnswer = int(playerAnswer)
            if playerAnswer == 1:
                login()
            elif playerAnswer == 2:
                register()
            elif playerAnswer == 3:
                chooseName()
        except ValueError:
            print("Please enter a number!")
            playerAccountQuestion()
        except IndexError():
            print(Fore.RED + "please enter a number between 1 and 3")

# make it possible to tik an answer with arrow keys

# player login

# dont print the password in the console when typing it in


def login():
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
        login()

# player register


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

# player choose name


def chooseName():
    print("Please enter your name")
    nameGuest = input(">>> ")
    print("Your name is", nameGuest)

# check if the name is already taken


# main menu thing

# choose game based on the current amount of players
def chooseGame():
    print("Please choose a game from the list below.")
    if amountPlayer == 1:
        print("there is currently no game for one player")
        # wait 2 seconds and then go back to the menu
        time.sleep(2)
        mainMenu()
    elif amountPlayer == 2:
        print("1. Connect 4")
        print("2. Tic Tac Toe")
    elif amountPlayer == 3:
        print("there is currently no game for three players")
    elif amountPlayer == 4:
        print("there is currently no game for four players")
    elif amountPlayer == 5:
        print("there is currently no game for five players")


def viewStatistics():
    print("there is currently no statistics")
    # wait 2 seconds and then go back to the menu
    time.sleep(2)
    mainMenu()


def viewAccount():
    print("your account:")
    print("username: ", username)
    print("password: ", password)
    # type exit to go back to the menu
    print("\nType exit to go back to the menu")
    exit = input(">>> ")
    if exit == "exit":
        mainMenu()
    else:
        print("invalid input")
        viewAccount()


def viewGameCollection():
    print("currntly there are theses games in the collection:")
    print("1. Connect 4")
    print("2. Tic Tac Toe")
    # type exit to go back to the menu
    print("\nType exit to go back to the menu")
    exit = input(">>> ")
    if exit == "exit":
        mainMenu()
    else:
        print("invalid input")
        viewGameCollection()


def viewGithub():
    print("the game collection is on github")
    print("the link is:")
    target = "https://github.com/FischLord/coding_P22/tree/main/programming/python/arcade-gamecollection"
    print(f"\u001b]8;;{target}\u001b\\{target}\u001b]8;;\u001b\\")
    # type exit to go back to the menu
    print("\nType exit to go back to the menu")
    exit = input(">>> ")
    if exit == "exit":
        mainMenu()
    else:
        print("invalid input")
        viewGithub()


def exit():
    print("thank you for playing")
    exit()

# type help anywhere to get a list of commands and their description


def help():
    help = input(">>> ")
    if help == "help":
        print("help")
        print("this is a list of commands and their description")
        print("help - this command")
        print("exit - exit the game")
        print("view statistics - view the statistics")
        print("view account - view your account")
        print("view game collection - view the game collection")
        print("view github - view the github page")
        print("play - play a game")
        print("main menu - go back to the main menu")
        print("how many players - choose how many players you want to play with")
        print("player account question - does all player got an account or is it a guest?")
        print("login - player login")
        print("register - player register")
        print("choose name - player choose name")
        print("choose game - choose game based on the current amount of players")


# main function


def main():
    welcomeMessage()
    howManyPlayers()
    playerAccountQuestion()
    chooseGame()


mainMenu()
