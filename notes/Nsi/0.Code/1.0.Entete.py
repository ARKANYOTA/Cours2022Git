#!/usr/bin/env python
##############################################
# Date: 08.09.2021                           #
# Nom: Carlisi, Prenom: Nolan, Classe: TG 04 #
# Exo: Exo Prog Fiche n°1                    #
##############################################

def transpose(table):
    """Create transpoded of table"""
    transp = []
    for i in range(len(table[0])):
        transp.append([])
        for j in range(len(table)):
            transp[i].append(table[j][i])
    return transp

