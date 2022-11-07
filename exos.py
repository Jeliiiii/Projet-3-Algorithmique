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

def retournerSixPlusTrois():
    return 6 + 3

def retournerSixPlusX(x):
    return 6 + x

def retournerYPlusX(x, y):
    return y + x

retournerSixPlusTrois()
retournerSixPlusX()
print("Qui vole un" + retournerSixPlusTrois() + "Vole un boeuf")

print("Bonjour world !")
# FIN