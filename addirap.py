"""
=============================================================================
= addirap : générateur d'addition pour l'approche addirap
= auteur : Alix boc
= date : 2022
=============================================================================
"""
from random import randint
from docx import Document
from docx.shared import Inches, Pt, Cm
from docx.enum.section import WD_SECTION,WD_ORIENT
from docx.oxml.ns import qn
import sys

letter = {"width":21.51,"height":27.94}
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

def formatDocxSection(doc):
    sections = doc.sections
    for section in sections:
        section.orientation = WD_ORIENT.LANDSCAPE
        section.page_width = Cm(letter["height"])
        section.page_height = Cm(letter["width"])
        section.top_margin = Cm(1)
        section.bottom_margin = Cm(1)
        section.left_margin = Cm(0.5)
        section.right_margin = Cm(0.5)

def afficher(mode,operations,operation="+",outputfile="addirap.docx"):
    doc = Document()
    section = doc.add_section(WD_SECTION.CONTINUOUS)
    section.start_type
    p1 = doc.add_heading("mode : " + mode)

    section = doc.add_section(WD_SECTION.CONTINUOUS)
    section.start_type
    section = doc.sections[2]
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Arial'
    font.size = Pt(14)

    # Set to 2 column layout
    sectPr = section._sectPr
    cols = sectPr.xpath('./w:cols')[0]
    cols.set(qn('w:num'),'3')

    for key in operations:
        p1 = doc.add_paragraph(str(key[0])+" "+operation+" "+str(key[1])+" =")
    formatDocxSection(doc)
    doc.save(outputfile)

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
    mode = "moyen"
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
                mode = tab[1]
                (minValue,maxValue) = validerMode(tab[1],minValue,maxValue)
            else:
                print("parametre inconnu :",tab[0])
    afficher(mode,generate(nbOperations=nbOperations,minValue=minValue,maxValue=maxValue),operation=operation)

if __name__ == "__main__":
    main(sys.argv)
