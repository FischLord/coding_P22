schalter= "y"
equals = "=================="
space_holder = equals+"Übersetzung"+equals

def spacer():
    print(space_holder)
    print()
    print(satz)
    print()
    print(space_holder)

while schalter == "y":
    print(("Bitte geben sie den zu Übersetzenden Satz ein."))
    satz = str(input("--> "))
    tester = 1
    #Kleinbuchstaben
    satz = satz.replace("e","elewe")
    satz = satz.replace("a","alewa").replace("i","ilewi").replace("o","olewo").replace("u","ulewu").replace("ä","älewä").replace("ö","ölewö").replace("ü","ülewü")
    satz = satz.replace("eleweilewi","eilewei").replace("ilewielewe","ielewie").replace("alewaulewu","aulewau")
    #Großbuchstaben
    satz = satz.replace("E","Elewe")
    satz = satz.replace("A","Alewa").replace("I","Ilewi").replace("O","Olewo").replace("U","Ulewu").replace("Ä","Älewä").replace("Ö","Ölewö").replace("Ü","Ülewü")
    satz = satz.replace("Eleweilewi","Eilewei").replace("Ilewielewe","Ielewie").replace("Alewaulewu","Aulewau")
    spacer()
    while tester == 1:
        schalter = str(input("Wollen Sie eine weiter Übersetzung tätigen? (y/n)"))
        if schalter == "n":
            print("Einen schönen Tag noch.")
            tester = 0
        else:
            if schalter == "y":
                print("")
                tester = 0
            else:
                print("Falsche Antwort, bitte benutzen sie y für JA oder n für NEIN")