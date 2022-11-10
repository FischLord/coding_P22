# janneck lehmann - 10.11.2022
# co author: leon kohlhaußen - 10.11.2022
# game collection menu/overlay

# import modules
import time
import os


# main menu
def mainMenu():
    # print big ASCII art
    print("           _____   _____          _____  ______ ")
    print("     /\   |  __ \ / ____|   /\   |  __ \|  ____|")
    print("    /  \  | |__) | (___    /  \  | |__) | |__   ")
    print("   / /\ \ |  _  /| |      / /\ \ | |  | |  __|  ")
    print("  / ____ \| | \ \| |____ / ____ \| |__| | |____ ")
    print(" /_/    \_\_|  \_\\_____/_/    \_\_____/|______|")
    print("                                                ")
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
            print("there is currently no statistics")
            # wait 2 seconds and then go back to the menu
            time.sleep(2)
            mainMenu()
        elif mainMenuAnswer == 3:
            print("there is currently no account")
            # wait 2 seconds and then go back to the menu
            time.sleep(2)
            mainMenu()
        elif mainMenuAnswer == 4:
            print("there is currently no game collection")
            # wait 2 seconds and then go back to the menu
            time.sleep(2)
            mainMenu()
        elif mainMenuAnswer == 5:
            print("there is currently no game collection on github")
            # wait 2 seconds and then go back to the menu
            time.sleep(2)
            mainMenu()
        elif mainMenuAnswer == 6:
            print("thank you for playing")
            exit()
        else:
            print("invalid input")
            # wait 2 seconds and then go back to the menu
            time.sleep(2)
            mainMenu()
    except:
        print("invalid input")
        # wait 2 seconds and then go back to the menu
        time.sleep(2)
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


def login():
    print("Please enter your username")
    username = input(">>> ")
    print("Please enter your password")
    password = input(">>> ")

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

# main function


def main():
    welcomeMessage()
    howManyPlayers()
    playerAccountQuestion()
    chooseGame()


mainMenu()
