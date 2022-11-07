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
part22 = (e * s < r) #t

# FIN