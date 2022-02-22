#!/usr/bin/env python
# vim: set sw=4 sts=4 et fdm=marker:
#┎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ Nom: Carlisi, Prenom: Nolan, Classe: TG 04 ┃
#┃ Creation: 19/09/2021 22:26:05              ┃
#┃ Mise a jour: 20/09/2021 08:46:40           ┃
#┃ Fichier: 1.3.carlisi_nolan_progF3App2.py   ┃
#┃ Exercice fiche 3 App 2                     ┃
#┖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

def cherche_max(liste: dict) -> int:  # {{{1
    if len(liste)==0:
        return None
    element_max = liste[0]
    for i in liste[1:]:
        element_max = max(element_max, i)
    return element_max

def compte_max(liste: dict) -> tuple[int, int]:  # {{{1
    if len(liste)==0:
        return None, 0
    element_max = liste[0]
    nb_occurence = 1
    for i in liste[1:]:
        if element_max == i:
            nb_occurence += 1
        elif element_max < i:
            nb_occurence = 1
            element_max = i

    return element_max, nb_occurence

def localise_max(liste: dict) -> tuple[int, dict]:  # {{{1
    if len(liste)==0:
        return None, []
    element_max = liste[0]
    occurence = [0]
    for index, i in enumerate(liste[1:]):
        if element_max == i:
            occurence += [index+1]
        elif element_max < i:
            occurence = [index+1]
            element_max = i

    return element_max, occurence


def cherche_car(chaine: str, char: chr) -> bool:  # {{{1
    return char in chaine
    #OU
    for i in chaine:
        if char == i:
            return True
    return False

def rang_elt1(chaine: str, char: chr) -> dict:  # {{{1
    if chaine=="":  # INUTILE
        return []  # INUTILE
    occurence = []
    for index, i in enumerate(chaine):
        if char == i:
            occurence += [index]

    return occurence

def rang_elt2_1(liste_int: dict, entier: int) -> dict:  # {{{1
    occurence = []
    for index, i in enumerate(liste_int):
        if entier == i:
            occurence += [index]

    return occurence
def rang_elt2_2(liste_int: str, entier: int) -> dict:  # {{{1
    occurence = []
    for index, i in enumerate(liste_int):
        if str(entier) == str(i):
            occurence += [index]

    return occurence



if __name__ == "__main__":  # {{{1
    liste = [1,4,6,8,3,8,4,8,2]
    print(cherche_max(liste))
    print(compte_max(liste))
    print(localise_max(liste))
    print(cherche_car("azertyuiop", "d"))
    print(cherche_car("azertyuiop", "r"))
    print(rang_elt1("azertyeeoe", "e"))
    print(rang_elt2_1([9,4,2,6, 9,8,1], 9))
    print(rang_elt2_2("194059839", 9))

# QUESTIONS: {{{1
"""
2) Que elle se ressemble enormement. 
"""
