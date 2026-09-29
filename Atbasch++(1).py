#Eingabe wird wie folgt verschlüsselt:
#1. Normal nach Atbasch (+Zahlen u. Sonderzeichen) verschlüsseln
#Ergebnis in zwei Hälften teilen
#Abwechselnd Buchstaben der ersten und zweiten Hälfte hintereinander ausgeben (bis jetzt nur als einzelne Zeichen per print)

import random as r
import string

print("Mein Atbasch++")
print("==================")
print("1 = verschlüsseln, 2 = Entschlüsseln")

i = 0    

xpar = string.ascii_lowercase + string.digits + string.punctuation

def genkey():
    zeichen = list(xpar)
    r.shuffle(zeichen)
    return ''.join(zeichen)

key = genkey()

if input() == "1": #verschlüsseln^

    klartext = input("Klartext eingeben: ")
    geheimtext = ""
    klartext = klartext.lower()

    for zeichen in klartext:
        geheimtext = geheimtext + zeichen

    #ggf. Zeichen austauschen
    geheimtext = geheimtext.replace("ä", "ae")
    geheimtext = geheimtext.replace("ö", "oe")
    geheimtext = geheimtext.replace("ü", "ue")
    geheimtext = geheimtext.replace("ß", "ss")
    geheimtext = geheimtext.replace (" ", "")

    #klartext übersetzen
    tabelle = str.maketrans(xpar, key)
    geheimtext = geheimtext.translate(tabelle).upper()

    #geheimtext verkreuzen
    print("Geheimtext ausgeben:" + " " + geheimtext[0 : len(geheimtext) : 2] + geheimtext[1 : len(geheimtext) : 2])

    print("Schlüssel:")
    print(key)

else: #entschlüsseln
    
    def entwirren():
        global klartext
        global i
        for x in range((laenge//2)):
            klartext = klartext + (klartext[i : i+1])
            i = i + laenge//2
            klartext = klartext + (klartext[i : i+1])
            i = i - (laenge//2 - 1)
    1
    geheimtext = input("Geheimtext eingeben:")
    klartext = ""
    geheimtext = geheimtext.lower()

    
    for zeichen in geheimtext:
        klartext = klartext + zeichen
    
    #geheimtext übersetzen
    tabelle = str.maketrans(input("Schlüssel eingeben:"), xpar)
    klartext = klartext.translate(tabelle).upper()
    
    #geheimtext entkreuzen
    
    if len(klartext) % 2 == 1: #länge um 1 erweitern wenn geheimtext ungerade ist
        laenge = len(klartext)+1
        entwirren()

    else: #wenn nicht dann halt nicht
        laenge = len(klartext)
        entwirren()
    
    #Klartext zuschneiden und ausgeben
    print("Entschlüsselter Klartext: ")
    
    if len(klartext) %2 == 0:
        print(klartext[len(klartext)//2 : len(klartext)])
    else:
        print(klartext[len(klartext)//2 : len(klartext)-1])