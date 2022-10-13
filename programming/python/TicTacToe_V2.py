import random
game = True
gamewon = False
sfeld = ["1","2","3","4","5","6","7","8","9"]


def reset():
    global sfeld
    sfeld = ["1","2","3","4","5","6","7","8","9"]

def spielstand():
    global spacer
    spacer = "                 "
    print()
    print(spacer," -----------",spacer)
    print(spacer,"|",sfeld[0],"|",sfeld[1],"|",sfeld[2],"|",spacer)
    print(spacer,"|---|---|---|",spacer)
    print(spacer,"|",sfeld[3],"|",sfeld[4],"|",sfeld[5],"|",spacer)
    print(spacer,"|---|---|---|",spacer)
    print(spacer,"|",sfeld[6],"|",sfeld[7],"|",sfeld[8],"|",spacer)
    print(spacer," -----------",spacer)
    print()

def space():
    print(spacer)

def spielerinfo():
    print("Spieler 1 bitte geben sie einen Namen ein wie ich sie nennen kann.")#Spieler 1/2 müssen ihren Nick setzen
    global p1name,p2name,p1symbol,p2symbol,p1info,p2info
    p1name = input("--> ")
    print("Spieler 2 bitte geben sie einen Namen ein wie ich sie nennen kann.")
    p2name = input("--> ")
    print(p1name,"bitte wähle dein Symbol")#Spieler 1/2 Symbol wird festgelegt/gespeichert
    p1symbol = input("--> ") 
    print(p2name,"bitte wähle dein Symbol")
    p2symbol = input("--> ")
    p1info = [p1name,p1symbol]
    p2info = [p2name,p2symbol]

def starterchoice(): #Es wird ausgelosst wer startet
    spieler = [p1name,p2name]
    starter = random.choice(spieler)
    spieler.remove(starter)
    print(starter,"fängt an!")
    print(spieler[0],"hat den zweiten Zug!")
    global p1,p2
    p1 = starter
    p2 = spieler[0]

def roundstowin():
    global rundenanzahl
    randomplayer = [p1name,p2name]
    randomplayer = random.choice(randomplayer)
    print("Bitte entscheidet euch wieviel Runden gewonnen werden müssen bis",randomplayer,"gewinnt.")
    rundenanzahl = input("--> ")

def winvarupdater():
    global w1,w2,w3,w4,w5,w6,w7,w8
    w1 = sfeld[0] + sfeld[1] + sfeld[2] #w1 - w3 Gewinnzahlen Horizontal
    w2 = sfeld[3] + sfeld[4] + sfeld[5]
    w3 = sfeld[6] + sfeld[7] + sfeld[8]
    w4 = sfeld[0] + sfeld[3] + sfeld[6] #w4 - w6 Gewinnzahlen Vertikal
    w5 = sfeld[1] + sfeld[4] + sfeld[7]
    w6 = sfeld[2] + sfeld[5] + sfeld[8]
    w7 = sfeld[0] + sfeld[4] + sfeld[8] #w7 - w8 Gewinnzahlen Schräg
    w8 = sfeld[6] + sfeld[4] + sfeld[2]

def spielzug():
    global p1zug,p2zug,p1s,p2s #Anfang der Spielerzuodrnung
    if p1 in p1info:
        p1s = p1info[1]
        p2s = p2info[1]
    else:
        p1s = p2info[1]
        p2s = p1info[1] #Ende der Spielerzuordnung     
    gamewon = False
    aktuellerunden1 = 0
    aktuellerunden2 = 0
    while not gamewon == True:
        space()
        print(p1,"bitte geben sie das Feld an wo sie ihr",p1s,"setzen wollen.")
        p1zug = input("--> ") #Spielereingabe muss noch geprüft werden
        p1zugzahl = int(p1zug) #Spielereingabe wird verarbeitet
        sfeld[p1zugzahl-1] = p1s
        p1sw = p1s + p1s + p1s #Für die Gewinnkontrolle
        winvarupdater() #Gewinnchecker Zahlen werden geupdated
        spielstand() #Spielstand wird angezeigt
        if w1 == p1sw or w2 == p1sw or w3 == p1sw or w4 == p1sw or w5 == p1sw or w6 == p1sw or w7 == p1sw or w8 == p1sw: #Es wird geprüft ob P1 gewonnen hat
            reset()
            aktuellerunden1 = aktuellerunden1 + 1
            if aktuellerunden1 == rundenanzahl: #Falls die gewünschte Rundenzahl erreicht wurde wird das Spiel Beendet
                gamewon = True
                print(p1,"Gewinnt das Spiel!")
            else:
                print(p1,"Score: ",aktuellerunden1,"/",rundenanzahl)
                spielstand()
        if not gamewon == True: #Spieler 2 Spielzug
            space()
            print(p2,"bitte geben sie das Feld an wo sie ihr",p2s,"setzen wollen.")
            p2zug = input("--> ")
            p2zugzahl = int(p2zug) #Spielereingabe wird verarbeitet
            sfeld[p2zugzahl-1] = p2s
            p2sw = p2s + p2s + p2s #Für die Gewinnkontrolle
            winvarupdater()
            spielstand()
            if w1 == p2sw or w2 == p2sw or w3 == p2sw or w4 == p2sw or w5 == p2sw or w6 == p2sw or w7 == p2sw or w8 == p2sw: #Es wird geprüft ob P2 gewonnen hat
                reset()
                aktuellerunden2 = aktuellerunden2 + 1
                if aktuellerunden2 == rundenanzahl: #Falls die gewünschte Rundenzahl erreicht wurde wird das Spiel Beendet
                    gamewon = True
                    print(p2,"Gewinnt das Spiel!")
                else:
                    print(p2,"Score: ",aktuellerunden2,"/",rundenanzahl)
                    spielstand()
                


while game == True:
    spielerinfo()
    roundstowin()
    starterchoice()
    spielstand()
    spielzug()
    game = input("Wenn sie Aufhören möchten geben sie False ein!")