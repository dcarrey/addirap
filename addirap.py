"""
=============================================================================
= addirap : générateur d'addition pour l'approche addirap 
= auteur : Alix boc
= date : 2022
=============================================================================
"""
from random import randint

nbOperations = 50
noOperation = 0
maxValue = 9
minValue = 1
operations = {}

while noOperation < nbOperations:
    a = randint(minValue,maxValue)
    b = randint(minValue,maxValue)
    if (a,b) not in operations.keys():
        operations[(a,b)] = a+b
        noOperation += 1

for key in operations.keys():
    print(key[0], "+", key[1], "=")
