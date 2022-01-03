# PROJET TICTACTOE TERMINALE NSI AIDE"

""" Joueur """

class Joueur:

    # Un joueur possède 2 attributs : un nom et un symbole ("X" ou "O").

    def __init__(self, ...):

        # Le constructeur de Joueur.


    def __str__(self):

        # La méthode __str__ qui permet d'afficher un joueur.





""" Case """

class Case:

    # Une Case possède 2 attributs : une position et une valeur. La position correspond au numéro de la case (0 à 8) et la valeur correspond au symbole présent dans la case ("X", "O" ou None si la case est vide).

    def __init__(self, ...):

        # Le constructeur de Case.


    def __str__(self):

        # La méthode __str__ qui permet d'afficher une Case. Si la case est vide elle renvoie la position de la case sinon elle renvoie la valeur de la case.






""" Grille """

class Grille:

    # Une Grille possède 1 attribut : un tableau de 9 Cases.


    def __init__(self):

        # Le constructeur de Grille.


    def verif_case(self, ...):

        # Permet de verifier si une Case a une certaine position est vide ou non. Si la case est vide, la méthode renvoie True et renvoie False sinon.



    def joue(self, ...):

        # Permet de changer la valeur d'une Case a une certaine position en "X" ou "O".



    def verif_victoire(self):

        # Permet de verifier s'il y a un vainqueur horizontalement, verticalement ou diagonalement.



    def __str__(self):

        # La méthode __str__ qui permet d'afficher une Grille sous la forme : | | | |
        #                                                                     | | | |
        #                                                                     | | | |






""" Jeu """

class Jeu:

     # Un Jeu possède 4 attributs : Une liste de Joueurs, une Grille, un indice du joueur actuel (pour pouvoir récuperer le Joueur dans la liste des Joueurs) et un compteur de coups joués.

    def __init__(self):

        # Le constructeur de Jeu.

    def joueur_actuel(self):

        # Permet de renvoyer le Joueur correspondant à l'indice du joueur actuel.


    def joueur_suivant(self):

        # Permet de changer l'indice du joueur actuel (Si 0 passe à 1 et inversement).


    def tour(self):

        # Permet de gérer un tour de jeu :
        # Affiche la Grille de jeu
        # Demande au joueur une Case où jouer
        # Boucle tant que la case choisie n'est pas vide
        # Joue le symbole du joueur dans la case choisie
        # Augmente le compteur de coups


    def jeu_entier(self):

        # Permet de gérer le jeu en entier :
        # Boucle tant qu'il n'y a pas de gagnant ou égalité
        # Effectue un tour de jeu
        # Verifie s'il y a un gagnant ou égalité et affiche le message correspondant
        # Si non, change de joueur



