#!/usr/bin/env python
# vim: set sw=4 sts=4 et fdm=marker:
#┎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ Nom: Carlisi, Prenom: Nolan, Classe: TG 04 ┃
#┃ Creation: 11/10/2021 14:42:08              ┃
#┃ Mise a jour: 11/10/2021 16:06:23           ┃
#┃ Fichier: TD1_Modele_relationnel.py         ┃
#┃ TD 1                                       ┃
#┖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# Exercice 1 {{{1
"""
a) id: INT, nom: STR, prenom: STR, date_naissance: DATE
b) 
| id | nom     | prenom  | date_naissance
------------------------------------------
| 2  | Tripoli | Etienne | 06/07/2001
| 3  | Dann    | Laura   | 25/12/2004
c) 
INDIVIDUS(_id_: INT, nom: STR, prenom: STR, date_naissance: DATE)
"""

# Exercice 2 {{{1
"""
CLIENTS   (_identifiant_: INT,nom: STR, prenom: STR, phone: INT(10), adresse: STR)
ARTICLES  (_code_: INT, nom: STR, desc: STR, prix: FLOAT)
COMMANDES (_numcommand_: INT, identifiant#: INT, code#: INT, datecommande: DATE)
"""

# Exercice 3 {{{1
"""
a)
Joueurs:
| Pseudo      | IP              | Date_Inscription| Or | Guilde
|-----------------------------------------------------------------------
| Thatoryl    | 166.219.88.149  | 16/11/2017 | 2113 | La communauté de l’anneau
| Nhamashal   | 199.154.114.125 | 03/07/201  | 3719 | L’armée du Mordor
| Rhenalyrr   | 20.73.30.74     | 23/08/2017 | 2327 | Les Elyséens
| Khaalindaan | 11.6.205.144    | 09/01/2020 | 4873 | L’organisation XIII
| Paulorin    | 235.180.9.184   | 01/02/2017 | 4956 | L’organisation XIII

Guildes: 
| Guilde           | Classement | Reputation | Type
-----------------------------------------------------------
| L’armée du Mordor         | 1 | Hostile    | Guerriere
| La communauté de l’anneau | 4 | Pacifique  | Aventure
| L’organisation XIII       | 2 | Hostile    | Scientifique
| Les Elyséens              | 3 | Neutre     | Guerriere

b)
clé primaire:
    - Joueurs -> Pseudo
    - Guildes -> Guilde
clé étrangères:
    - Joueurs -> [Guildes]

c)
JOUEURS(_Pseudo_: STR, IP: STR, Date_Inscription: DATE, Or: INT, Guilde#: STR)
Guildes(_Guilde_: STR, Classement: INT, Reputation: STR, Type: STR)
"""


# Exercice 4 {{{1
"""
R1 (A, B, C, D)
avec :  A → B, C
        B → D
> R1(_A_, B#, C)
> RR(_B_, D)
---
R2 (A, B, C, D, E)
avec :  A, B → C, E
        B → D

> R2 (_A_, _B#_, C, D)
> RR (_B_, D)
---
R3 (A, B, C, D, E, F)
avec : A → C
       AB → D,F
       C → E
> R3 (_A_, C#)
> RR (_A#_, _B_, D, F)
> RS (_C_, E)
---
R4 (A, B, C, D)
avec :  A → C
        B → D
> R4 (_A#_, _B#_)
> RR (_A_, C)
> RS (_B_, D)
"""

# Exercice 5 {{{1
"""
a) car il y'a pluieurs idJoueur avec la même valeur, et les joueurs peuvent avoir la même console
b) Oui elle sont redondantes avec un cote associée au prix_cote eux meme associé à la consle et son édition
c) avoir une cote ou cote prix pour deux console et édition differantes


d et e)
Joueur (_idJoueur_: INT, _idConsole#_: INT, annee_achat: INT)
Console(_idConsole_: INT, nom_console: STR, edition_console: STR, cote: STR, prix_cote: INT)
"""


# Exercice 6 {{{1
"""
a)
Eleves (_numero_: INT, nom: STR, prenom: STR, classe#: INT)
Professeurs (_identifiant_: INT, nom: STR, prenom: STR)
classes (_id_: INT, intitule_classe: STR, prof_principal_id#: INT)
Matieres (_id_: INT, initule_matiere: STR)
Cours (_matiere#_, classe#, prfesseur#)
Note (_numero_: INT, valeur: INT, coeff: FLOAT, eleve#: INT, matiere#: INT)
b) 
Eleves (_numero_: INT, nom: STR, prenom: STR, classe#: INT)
                                              Classes.id
Professeurs (_id_: INT, nom: STR, prenom: STR)
classes (_id_: INT, intitule_classe: STR, prof_principal_id#: INT)
                                            Professeurs.id
Matieres (_id_: INT, initule_matiere: STR)
Cours (_matiere#_, classe#, prfesseur#)
        Matieres.id
Note (_numero_: INT, valeur: INT, coeff: FLOAT, eleve#: INT, matiere#: INT)
                                            Eleves.numero , Matieres.id
"""
