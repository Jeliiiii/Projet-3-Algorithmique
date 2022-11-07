# DEBUT
r = 12000
s = 1250
e = 10 
rh = 230

part1 = ((365 * 3) / (24 - (16 - 8)) * (rh) > r) #t
part2 = (e * s < r) #f

assertionFinale = ( (365 * 3) / (24 - (16 - 8)) * (rh) > r) == (e * s < r)
assertionFinale = part1 == part2


# FIN