import math

def nteWurzel(r, x1):  #n-te Wurzel ziehen
    return r**(1 / float(x1))


def umstellen():
    print(
        "\033[33m[Gebe bitte die gefragten Daten nach dem muster: \033[34m(m*x^n+n)\033[33m ein]\x1B[0m"
    )  #aufforderung der eingabe nach dem vorgegebenen Muster
    print()
    m = float(input("\033[36m\033[1mm\033[0m -->"))  #abfrage nach m
    x1 = float(input("\033[36m\033[1mExponent von x\033[0m -->")
               )  #abfrage nach dem Exponenten des ersten x Wertes
    n = float(input("\033[36m\033[1mn\033[0m -->"))  #abfrage nach n
    r = (0 - (n)) / m  #umstellung von n nach 0 und geteielt durch m
    e = float()  #Definition des Ergebniswertes
    if x1 < 1:  #falls ein negativer Exponent angegeben wird gibt es eine Fehlermeldung
        print(
            "\033[31mDer Rechner ist nicht für negative Exponenten ausgelegt!\033[0m"
        )
        print()
    else:
        if x1 > 1:  #wenn es einen Exponeten gibt der größer als 1 ist wird dieser bereich ausgeführt wobei eine Wurzel gezogen werden muss
            if r < 0:  #wenn der r Wert negativ ist kann keine Wurzel gezogen werden ergo: keine Nullstelle vorhanden
                print("\033[7mKeine Nullstellen vorhanden.\033[0m")
                print()
            else:  #wenn r positiv ist wird die Wurzel gezogen und die Nullstellen ausgegeben
                e = r**(1.0 / x1)
                y = m * (e)**x1 + (
                    n
                )  #kreiren der Funktion damit der y Wert für den genauen Punkt ausgerechet werden kann
                print("\033[7mAbgefragte Funktion: f(x)=", m, "x^", x1, "+", n,
                      "\033[0m")
                print("\033[7mNullstelle 1 lautet:", e, "sie liegt bei P(", e,
                      "/", y, ")\033[0m")
                print("\033[7mNullstelle 2 lautet:", -e, "sie liegt bei P(",
                      -e, "/", y, ")\033[0m")
                print()
        else:
            if x1 == 1:
                y = m * (r) + (
                    n
                )  #kreiren der Funktion damit der y Wert für den genauen Punkt ausgerechet werden kann
                print("\033[7mDie Nullstelle der Funktion: f(x)=", m, "x+", n,
                      "lautet:", r, "sie liegt bei P(", r, "/", y, ")\033[0m")
                print()


def pqformel():
    print(
        "\033[33m[Gebe bitte die gefragten Daten nach dem muster: \033[34m(ax^2+bx+c)\033[33m ein]\x1B[0m"
    )  #aufforderung der eingabe nach dem vorgegebenen Muster
    print()
    a = float(input("\033[36m\033[1ma\033[0m-->"))
    b = float(input("\033[36m\033[1mb\033[0m-->"))
    c = float(input("\033[36m\033[1mc\033[0m-->"))
    b = (b) / (a)
    c = (c) / (a)
    pq0 = ((b) / 2)**2 - (c)  #ausrechnen des Wertes der unter der Wurzel steht
    if pq0 < 0:
        print("\033[7mKeine Nullstellen in der Funktion: f(x):", a, "x^2+(",
              b * a, ")x+(", c * a, ")vorhanden.\033[0m")
        print()
    else:
        pq1 = -((b) / 2) + (pq0**(1 / 2))  #lösung der + pq formel
        pq2 = -((b) / 2) - (pq0**(1 / 2))  #lösung der - pq formel
        y1 = ((pq1)**2) + (b * (pq1)) + (c)
        y2 = ((pq2)**2) + (b * (pq2)) + (c)
        print("\033[7mAbgefragte Funktion: f(x):", a, "x^2+(", b * a, ")x+(",
              c * a, ")\033[0m")
        print()
        print("\033[7mNullstelle 1 bei: ", pq1, "sie liegt bei P(", pq1, "/",
              y1, ")\033[0m")
        print("\033[7mNullstelle 2 bei: ", pq2, "sie liegt bei P(", pq2, "/",
              y2, ")\033[0m")


