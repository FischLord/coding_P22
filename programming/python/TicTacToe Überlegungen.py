game = True
aktuellerplayer = "O"

Feld = ["0","1","2","3","4","5","6","7","8","9"]

def spielstand():
  print(" -----------")
  print("|",Feld[1],"|",Feld[2],"|",Feld[3],"|")
  print("|---|---|---|")
  print("|",Feld[4],"|",Feld[5],"|",Feld[6],"|")
  print("|---|---|---|")
  print("|",Feld[7],"|",Feld[8],"|",Feld[9],"|")
  print(" -----------")

def playerident():
  global aktuellerplayer
  if aktuellerplayer == "X":
    aktuellerplayer = "O"
  else:
    aktuellerplayer = "X"


def spieler_eingabe():
    global spiel_aktiv
    while True:
        spielzug = input("Bitte Feld eingeben: ")
        try:
            spielzug = int(spielzug)
        except ValueError:
            print("Bitte Zahl von 1 bis 9 eingeben")
        else:
            if spielzug >= 1 and spielzug <= 9:
                return spielzug
            else:
                print("Zahl muss zwischen 1 und 9 liegen")



spielstand()
while game:
  print(aktuellerplayer, "ist am Zug")
  spielzug=spieler_eingabe()
  if spielzug:
    Feld[spielzug] = aktuellerplayer
    spielstand()
    playerident()




