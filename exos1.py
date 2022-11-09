#Exercice 1 #Faire une fonction qui concatene 2 chaînes de charactères, les séparants par une virgule  

#DEBUT
def concaWithComma(strA, strB):
    #Je m'assure que strA est bien un str
    stringfieldA = str(strA)
    #Je m'assure que strB est bien un str
    stringfieldB = str(strB)
    #Retourner strA + ',' + strB
    return strA + ", " + strB

concaWithComma(23, "tomato")
#FIN


#Exercice 2 #Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de charactère #avec l'ensemble des occurences d'un chiffres e.g: pour 
#la fonction(tableau, 0) doit renvoyer "0,4,7" n'hésitez pas a implémenter la premiere fonction;)  

#DEBUT
tableau = [0,1,1,1,0,1,1,0,1] 
#Definir la fonction findIndex qui itere sur tableau, cherchant l'index des différences occurente de x
def findIndex(tableau, x):
    #Definir i un index de depart
    i = 0
    #Definir chaineRetour telle qu'une chaine de caractère vide
    chainRetour = ''
    #Je défini un booleen tel que firstTurn est true
    firstTurn = True
    #Tant que i est different du nombre d'element dans le tableau
    while i != len(tableau) :
         #Alors j'attribue à une variable la valeur de tableau à l'index i
        selected = tableau[1]
        #Si selected est égal à x ET que firstTurn est true
        if selected == x & firstTurn == True :
            #Alors on assigne a chaineRetour le retour de str(i)
            chaineRetour = str(i)
            #Changer la valeur de firstTurn a false
            firstTurn = False
        #Sinon si selected est égal à x
        elif selected == x :
            #Alors j'assigne le retour de concaWithComma tel que : concaWithComma(chaineRetour, i) à chaineRetour
            chaineRetour = concaWithComma(chaineRetour, i)
        #J'incrémente i de 1 
        i = i + 1
    #Retourner la chaine retour
    return chaineRetour
#Definir mon index
i = 0
while (i != len(tableau)):
    selected = tableau[i]
    i = i + 1
#FIN


#Exercice 3 #Renvoyer / Afficher un message
#DEBUT

msg=str(input("Entrez vôtre message : "))
print(msg)

#FIN

#Une fonction qui renvoie la suite de Fibonacci