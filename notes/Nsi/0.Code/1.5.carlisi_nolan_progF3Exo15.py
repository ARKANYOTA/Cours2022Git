#!/usr/bin/env python
# vim: set sw=4 sts=4 et fdm=marker:
#┎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ Nom: Carlisi, Prenom: Nolan, Classe: TG 04 ┃
#┃ Creation: 20/09/2021 16:08:20              ┃
#┃ Mise a jour: 22/09/2021 09:05:21           ┃
#┃ Fichier: 1.4.carlisi_nolan_progF3.py       ┃
#┃ Exercice fiche 3 Exo 1 à 10                ┃
#┖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

import random
def Exo1(): # {{{1
    n = int(input("entier n:"))
    m = int(input("entier m:"))
    return list(range(n, m + 1))


def Exo2(): # {{{1
    return liste_alea(10, 100, 5)

def liste_alea(a, b, n):
    return [random.randint(a, b) for rand in range(n)]

def Exo3(): # {{{1
    pass



def exo3():
    print(cr)

def cree_liste(m, n):
    return list(range(m, n + 1))


def Exercice_4():
    L = liste_alea(0, 20, 7)
    print(L)
    return moyenne(L)


def moyenne(L):
    c = 0
    for k in L:
        c += k
    return c / len(L)


def Exercice_5():
    L = liste_alea(0, 20, 7)
    print(L)
    return mon_max(L)


def mon_max(L):
    c = 0
    for k in L:
        if k > c:
            c = k
    return c


def Exercice_6():
    L = [1, 3, 6, 5, 6, 4, 6]
    print(L)
    return rang_max(L)


def rang_max(L):
    c = 0
    i = -1
    for k in range(len(L)):
        if L[k] > c:
            c = L[k]
            i = k
    return i


def Exo7():
    L = liste_alea(1, 9, 20)
    print(L)
    return localise_max(L)


def localise_max(L):
    c = 0
    i = []
    for k in range(len(L)):
        if L[k] > c:
            i.clear()
            i.append(k)
            c = L[k]
        elif L[k] == c:
            i.append(k)
    return i

def tab01(nb_col: int, nb_lig: int) -> list:
    return [[random.randint(0, 1) for j in range(nb_lig)] for i in range(nb_col)]


def aff_tab(T):
    for i in T:
        print(i)

def transpose(T):
    nv_T = [[] for i in range(len(T[1]))]
    for ii, i in enumerate(T):
        for ij, j in enumerate(i):
            nv_T[ij] += [j]
    return nv_T

def exo12():
    print(nb_elt([1, [2, [3, [4, [5, []]]]]]))


def nb_elt(T) -> int:
    count = 0
    for i in T:
        if isinstance(i, list):
            count += nb_elt(i)
        else:
            count += 1
    return count



def Espacement(n):  # {{{1
    print("=================")
    print(f"Exo {n}\n")


if __name__ == "__main__": # {{{1
    tab = tab01(10, 5)
    aff_tab(tab)
    aff_tab(transpose(tab))
    
    import sys
    Exos = [Exo1, Exo2, Exo3] # , Exo4, Exo5, Exo6, Exo7, Exo8, Exo9, Exo10, Exo11]
    # Si il y'a un argument dans l'execution 
    if len(sys.argv) == 1 or (not sys.argv[1].isdigit()):
        for index,i in enumerate(Exos):
            Espacement(index+1)
            retour = i()
            if retour != None:
                print(retour)
    else:
        Espacement(sys.argv[1])
        retour = Exos[int(sys.argv[1])-1]()
        if retour != None:
            print(retour)
        
        

    print("C'est la fin")