def substitution():
    print(
        "\033[33m[Gebe bitte die gefragten Daten nach dem muster: \033[34m(ax^(n*2)+bx^n+c)\033[33m ein]\x1B[0m"
    )
    a = float(input("\033[36m\033[1ma\033[0m-->"))
    b = float(input("\033[36m\033[1mb\033[0m-->"))
    c = float(input("\033[36m\033[1mc\033[0m-->"))
    n = float(
        input("\033[36m\033[1mn\033[0m-->")
    )  #abfrage des kleineren Exponenten wobei er halb so groß sein muss wie der größere Exponent
    m = n * 2  #kann möglicherweise fehler hervorrufen
    b = (b) / (a)  #alle Glieder werden durch den a Wert geteielt
    c = (c) / (a)
    pq0 = ((b) / 2)**2 - (c)  #ausrechnen des Wertes der unter der Wurzel steht
    if pq0 < 0:
        print("\033[7mKeine Nullstellen in der Funktion: f(x):", a, "x^2+(",
              b * a, ")x+(", c * a, ")vorhanden.\033[0m")
        print()
    else:
        pq1 = -((b) / 2) + (pq0**(1 / 2))  #lösung der + pq formel
        pq2 = -((b) / 2) - (pq0**(1 / 2))  #lösung der - pq formel
        print("\033[7mAbgefragte Funktion: f(x):", a, "x^2+(", b * a, ")x+(",
              c * a, ")\033[0m")
        print()
        if pq1 > 0:  #testen erstes Ergebnis der pq Formel positiv ist
            wpq1 = pq1**(1 / n)  #wurzel aus dem pq ergebnis ziehen
            y1 = ((wpq1)**m) + (b * ((wpq1)**n)) + (c)
            y3 = ((-wpq1)**m) + (b * ((-wpq1)**n)) + (c)
            print("\033[7mNullstelle 1 bei: ", wpq1, "sie liegt bei P(", wpq1,
                  "/", y1, ")\033[0m")
            print("\033[7mNullstelle 2 bei: ", -wpq1, "sie liegt bei P(",
                  -wpq1, "/", y3, ")\033[0m")
        if pq2 > 0:  #testen zweites Ergebnis der pq Formel positiv ist
            wpq2 = pq2**(1 / n)  #wurzel aus dem pq ergebnis ziehen
            y2 = ((wpq2)**m) + (b * ((wpq2)**n)) + (c)
            y4 = ((-wpq2)**m) + (b * ((-wpq2)**n)) + (c)
            print("\033[7mNullstelle 3 bei: ", wpq2, "sie liegt bei P(", wpq2,
                  "/", y2, ")\033[0m")
            print("\033[7mNullstelle 4 bei: ", -wpq2, "sie liegt bei P(",
                  -wpq2, "/", y4, ")\033[0m")
        if pq1 < 0 and pq2 < 0:  #testen ob beide Ergebnisse der pq Formel negativ sind
            print("\033[7mKeine Nullstellen vorhanden.\033[0m")
            print()
def polynomdivision():
    variable = int(input("\033[36m\033[1mNenne die anzahl der Variablen (max=5)\033[0m-->"))
    if variable == 4:
      a = float(input("\033[36m\033[1ma\033[0m-->"))
      b = float(input("\033[36m\033[1mb\033[0m-->"))
      c = float(input("\033[36m\033[1mc\033[0m-->"))
      d = float(input("\033[36m\033[1md\033[0m-->"))
    if variable == 5:
      a = float(input("\033[36m\033[1ma\033[0m-->"))
      b = float(input("\033[36m\033[1mb\033[0m-->"))
      c = float(input("\033[36m\033[1mc\033[0m-->"))
      d = float(input("\033[36m\033[1md\033[0m-->"))
      d = float(input("\033[36m\033[1md\033[0m-->"))
    else:
        print("nice")

    print()
    print("Momentan ist er nur für Floats Bsp:(1.00231234) ausgelegt!")
    print("Das ist ein Nullstellen Rechner (er berechnet Nullstelen)")
    print("Tippe 1 um etwas Gleichzusetzen (Ein x ist in der Funktion Bsp: f(x)=ax^n+b)")
    print("Tippe 2 um eine Nullstelle eine Quadratischen gleichung zu berechnen Bsp: f(x)=ax^2+bx+c")
    print("Tippe 3 um eine Nullstelle mithilfe der Substitution zu bestimmen Bsp: f(x)=ax^4+bx^2+c ")
    print("Tippe 4 um eine Nullstelle aus einer Funktion zu bekommen bei der man die Polynomdivision anwenden müsste Bsp: f(x)=ax^3+bx^2+cx+d")
    print()
    art = int(input("Hier eingeben:"))
    print()
    print()
    if art == 1:  #Nullstellen durch umstellen bestimmen
        umstellen()
    if art == 2:  #Nullstellen einer Quadratischen Funktion bestimmen
        pqformel()
    if art == 3:  #Nullstellen mithilfe der Substituttion bestimmen
        substitution()
    if art == 4:
        print("Das ist die Nullstellenberechnung eines Polynoms")
        print("Um die Polynomdivision anwenden zu können muss eine Nullstelle bekannt sein.")
        print("Diese kann z.b. durch raten Herausgefunden werden")
        abfrage = input("Tippe: [true] wenn du bereits eine hast und [false] wenn keine: ")
        print()
        if abfrage == "true":
            NS = float(input("\033[36m\033[1mDie bereits herausgefundene Nullstelle\033[0m-->"))
            print("Diese Eingabe war Leider nicht korrekt!")
        else:
            if abfrage == "false":
                print("false")
            else:
                print("Prüfe deine Eingabe bitte nochmal ^^")
    if art > 4:
            print("\033[41mDas ist eine Ungültige eingabe!\x1B[0m")
    if art < 0:
            print("\033[41mDas ist eine Ungültige eingabe!\x1B[0m")

polynomdivision()
