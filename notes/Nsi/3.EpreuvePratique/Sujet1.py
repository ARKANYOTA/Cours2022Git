#!/usr/bin/env python
# vim: set sw=4 sts=4 et fdm=marker:
#┎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ Nom: Carlisi, Prenom: Nolan, Classe: TG 04 ┃
#┃ Creation: 15/12/2021 07:18:10              ┃
#┃ Mise a jour: 15/12/2021 07:40:32           ┃
#┃ Fichier: Sujet1.py                         ┃
#┃ Exercice fiche 1                           ┃
#┖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛




# Exercice 1:

def moyenne(tab):
    if len(tab)==0:
        print("erreur")
        return "erreur"
    else:
        somme = 0
        for i in tab:
            somme+=i
        return somme/len(tab)

print(moyenne([5, 3, 8]))
print(moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(moyenne([]))

# Exercice 2:

def tri(tab):
    #i est le premier indice de la zone non triee, j le dernier indice.
    #Au debut, la zone non triee est le tableau entier.
    i = 0
    j = len(tab)-1
    while i != j :
        if tab[i] == 0:
            i = i+1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j = j-1
    return tab

print(tri([0,1,0,1,0,1,0,1,0]))

# Sujet 3

# Exercice 1

def multiplication(n1, n2):
    result = 0
    if n1 > 0:
        for i in range(n1):
            result += n2
    elif n1 < 0:
        for i in range(-n1):
            result += n2
        result = -result
    else:
        result = 0
    return result

print(multiplication(3,5))
print(multiplication(-4,-8))
print(multiplication(-2,6))
print(multiplication(-2,0))


# Exo 2
def dichotomie(tab, x):
    """
    tab : tableau d’entiers trié dans l’ordre croissant x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = fin-debut
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m-1
    return False
print(dichotomie([15,16,18,19,23,24,28,29,31,33],28))
print(dichotomie([15,16,18,19,23,24,28,29,31,33],27))
