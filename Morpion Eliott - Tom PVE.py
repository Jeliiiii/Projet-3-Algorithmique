#DEBUT
def bot(tablo, CPU):
    win = win()
    PlayerWin = win()
    AvCPU = AvCPU()
    if win != False:
        tablo[win[0]][win[1]] = CPU
    elif PlayerWin != False:
        tablo[PlayerWin[0]][PlayerWin[1]] = CPU
    elif AvCPU != False:
        tablo[AvCPU[0]][AvCPU[1]] = CPU

def deuxParTrois(caseA, caseB, caseC):
    if caseA == caseB == PoE and caseC == "-":
        return 2
    elif caseC == caseA == PoE and caseB == "-":
        return 1
    elif caseB == caseC == PoE and caseA == "-":
        return 0
    return False

def win(tablo, PoE):
    for i in range(3):
        ligne = deuxParTrois(tablo[i][0], tablo[i][1], tablo[i][2], PoE)
        colonne = deuxParTrois(tablo[0][i], tablo[1][i], tablo[2][i], PoE)
        if ligne != False:
            return i, ligne
        if colonne != False:
            return colonne, i