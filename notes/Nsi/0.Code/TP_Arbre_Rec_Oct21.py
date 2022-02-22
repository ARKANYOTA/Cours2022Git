#!/usr/bin/env python
# vim: set sw=4 sts=4 et fdm=marker:
#-------------------------------------------
# Tp dictionnaires, récursivité et arbres
# Octobre 21
# Nom : CARLISI
# Prénom : Nolan
# Classe : TG 04
#-------------------------------------------


# Les imports
#-------------
from random import *



          #####################
          #   Les fonctions   #
          #####################

# Les fonctions d'entrée /sortie
#--------------------------------
'''
La fonction aff_arbre(a):
Prend en argument un dictionnaire de dictionnaire a
représentant un arbre binaire et affiche pour chaque noeud :
sa valeur et la valeur de ses deux fils
si pas de fils affiche -
 '''
def aff_arbre(a):
  print(23*"-")
  for c,v in a.items():
    if v["fg"]==None:
      fg="-"
    else:
      fg=v["fg"]
    if v["fd"]==None:
      fd="-"
    else: fd=v["fd"]  
    print ("noeud : ",c," {fg:",fg," fd:",fd,"}",sep="") 
  print(23*"-")

# Placer une valeur dans un arbre
#--------------------------------
def place(s:int,x:int,a:dict)->dict:
   # Données : s valeur du sommet du sous_arbre exploré
   #           x (différent de s) valeur à placer dans l'arbre
   #           a dictonnaire de dictionnaires, l'arbre général
   #           a contient au moins un sommet, sa racine. 
   # Résultat : L'arbre initial avec l'entier x bien placé
   if x<s: # x doit être dans le sous arbre gauche
     if a[s]["fg"]==None:
        a[x]={"fg":None,"fd":None}
        a[s]["fg"]=x
        return a
     else:
        return place(a[s]["fg"],x,a)
   else:# x doit être dans le sous arbre droit
     if a[s]["fd"]==None:
        a[x]={"fg":None,"fd":None}
        a[s]["fd"]=x
        return a
     else:
        return place(a[s]["fd"],x,a)

    
# Lire un arbre
#--------------------------------
def lire(s:int,a:dict):
  # Fonction qui permet d'afficher les éléments de l'arbre
  # s est le sommet du sous-arbre exploré
  # a est le dictionnaire représentant l'arbre
  if a[s]["fg"]!=None:    # cas où le sommet s a un fils gauche
     lire(a[s]["fg"],a)   # on lit le sous-arbre gauche du sommet s

  print(s,end=" ")        # on affiche le sommet s
                          #(remplacer le saut de ligne par un espace)
  if a[s]["fd"]!=None:    # cas où le sommet s a un fils droit
     lire(a[s]["fd"],a)   # on lit le sous-arbre droit du sommet s

def stocke(s,a,res):
  # Fonction qui permet de stoker les éléments lus de l'arbre
  # s est le sommet du sous-arbre exploré
  # a est le dictionnaire représentant l'arbre
  # res est la liste donnant les éléments lus de l'arbre
  # Il n'y a pas de return car la liste est modifiée sur place
  if a[s]["fg"]!=None:
     stocke(a[s]["fg"],a,res)
  res.append(s)
  if a[s]["fd"]!=None:
     stocke(a[s]["fd"],a,res)
  

# Créer un listes des entiers de 1 à n mélangée
def listalea(n):
   L=[k for k in range(1,n+1)]
   shuffle(L)  # Fonction mélangeant les éléments d'une liste
   return L



          ####################
          #   Le programme   #
          ####################



# Listes pour les différents jeux d'essais
# ----------------------------------------
#L=[6,2,8,4,7,9,5,1,3]
#L=[8,4,2,9,1,6,10,5,11,7,3]
#L=[7,14,3,5,2,11,9,12,1,17]
#L=[1,2,3,4,5]
#L=[5,4,3,2,1]
#L=[2,4,6,5,3,1]
#L=[2,1,4,3,6,5]
#L=listalea(12)

# Initialisation de l'arbre
arbre={L[0]:{"fg":None,"fd":None}}
print("La liste initiale :",L)

# Création de l'arbre
for k in range(1,len(L)):
    arbre = place(L[0],L[k],arbre)
# Affichage de l'arbre
print("L'ABR associé :")
aff_arbre(arbre)
# Lecture de l'arbre
print("Résultat de la lecture de l'ABR")
lire(L[0],arbre)
print()
nv_L=[]
stocke(L[0],arbre,nv_L)
print("nv_L=",nv_L)


