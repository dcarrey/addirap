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
    operations = {}
    noOperation = 0
    while noOperation < nbOperations:
        a = randint(minValue,maxValue)
        b = randint(minValue,maxValue)
        if (a,b) not in operations.keys():
            operations[(a,b)] = 1
            noOperation += 1
    return operations

def afficher(operations,operation="+",output=sys.stdout):
    for key in operations.keys():
        print(key[0], operation, key[1], "=", file=output)

def main(parametres):
    nbOperations=50
    operation = "+"
    minValue = 1
    maxValue = 9
    if len(parametres) > 1:
        for param in parametres:
            tab = param.split("=")
            if tab[0] == "operation":
                operation = tab[1]
            elif tab[0] == "nbOperations":
                nbOperations = int(tab[1])
            elif tab[0] == "minValue":
                minValue = int(tab[1])
            elif tab[0] == "maxValue":
                maxValue = int(tab[1])
            else:
                print("parametre inconnu :",tab[0])
    afficher(generate(nbOperations=nbOperations,minValue=minValue,maxValue=maxValue),operation=operation)

if __name__ == "__main__":
    main(sys.argv)
