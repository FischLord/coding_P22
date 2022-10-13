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



def eingabe():
  global game
  while True:
    eingabe = input("Hier das Feld eingeben -> ")
    try:
      eingabe = int(eingabe)
    except ValueError:
      print("Eingabe muss eine Ganzzahlige Zahl sein.")
    else:
      if eingabe >= 1 and eingabe <= 9:
       return eingabe
      else:
        print("Zahl muss im spektrum von 1-9 liegen.")



spielstand()
while game:
  print(aktuellerplayer, "ist am Zug")
  eingabe=eingabe()
  if eingabe:
    Feld[eingabe] = aktuellerplayer
    spielstand()
    playerident()




