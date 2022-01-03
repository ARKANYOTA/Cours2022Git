#!/usr/bin/env python
# vim: set sw=4 sts=4 et fdm=marker:
#┎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ Nom: Carlisi, Prenom: Nolan, Classe: TG 04 ┃
#┃ Creation: 17/12/2021 09:51:07              ┃
#┃ Mise a jour: 17/12/2021 11:07:29           ┃
#┃ Fichier: Sujet17.py                        ┃
#┃ Exercice fiche 17                          ┃
#┖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


#Exercice 1:

def indice_du_min(liste: list) -> int:
    # Entrée : Liste
    # Sortie : Interge, indice de la liste, ou -1 si liste vide
    if len(liste)==0:
        return -1
    else:
        minimum = 0
        for i in range(1, len(liste)):
            if liste[minimum] > liste[i]:
                minimum = i
        return minimum

print(indice_du_min([5]))
print(indice_du_min([2, 4, 1]))
print(indice_du_min([5, 3, 2, 2, 4]))

# Exercice 2

def separe(tab):
    i = 0
    j = len(tab) - 1
    while i < j:
        if tab[i] == 0:
            i = i + 1
        else:
            tab[i], tab[j] = tab[j], tab[i]
            j -= 1
    return tab

# separe([1,0,0,1,0,0,1,1,1,0,1,1])

# Sujet 18

# Exercice 1

def maxi(tab):
    if len(tab)==0:
        return (None, None)
    else:
        M = 0
        for i in range(1, len(tab)):
            if tab[M] < tab[i]:
                M = i
        return (tab[M], M)

print(maxi([1,5,6,9,1,2,3,7,9,8]))

# Exo 2

def positif(T):
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = []
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print(T)
    return T2

print(positif([-1,0,4,5,-1,-93,83,1]))


# Sujet 15:

# Exo 1:

def rechercheMinMax(tab):
    if len(tab)==0:
        return {'min': None, 'max': None}
    valeurs = {'min': tab[0], 'max': tab[0]}
    for i in tab:
        if valeurs['min'] > i:
            valeurs['min'] = i
        if valeurs['max'] < i:
            valeurs['max'] = i
    return valeurs

print(rechercheMinMax([0,1,4,2,-2,9,3,1,7,1]))
print(rechercheMinMax([]))

# Exo 2:
class Carte:
    """Initialise Couleur (entre1 à 4), et Valeur (entre1 à 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v
    """Renvoiele nom de la Carte As, 2, ... 10, Valet, Dame, Roi"""
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"

        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"
    """Renvoiela couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique','coeur', 'carreau', 'trefle'][self.Couleur]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []
    """Remplit le paquet de cartes"""
    def remplir(self):
        for i in range(1,13+1): 
            for j in range(1, 4+1): # Pour toutes les couleurs
                self.contenu.append(Carte(j,i))
    """Renvoiela Carte qui se trouve à la position donnée"""
    def getCarteAt(self, pos):
        return self.contenu[pos]

unPaquet = PaquetDeCarte()
unPaquet.remplir()
uneCarte = unPaquet.getCarteAt(20)
print(uneCarte.getNom()+ " de " + uneCarte.getCouleur())

# Sujet 2:

# Exo 1:

def rendu(somme_a_rendre: int) -> list:
    a_rendre = [0, 0, 0]
    if somme_a_rendre <= 0:
        raise Exception("Entier positif non nul")
    for i, j in enumerate(5, 2, 1):
        while somme_a_rendre >= j:
            somme_a_rendre -= j
            a_rendre[i] += 1
    return a_rendre

print(rendu(13))
print(rendu(64))
print(rendu(89))







# Sujet 6

# Exo 1:
# Sujet 6

# Exo 1:
# Sujet 6

# Exo 1:
# Sujet 6

# Exo 1:
# Sujet 6

# Exo 1:
