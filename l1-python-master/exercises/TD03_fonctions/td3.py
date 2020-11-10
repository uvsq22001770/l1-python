# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné."""
    return (temps[0]*24*3600+temps[1]*3600+temps[2]*60+temps[3])


temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps))


def secondeEnTemps(seconde):
    """Renvoie le temps du nombre de seconde passées en argument"""
    j = seconde // 86400
    h = (seconde % 86400) // 3600
    m = ((seconde % 86400) % 3600) // 60
    s = ((seconde % 86400) % 3600) % 60
    return ((j, h, m, s))


temps = secondeEnTemps(100000)
print(temps[0], "j", temps[1], "h", temps[2], "min", temps[3], "s")

# fonction auxiliaire ici


def afficheTemps(temps):

    """Affiche le temps"""
    if temps[0] == 1:
        print(temps[0], "jour", end=" ")
    elif temps[0] > 1:
        print(temps[0], "jours", end=" ")
    if temps[1] == 1:
        print(temps[1], "heure", end=" ")
    elif temps[1] > 1:
        print(temps[1], "heures", end=" ")
    if temps[2] == 1:
        print(temps[2], "minute", end=" ")
    elif temps[2] > 1:
        print(temps[2], "minutes", end=" ")
    if temps[3] == 1:
        print(temps[3], "seconde", end=" ")
    elif temps[3] > 1:
        print(temps[3], "secondes", end=" ")
    return temps


afficheTemps((1, 0, 14, 23))


def demandeTemps():
    """Redemande un temps si intervalles pas respactés"""

    jours = int(input("entrer nombre de jours"))
    heures = int(input("entrer nombre d'heures"))
    minutes = int(input("entrer nombre de minutes"))
    secondes = int(input("entrer nombre de secondes"))
    while heures >= 24:
        heures = int(input("entrez une nouvelle valeur pour les heures"))

    while minutes >= 60:
        minutes = int(input("entrez une nouvelle valeur pour les minutes"))

    while secondes >= 60:
        secondes = int(input("entrez une nouvelle valeur pour les secondes"))

    return (jours, heures, minutes, secondes)


afficheTemps(demandeTemps())


def sommeTemps(temps1, temps2):

    tempsEnSeconde(temps1)
    tempsEnSeconde(temps2)
    secondes_du_temps1 = tempsEnSeconde(temps1)
    secondes_du_temps2 = tempsEnSeconde(temps2)
    somme = secondes_du_temps1 + secondes_du_temps2
    somme1 = secondeEnTemps(somme)
    somme2 = afficheTemps(somme1)
    
    return somme2


sommeTemps((2, 3, 4, 25), (5, 22, 57, 1))
