import os,time
from stat import FILE_ATTRIBUTE_COMPRESSED
####################### Login start #######################
def inputdetails(x):
    global name,password
    if x == "n":
        name = input("Bitte geben sie ihren Namen an.  ")
        print()
    if x == "p":
        password = input("Bitte geben sie ihren Passwort an.  ")
        print()
    if x == "np":
        name = input("Bitte geben sie ihren Namen an.  ")
        print()
        password = input("Bitte geben sie ihren Passwort an.  ")
        print()

def test():
    inputdetails("n")
    txttest = open("python\login\details.txt", "r")
    for i in txttest:
        details = i.split(",")
        detailsname = details[0]
        if detailsname == name:
            print("Dieser username ist bereits vergeben!")
            txttest.close
            test()
    txttest.close

def reg():
    test()
    inputdetails("p")
    txt = open("python\login\details.txt", "a")
    txt.write(name+","+password+",\n")
    txt.close
    print("Registrierung erfolgreich!")

def log(npvar):
    txtlog = open("python\login\details.txt", "r")
    inputdetails(npvar)
    for i in txtlog:
        details = i.split(",")
        detailsname = details[0]
        detailspassword = details[1]
        if name == detailsname and password == detailspassword:
            print("Succesfully logged in!")
            txtlog.close
            userexist = 0
            break
        elif name == detailsname and password != detailspassword:
            print("Passwort Falsch")
            txtlog.close
            log("p")
        elif name != detailsname:
            userexist = 1
    if userexist == 1:
        print("This user doesnt exist!")


def login():
    print("Bitte wählen sie zwischen Login (log) und Registrieren (reg)! ")
    intention = input()
    if intention != "reg":
        if intention != "log":
            login()
    if intention == "reg":
        reg()
    if intention == "log":
        log("np")
####################### Login end #######################

login()
#Login complete
time.sleep(0.8)
os.system("cls")