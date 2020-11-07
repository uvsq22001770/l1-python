# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return (temps[0]*24*3600+temps[1]*3600+temps[2]*60+temps[3])


temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps))   


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    j = seconde // 86400
    h = (seconde % 86400) // 3600
    m = ((seconde % 86400) % 3600) // 60
    s = ((seconde % 86400) % 3600) % 60
    return ((j, h, m, s))


temps = secondeEnTemps(100000)
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes")

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

    temps[0] = int(input())
    temps[1] = int(input())
    temps[2] = int(input())
    temps[3] = int(input())
    
    return (temps[0], temps[1], temps[2], temps[3])

afficheTemps(demandeTemps())