# -*- coding: utf-8 -*-
import random

pointedanswer = {
    "hallo": "Schönen Guten Tag.",
    "geht": "Alles was Beine hat.",
    "herunterfahren": "Tur mir leid, sie müsssen den Command bye nutzen um mich abzuschalten",
    "fresh": "Danke, ich denke auch das sie Fresh sind",
    "apfel": "Birne",
    "was": "Wie?",
    "nein": "Doch!",
    "helikopter": "117"

}
randomsentance = ["Sehr schön!","Das klingt ja sehr interesant.","Coole Sache!","Ich Verstehe..."]


print("Coding Training by www.Phyton-Lernen.de")
print("Dieser Chatbot wird versuchen mit dir ein Gespräch zu führen.")
print("Wenn du ihm überdrüssig bist, screibe enifach 'bye'.")
userinput = ""
while not userinput == "bye":
    userinput = ""
    while userinput == "":
        userinput = input("Ihre Frage/Anntwort")
    userinput = userinput.lower()
    user_words = userinput.split()
    for x in user_words:
        if x in pointedanswer():
    print(random.choice(randomsentance))
print("Program beendet!")
exit()