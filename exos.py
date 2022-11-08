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
def retournerBrutNetCoef(Brut, Coefficient):
    return Brut * Coefficient

# SalaireParSeconde(SalaireHoraire, HeureParJourOuvré, NbJourOuvréParAn)
def retournerSalparSec(salHoraire, HeureJour, Jour):
    SalAnnuel = salHoraire * HeureJour * Jour
    nbsecondeparan = 365 * 24 * 3600
    return SalAnnuel / nbsecondeparan
# FIN