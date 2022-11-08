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
def retournerXDivY(x, y):
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
# FIN
