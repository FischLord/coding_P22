# janneck lehmann - 10.11.2022
# co author: leon kohlhaußen - 10.11.2022
# login modul for "the game collection"

import os

def login(username,password):
    txt = open(os.path.dirname(os.path.abspath(__file__))+"/accountinfo.txt", "r")
    for line in txt:
        line = line.split(",")
        if username == line[0] and password == line[1]:
            print("You have successfully logged in!")
            return True
        else:
            print("Your username or password is incorrect!")
            return False


def register():
    global username,password,email
    print("Please enter your username")
    username = input(">>> ")
    if checkUsername(username):
        print("This username is already taken")
        print("Try again!")
        register()
    else:    
        print("Please enter your password")
        password = input(">>> ")
        print("Please enter your password again")
        password2 = input(">>> ")
        if password == password2:
            while True:
                print("Please enter your email")
                email = input(">>> ")
                if checkEmail(email):
                    print("This email is already taken")
                    print("Try again!")
                else:
                    break
            print("Your account has been created.")
            registerAccount(username,password,email)
            return True

        else:
            print("Your passwords don't match!")
            register()

def checkUsername(username):
    txt = open(os.path.dirname(os.path.abspath(__file__))+"/accountinfo.txt", "r")
    for line in txt:
        line = line.split(",")
        if username == line[0]:
            return True
        else:
            return False
def checkEmail(email):
    txt = open(os.path.dirname(os.path.abspath(__file__))+"/accountinfo.txt", "r")
    for line in txt:
        line = line.split(",")
        if email == line[2]:
            return True
        else:
            return False
def registerAccount(username,password,email):
    txt = open(os.path.dirname(os.path.abspath(__file__))+"/accountinfo.txt", "a")
    txt.write(username+","+password+","+email+",\n")
    txt.close

#make funktion which encrypt
