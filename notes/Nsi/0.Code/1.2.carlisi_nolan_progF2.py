#!/usr/bin/env python
# vim: set sw=4 sts=4 et fdm=marker: {{{1
#┎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ Nom: Carlisi, Prenom: Nolan, Classe: TG 04 ┃
#┃ Creation: 15/09/2021 08:16:08              ┃
#┃ Mise a jour: 17/09/2021 09:36:53           ┃
#┃ Fichier: 1.2.carlisi_nolan_progF2.py       ┃
#┃ Exercice fiche 2                           ┃
#┖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# Le {{{1 permet de plier le code dans mon editeur

# {{{1
import random
def Exo1(): # {{{1
    n = int(input("Nombre n:"))
    if n > 50: 
        print("Gagné")
    else: 
        print("Perdu")
    note = int(input("Nombre note entre 0 et 20:"))
    if note >= 10:
        print("Admis")
    elif note >= 8:
        print("Second groupe")
    else:
        print("Refusé")


def Exo2(): # {{{1
    n = int(input("Un entier positif: "))
    for i in range(n+1):
        print(f"2 puissance {i} vaut {2**i}")


def Exo3(): # {{{1
    n = int(input("Un entier positif: "))
    S = (n*(n+1))//2
    print(f"S = {S}")


def Exo4(): # {{{1
    M = int(input("Un entier strictement positif: "))
    n = 0
    S = 0 
    while S < M:
        n +=1
        S += n
    print(f"pour n={n} S={S} > {M}")


def Exo5(): # {{{1
    n = int(input("Un entier positif : "))
    for i in range(10):
        print(f"{i} x {n} = {i*n}")


def Exo6(): # {{{1
    for i in range(10):
        print(f"Table de multiplication de {i}")
        for j in range(10):
            print(f"\t{i} x {j} = {i*j}")


def Exo7(): # {{{1
    txt = input("Le texte : ")
    car = input("Le caractère : ")
    occ_car = 0
    for i in txt:
        if i==car:
            occ_car += 1
    print(occ_car)


def Exo8(): # {{{1
    txt = input("Le texte : ")
    car = input("Le caractère : ")
    new_txt = ""
    for i in txt:
        if not i==car:
            new_txt += i
    print(new_txt)
    

def Exo9(): # {{{1
    txt = input("Le texte : ")
    car = input("Le caractère à modifier : ")
    nv_car = input("Le caractère à remplaçant : ")
    new_txt = ""
    for i in txt:
        if i==car:
            new_txt += nv_car
        else:
            new_txt += i
    print(new_txt)


def Exo10(): # {{{1
    txt = input("Le texte en majuscules: ")
    new_txt = ""
    for i in txt:
        if not i in "AEIOUY":
            new_txt += i
    print(new_txt)


def Exo11(): # {{{1
    # Génération du tableau
    table = [[chr(i*6+j+65 if i*6+j+65 < 91 else i*6+j+22) for j in range(6)]for i in range(6)]
    dico_cl = {} # key: clé, value: letter
    dico_lc = {} # key: letter, value: clé
    # Espace etant codée comme charactère comportant un 0
    for ii, i in enumerate(table):
        for ij, j in enumerate(i):
            dico_cl[str(ii+1) + str(ij+1)] =j
            dico_lc[j] =str(ii+1) + str(ij+1)
    
    print(dico_cl, dico_lc)
    e_decode = input("(e)ncode/(d)ecode : ")
    if e_decode == "e":
        encoded_str = ""
        for i in input("Texte à encoder: ").upper():
            if i==" ":
                encoded_str += random.choice(["0"+str(i) for i in range(0,10)]+ [str(i)+"0" for i in range(0,10)])
            else:
                encoded_str += dico_lc.get(i, "??")
        return encoded_str
    elif e_decode == "d":
        decoded_str = ""
        char = ""
        for i in input("Texte à décoder: ").upper():
            char += i
            if len(char) == 2:
                if "0" in char:
                    decoded_str += " "
                else:
                    decoded_str += dico_cl.get(char, "?")
                char = ""
        return decoded_str
    else:
        return


def Espacement(n): # {{{1
    print("=================")
    print(f"Exo {n}\n")


if __name__ == "__main__": # {{{1
    import sys
    Exos = [Exo1, Exo2, Exo3, Exo4, Exo5, Exo6, Exo7, Exo8, Exo9, Exo10, Exo11]
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
