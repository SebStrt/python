print("Caesar")
print("==================")
print("1 = verschlüsseln, 2 = Entschlüsseln")

i = 0    

if input() == "1": #verschlüsseln

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
    
    n = 0
    
    alpha1 = "abcdefghijklmnopqrstuvwxyz"
    
    
    
    
    for n in range(1, 27):
        alpha2 = alpha1[n :] + alpha1[ : n]
        tabelle = str.maketrans(alpha1, alpha2)
        geheimtext = klartext.translate(tabelle)
        geheimtext = geheimtext.upper()
        print("Rotation " + str(n) + " " + geheimtext)
    