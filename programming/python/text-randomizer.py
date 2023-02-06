# Lehmann Janneck, 06.02.2023
# Programm randomizes an specific amount of Sselfinserted strings

import random
import os

#? ================= Custome Settings =================

# fill this list to properly use the existing list mode
exsistingStrings = [
        # enter your strings here in the following format ["xxxx",]
        "string1",
        "string2",
        "string3",
        "string4",
    ]



# 0 asks you every Time if you want to use an existing list or self input strings
# 1 uses an existing list
# 2 self inputs strings 
defaultMode = 0


#? ================= Custome Settings =================





# little credits function for the startup
def credits():
    os.system("cls")
    print("")
    print("Text Randomizer by Lehmann Janneck")
    print("Version 1.1a")
    print("")
    print("")
    print("")

# Ask for the amotunt of strings to randomize
def numberOfStrings():
    global number
    while True:
        try:
            number = int(input("How many strings do you want to randomize? > "))
            if number > 0:
                return number
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a number.")

# input the strings
def inputStrings(number):
    global strings
    strings = []
    for i in range(number):
        strings.append(input("Enter string " + str(i + 1) + " > "))
    # check if entered strings empty strings and delete them
    for i in range(number):
        if strings[i] == "":
            strings.remove(strings[i])

# print one random string
def randomizeStrings(strings):
    credits()
    print("")
    print("")
    print("Randomized string: " + random.choice(strings))
    print("")
    print("")

# selfInputMode function
def selfInputMode():
    numberOfStrings()
    inputStrings(number)
    randomizeStrings(strings)
        

def useExistingList():
    randomizeStrings(exsistingStrings)




#! main program
nextRound = True
while nextRound == True:
    if defaultMode == 0:
        print("Do you want to use an existing list of strings or do you want to self input strings?")
        print("1. Use existing list")
        print("2. Self input strings")
        choice = input("> ")
        try:
            choice = int(choice)
            if choice == 1:
                useExistingList()
            elif choice == 2:
                selfInputMode()
        except ValueError:
            print("Please enter a number.")
    elif defaultMode == 1:
        useExistingList()
    elif defaultMode == 2:
        selfInputMode()
    nextRoundChoice = True
    while nextRoundChoice == True:
                    nextRound = input("Do you want to randomize another string? (y/n) ")
                    if nextRound == "y":
                        nextRound = True
                        nextRoundChoice = False
                        os.system("cls")
                    elif nextRound == "n":
                        nextRound = False
                        nextRoundChoice = False 
                    else:
                        print("Please enter 'y' or 'n'.")
                        nextRoundChoice = True
    


