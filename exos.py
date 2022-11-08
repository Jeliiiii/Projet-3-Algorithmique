# DEBUT
r = 12000
s = 1250
e = 10 
rh = 230

assertionFinale = (((365 * 3) / (24 - (16 - 8))) * (rh) > r) == (e * s < r)

part1 = ((365 * 3) / (24 - (16 - 8)) * (rh) > r) #t
part2 = (e * s < r) #f

assertionFinale2 = ((365 * 3) / (4 - (12 - 8)) * (rh) > r) == (e * s < r)

part12 = ((365 * 3) / (4 - (12 - 8)) * (rh) > r) #f
part22 = (e * s < r) #f

# add(6, 3)
def retournerSixPlusTrois():
    return 6 + 3

# add(6, x)
def retournerSixPlusX(x):
    return 6 + x

# add(y, x)
def retournerYPlusX(x, y):
    return y + x


#Exercices Maison

# add(x, y)
def retournerXPlusY(x, y):
    return x + y 



# sub(x, y)
def retournerXMoinsY(x, y):
    return x - y



# multiply(x, y)
def retournerXMultiY(x, y):
    return x * y



# divide(x, y)
#Définir une fonction diviser
def retournerXDivY(x, y):
    #Si y est égale à 0
    if (y == 0) :
        #Alors afficher "Division par 0 impossible"
        print("Division par 0 impossible")
        #retourner vide
        return
    #Sinon
    else :
        #Retourner x diviser par y
        return x / y



# modulo(x, y)
def retournerXModuloY(x, y):
    return x % y



# SalaireNet(Brut, Coefficient)
#Définir une fonction withdrawFees qui retire unpourcenetage à un total en fonction d'un total et d'un pourcentage
def withdrawFees(total, percent):
    #Définir Fees en fonction d'un total et d'un pourcentage
    fees = total * (percent / 100)
    #soustraire Fess au total
    result = total - fees
    #retourner la valeur obtenue
    return result

#Definir uen fonction qui retourne le salaire net en fonction du salaire brut (float) et du secteur d'activité (isPublic > Boleen)
def CalculBrutEnNet(salaireBrut, isPublic):
    #Si je suis un travailleur du secteur public 
    if isPublic:
        #Alors je soustrais 15% de mon salaire Brut pour obtenir mon salaire Net public
        #salaireNet = salaireBrut - (salaireBrut * (85/100))
        salaireNet = withdrawFees(salaireBrut, 15)
    #Sinon : Je suis un travailleur privé
    else:
        #Alors je soustrais 23% de mon salaire Brut pour obtenir mon salaire Net Privé
        #salaireNet = salaireBrut - (salaireBrut * (77/100))
        salaireNet = withdrawFees(salaireBrut, 23)
    
    #Retourner salaireNet
    return salaireNet



# SalaireParSeconde(SalaireHoraire, HeureParJourOuvré, NbJourOuvréParAn)
def retournerSalparSec(salHoraire, HeureJour, Jour):
    #Calculer mon salaire annuel
    SalAnnuel = salHoraire * HeureJour * Jour
    #Calculer le nombre de seconde dans une année
    nbsecondeparan = 365 * 24 * 3600
    #Je pose et retourne la division
    return SalAnnuel / nbsecondeparan

def input():
    #Renvoie un caractère de type string au hasard

#Exercice mini jeu

#Faire un mini jeu qui affiche un message lorsque input renvoie le bon caractère
#Le caractère doit être paramétrable
#Debut
    #Définir le caractère à touver
    lettre = str(input("Définissez votre caractère à trouver"))

    #Initializer un compteur
    compteur = 0

    #Vérifier le caractère renvoyé par input tant que la valeur envoyée est différente de la valeur recherchée
    while input() != lettre:
        #Incrémenter le compteur
        compteur = compteur + 1
    else :
        #Afficher un message disant que la lettre a été touvée
        print("Bravo, vous avezz trouvé la lettre recherchée")
        #Afficher le nombre de passage dans la boucle pour y arriver
        print(compteur)

    #Vider le compteur
    compteur = 0
# FIN
