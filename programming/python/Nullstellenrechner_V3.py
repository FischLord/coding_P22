rechner = True
x_zahlen =[]
x_exponenten=[]
y = 0
ns = []
space="##################"

def spacer(len):
    print(space)
    for i in range(len):
        print("-")
    print(space)


print("                             ",space,"Nullstellenrechner - V.3 - BETA",space)
print()
print("Dieser Nullstellenrechner versucht durch das einsetzen von Zahlen in einem Bereich zwischen 100 und -100 die Nullstell einer Funktion herrauszufinden.")
print("Die Beta Version hierbei ist noch nicht in der Lage mit Kompletten funktionseingaben zu Rechnen, deswegen müssen zuerst einige Funktionskomponenten einzeln eingegeben werden.")
print("Bitte Geben sie an ob sie die Rechenvorgänge des Rechners sehen wollen oder nicht. (ja/nein)")
print("Das Anzeigen der errechneten Variablen, kann die Folge haben das die Rechnung länger dauert.")
schalter = False
while not schalter == True:
    logger = input("--> ")
    try:
        logger = str(logger)
    except ValueError:
        print("Bitte mit ja oder nein Antworten!")
    else:
        if logger == "ja" or logger == "nein":
            schalter = True
        else:
            print("Bitte mit ja oder nein Antworten!")
            
spacer(3)
while rechner == True:
    #-------Start Angabe der Länger der Funktion-------#
    print("Bitte geben sie die Anzahl der vorhandeneden 'x'-Variablen an.")
    schalter = False
    while not schalter == True:
        xanzahl = input("--> ")
        try:
            xanzahl = int(xanzahl)
        except ValueError:
            print("Bitte eine Zahl eingeben!")
        else:
            if xanzahl < 1:
                print("Es muss mindestens Ein x in der Funktion geben. (Sprich die Eingabe muss mind. 1 sein.)")
            else:
                schalter = True
    #-------Start Eingabe der Funktion--------#
    loop_anzahl = 0
    for loop in range(xanzahl):
        loop_anzahl = loop_anzahl + 1
        print("Bitte geben Sie die Zahl ein, die vor dem",loop_anzahl,". x steht.")
        schalter = False
        while not schalter == True:
            zahl = input("--> ")
            try:
                zahl = float(zahl)
            except ValueError:
                print("Bitte eine Zahl eingeben.")
            else:
                schalter = True
        x_zahlen.append(zahl)
        print("Bitte geben Sie den Exponenten vom",loop_anzahl,". x ein. (Wenn kein Sichtbarer Exponent vorhanden ist, gebe 1 ein.)")
        schalter = False
        while not schalter == True:
            exponent = input("--> ")
            try:
                exponent = int(exponent)
            except ValueError:
                print("Bitte eine Zahl eingeben.")
            else:
                if exponent < 1:
                    print("Die eingabe muss mindestens 1 sein.")
                else:
                    schalter = True
        x_exponenten.append(exponent)
    print("Bitte geben Sie das Absolutglied der Funktion an. (Die Zahl ohne x am ende)")
    schalter = False
    while not schalter == True: 
        absolutglied = input("--> ")
        try:
            absolutglied = float(absolutglied)
        except ValueError:
            print("Bitte eine Zahl eingeben.")
        else:
            schalter = True
    #-------Start berechnung der Nullstelle------#
    x_zahlen_save = x_zahlen.copy()
    x_exponenten_save = x_exponenten.copy()
    xanzahl_save = xanzahl
    schalter = False
    x = -100
    x_anzahl = 0 
    versuch = 0
    while not schalter == True:
        x_zahlen = x_zahlen_save.copy()
        x_exponenten = x_exponenten_save.copy()
        xanzahl = xanzahl_save
        y = 0
        for loop in range(xanzahl):
            y = y + x_zahlen[0] * x ** x_exponenten[0]
            del x_zahlen[0]
            del x_exponenten[0]
        y = round(y,4) + round(absolutglied,4)
        if y == 0:
            ns.append(x)
        if logger == "ja":
            print("(",x,"|",y,")")
        #----------Start der X-Zugabe-----------#
        if y <= 5:
            x = x + 10**-4
            x = round(x,4)
        if y > 5 and y <= 10:
            x = x + 10**-3
            x = round(x,3)
        if y > 10:
            x = x + 10**-1
            x = round(x,1)
        x_anzahl = x_anzahl + 1
        #----------Ende der Nullstellensuche--------#
        if x > 100:
            schalter = True
        versuch = versuch + 1
    #-----------Start der Endsequenz-----------#
    spacer(8)
    print("Es wurden",versuch,"Zahlen in die Formel eingesetzt um eine Lösung zu finden.")
    print("Die gefundenden Nulstellen lauten:",ns)
    print("Wollen sie eine weitere Nullstelle berrechnen lassen? (y/n) ")
    schalter = False
    while not schalter == True:
        abfrage = input("--> ")
        try:
            abfrage = str(abfrage)
        except ValueError:
            print("Bitte eine gültige Antwort geben! (y/n)")
        if not abfrage == "y":
            rechner = False
            print("Einen schönen Tag noch.")
            schalter = True
        else:
            rechner = True
            schalter = True