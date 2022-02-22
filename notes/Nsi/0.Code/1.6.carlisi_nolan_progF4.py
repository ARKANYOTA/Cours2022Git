#!/usr/bin/env python
# vim: set sw=4 sts=4 et fdm=marker:
#┎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ Nom: Carlisi, Prenom: Nolan, Classe: TG 04 ┃
#┃ Creation: 06/10/2021 08:15:53              ┃
#┃ Mise a jour: 08/10/2021 11:32:27           ┃
#┃ Fichier: 1.6.carlisi_nolan_progF4.py       ┃
#┃ Exercice fiche 4                           ┃
#┖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# Exos {{{1
# Exo 1 {{{2
def truc(a,b):
    print(f"{a=}, {b=}")
    if b==0: return a
    return truc(a+1, b-1)

# print(f"a=7, b=5, {truc(7, 5)=}")

# Exo 2 {{{2
def fctA():
    print ("Début fonction fctA")
    i=0
    while i<5:
        print(f"fctA {i}")
        i = i + 1
    print ("Fin fonction fctA")

def fctB():
    print ("Début fonction fctB")
    i=0
    while i<5:
        if i==3:
            fctA()
            print("Retour à la fonction fctB")
        print(f"fctB {i}")
        i = i + 1
    print ("Fin fonction fctB")

# fctB()

# Exo 3 {{{2

def fact1(n):
    P=1
    for k in range(1,n+1):
        P=P*k
    return P

def fact2(n):
    P=1
    cpt=n
    while cpt>0:
        P=P*cpt
        cpt=cpt-1
    return P

def fact3(n):
    if n<=1:
        return 1
    else :
        return n*fact3(n-1)


# print(fact3(998))
# 
# 
# n = int(input("n = "))
# print(fact1(n))
# print(fact2(n))
# print(fact3(n))

# 5) {{{3

from time import *

# d = time()
# fact1(n)
# fin = time()
# print("tps: ", fin-d)
# d = time()
# fact2(n)
# fin = time()
# print("tps: ", fin-d)
# d = time()
# fact3(n)
# fin = time()
# print("tps: ", fin-d)

# Exo 4 {{{2

def f(a,b):
    # assert a >0 and b > 0, "a et b positifs"
    if b==1: return a
    return a+f(a, b-1)

# a=int(input("a : "))
# b=int(input("b : "))
# print(f"{a=}, {b=}, {f(a,b)=}")


def mult(a,b):
    if b < 0:
        if a < 0:
            a = abs(a)
            b = abs(b)
        else:
            b = -b
            a = -a
    if b==1: 
        return a
    return a+mult(a, b-1)

#     elif b > 0:
#         return a+mult(a, b-1)
#     else:
#         return a-mult(a, b+1)

# assert mult(3,5)==15
# assert mult(0,5)==0
# assert mult(-5,4)==-20
# assert mult(7,0)==0
# assert mult(4,-2)==-8
# assert mult(-5,-3)==15

# Exo 4+1(5) {{{2
def cpte_car(txt, car):
    if len(txt)==1:
        return int(car==txt), ""
    else:
        return int(car==txt[0]) + cpte_car(txt[1:], car)[0], txt

def supprime_car(txt, car):
    return txt if txt=="" else ((txt[0] if txt[0]!=car else "") + supprime_car(txt[1:], car))

def bidule(txt):
    return txt if txt=="" else (bidule(txt[1:])+txt[0])
