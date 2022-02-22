#!/usr/bin/env python
# vim: set sw=4 sts=4 et fdm=marker:
#┎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ Nom: Carlisi, Prenom: Nolan, Classe: TG 04 ┃
#┃ Creation: 13/10/2021 08:19:29              ┃
#┃ Mise a jour: 19/11/2021 12:15:37           ┃
#┃ Fichier: 1.8.carlisi_nolan_progF6.py       ┃
#┃ Exercice fiche 6                           ┃
#┖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

from turtle import *
from time   import sleep

def is_vide(P):
    return len(P)==0



# Exercice 1 {{{1
def spirale(a, long):
    if long >= 0:
        forward(long)
        right(a)
        spirale(a, long-5)


# Exercice 2 {{{1
def cercles(n):
    if n>0:
        circle(n, 360)
        cercles(n-5)

def polygone(n, long):
    assert 360%n==0, "!possible"
    angle = 360//n
    for k in range(n):
        forward(long)
        left(angle)

def des_polygones(n, long):
    if long>0:
        polygone(n, long)
        des_polygones(n, long-5)
        #polygone(n-5, long)


# Exercice 3 {{{1
def dessin_recursif(n, max_n=None, angle=360):
    max_n = n if max_n is None else max_n
    n_angle = ((n-1)/max_n)*360
    if n <= 0: return None
    setheading(angle)
    up()
    goto(0,0)
    down()
    l = 20
    begin_fill()
    for i, j in [(1, 1), (5, 1), (6, 1), (2, 1), (4, -1), (3, 1),(1, 1)]:
        forward(i*l)
        left(90*j)
    end_fill()
    dessin_recursif(n-1, max_n,n_angle)
    

# Exercice 4 {{{1
def parenthese(txt, n):
    if txt=="":
        return n==0
    else:
        if txt[0]=="(":
            return parenthese(txt[1:], n+1)
        elif txt[0]==")":
            return parenthese(txt[1:], n-1)
def parenthese2(txt, n):
    print(txt, n)
    if n<0:
        return False
    if txt=="":
        return n==0
    else:
        if txt[0]=="(":
            return parenthese2(txt[1:], n+1)
        elif txt[0]==")":
            return parenthese2(txt[1:], n-1)
            
def parenthese3(txt, n):
    print(txt, n)
    if n<0:
        return False
    if txt=="":
        return n==0
    else:
        if txt[0]=="(":
            return parenthese3(txt[1:], n+1)
        elif txt[0]==")":
            return parenthese3(txt[1:], n-1)
        else:
            return parenthese3(txt[1:], n)

# Exercice 5 {{{1
def consecutifs(L):
    if len(L) <= 1: return False
    return True if L[0]+1==L[1] else consecutif(L[1:])
    # VERSION MONOLINE
    # return if len(L) <= 1 else (True if L[0]+1==L[1] else consecutif(L[1:]))

# Exercice 6 {{{1
def som(x, n):
    if n<=0:
        return 1
    print(f"{x=} * som({x=}, {n-1=})+1")
    return x * som(x, n-1)+1

# Exercice 7 {{{1
def u(n):
    if n==0: return 5
    return u(n - 1)+2*v(n - 1)

def v(n):
    if n==0: return 2
    return 2*u(n-1)+v(n-1)
# Exercice 8 {{{1
def fusion(T1,T2):
    if T1==[]: return T2
    if T2==[]: return T1
    if T1[0]<T2[0]:
        return [T1[0]]+fusion(T1[1:], T2)
    else:
        return [T2[0]]+fusion(T1, T2[1:])

def trifusion(T):
    if len(T)<=1: return T
    T1=[T[x] for x in range(len(T)//2)]
    T2=[T[x] for x in range(len(T)//2, len(T))]
    return fusion(trifusion(T1), trifusion(T2))
# Exercice 9 {{{1
def numero(x,y):
#     if x>0:
#        print(f"\033[33mx\033[0m = {x}, y = {y}: ", numero(x-1, y)+x+1)
#        return numero(x-1, y)+x
#    elif y>0:
#        print(f"x = {x}, \033[33my\033[0m = {y}: ", numero(x, y-1)+y+1)
#        return numero(x, y-1)+y
#    else:
#        return 0
    if y!=0:
        return numero(x+1, y-1)+1
    else: # y=0
        if x==0:
            return 0
        else:
            return numero(0, x-1)+1

# IF NAME == MAIN: {{{1
if __name__== "__main__":
    # speed("fastest")
    ## Exo 2
    # des_polygones(4, 80)
    # des_polygones(6, 80)
    ## Exo 3
    # dessin_recursif(4)
    ## Exo 4
    # print(parenthese3("test", 0))
    # print(parenthese3("()", 0))
    # print(parenthese3("(test)", 0))
    # print(parenthese3("(hello)azer)", 0))
    # print(parenthese3("((m) ) (on()t( est (est (bo))n))", 0))
    # print(parenthese3("((m) ) (on)t( est (est (bo))n))", 0))
    # print(parenthese3("truc(22()bidule(23)56", 0))
    ## Exo 5
    ## Exo 6
    # print(som(5, 3))
    ## Exo 7
    # for i in range(10):
    #     print(i,"\t", u(i), "\t", v(i))

    # sleep(1)

    ## Exo 8
    # print(fusion([1,4,5,6,7,3,4,5], [2,5,6,7,3]))
    # print(trifusion([1,4,5,6,7,3,4,5]))
    ## Exo 9
    print(0, numero(0,0))
    print(1, numero(1,0))
    print(2, numero(0,1))
    print(3, numero(2,0))
    print(4, numero(1,1))
    print(12, numero(2,2))
    print(11, numero(3,1))



