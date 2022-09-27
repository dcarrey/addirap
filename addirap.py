"""
=============================================================================
= addirap : générateur d'addition pour l'approche addirap
= auteur : Alix boc
= date : 2022
=============================================================================
"""
from random import randint
import sys

def generate(nbOperations=50,minValue=1,maxValue=9):
    operations = []
    noOperation = 0
    maxLoop = 10000
    nbLoop = 0
    while noOperation < nbOperations:
        nbLoop += 1
        a = randint(minValue,maxValue)
        b = randint(minValue,maxValue)
        if nbLoop < maxLoop:
            if (a,b) not in operations:
                operations.append((a,b))
                noOperation += 1
        else:
            operations.append((a,b))
            noOperation += 1
    return operations

def afficher(operations,operation="+",output=sys.stdout):
    for key in operations:
        print(key[0], operation, key[1], "=", file=output)

def validerMode(mode,min,max):
    if mode == "facile":
        minValue = min
        maxValue = int(max/2)+1
    elif mode == "moyen":
        minValue = min
        maxValue = max
    elif mode == "difficile":
        minValue = int(max/2)+1
        maxValue = max
    return (minValue,maxValue)

def main(parametres):
    nbOperations=50
    operation = "+"
    minValue = 1
    maxValue = 9
    if len(parametres) > 1:
        for param in parametres[1:]:
            tab = param.split("=")
            if tab[0] == "operation":
                operation = tab[1]
            elif tab[0] == "nbOperations":
                nbOperations = int(tab[1])
            elif tab[0] == "minValue":
                minValue = int(tab[1])
            elif tab[0] == "maxValue":
                maxValue = int(tab[1])
            elif tab[0] == "mode":
                (minValue,maxValue) = validerMode(tab[1],minValue,maxValue)
            else:
                print("parametre inconnu :",tab[0])
    afficher(generate(nbOperations=nbOperations,minValue=minValue,maxValue=maxValue),operation=operation)

if __name__ == "__main__":
    main(sys.argv)
