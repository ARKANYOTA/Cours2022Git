import turtle
import random


### Exo1: VOcabulaire et syntaxe
# class Individu:
#     def __init__(self, nom, prenom, annee_naissance):
#         self.nom = nom
#         self.prenom = prenom
#         self.annee_naissance = annee_naissance
#     def calculAge(self,annee):
#         return annee - self.annee_naissance
#     def estMajeur(self, annee):
#         return self.calculAge(annee) >= 18
# 
# # 1) C'est un consgtructeur
# 
# # 2) Les méthodes = (__ini__, calculAge), et les attributs = (nom, prenom, annee_naissance)
# 
# # 3) Elle renvoie l'age de la personne a un certain temps a partir de l'linput de la function, elle renvoie un nombre(int si on met un int, un float si on met un float pour annee)
# 
# # 4) self représente est fait pour appeleer les attributs du constructeur.
# 
# me = Individu("CARLISI", "Nolan", 2004)
# print(me.estMajeur(2020))


# ### Exo2: Stylo
# 
# """
# Définissez la classe Stylo
# 2. Implémentez le constructeur avec deux attributs :
# - liste_couleurs qui représente la liste des couleurs dont dispose le stylo
# - couleur_actuelle qui représente la couleur choisie.
# Lorsque l’on instancie un stylo, il n’est pas nécessaire d’avoir choisi une
# couleur_actuelle. On peut donc fixer sa valeur à “None” dans le constructeur.
# 3. Implémentez la méthode choisirCouleur(self, couleur) qui va vérifier si la couleur
# choisie est bien dans la liste des couleurs disponibles. Si oui, la couleur actuelle du
# stylo va devenir cette couleur. Si non, un message sera affiché : “Couleur non
# disponible”
# 4. Implémentez la méthode fermerStylo(self) qui permet de rentrer la mine du stylo
# et donc de réinitialiser sa couleur actuelle.
# 5. Testez vos méthodes en créant une instance de Stylo.
# """
# 
# 
# class Stylo:
#     def __init__(self, liste_couleur, couleur_actuelle):
# 	self.liste_couleur = liste_couleur
# 	self.couleur_actuelle = couleur_actuelle
#     def choisirCouleur(self, couleur):
#     	if couleur in self.liste_couleur:
# 	    self.couleur_actuelle = couleur
# 	else:
# 	    print("Couleur non disponible")
#     def fermerStylo(self):
#     	self.couleur_actuelle = None
# 
# stylo1 = Stylo(["rouge", "bleu", "vert"], "bleu")

# ### Exo3: Rectangle
# 
# """
# Un rectangle est défini par une longueur et une largeur.
# 1. Définissez la classe Rectangle
# 2. Implémentez le constructeur de la classe Rectangle
# 3. Modifiez le constructeur en ajoutant une condition pour faire en sorte que la
# longueur soit toujours supérieure à la largeur.
# 4. Implémentez la méthode périmetre(self) qui permet de calculer le périmètre d’un
# rectangle.
# Rappel : Le périmètre d’un rectangle est la somme de tous ses côtés.
# 5. Implémentez la méthode aire(self) qui permet de calculer l’aire d’un rectangle.
# Rappel : L’aire d’un rectangle est égale à la longueur * la largeur
# 6. Implémentez la méthode estCarre(self) qui renvoie True si le rectangle est un
# carré et False sinon.
# 7. Testez vos méthodes en créant une instance de Rectangle
# 8. Implémentez une nouvelle méthode traceRectangle(self) qui va tracer le
# rectangle grâce à turtle.
# """
# 
# class Rectangle:
# 	def __init__(self, longueur, largeur):
# 		self.longueur = longueur
# 		self.largeur = largeur
# 	def perimetre(self):
# 		return 2 * (self.longueur + self.largeur)
# 	def aire(self):
# 		return self.longueur * self.largeur
# 	def estCarre(self):
# 		return self.longueur == self.largeur
# 	def traceRectangle(self):
# 		turtle.forward(self.longueur)
# 		turtle.left(90)
# 		turtle.forward(self.largeur)
# 		turtle.left(90)
# 		turtle.forward(self.longueur)
# 		turtle.left(90)
# 		turtle.forward(self.largeur)
# 		turtle.left(90)
# 
# rectangle1 = Rectangle(10, 5)
# print(rectangle1.traceRectangle())
# 
# ### Exo4: Carte
# 
# """
# Dans cet exercice vous allez implémenter une carte de jeu.
# 1. Définissez la classe Carte
# 2. Implémentez le constructeur (deux seul attribut : la valeur allant de 1 à 13 de la
# carte et sa couleur (Trèfle Carreau Coeur ou Pique)
# 3. Implémentez une méthode estFigure(self) qui indique si la carte est une figure
# ou non. Elle affichera la figure de la carte si c’est une figure et affichera “La carte
# n’est pas une figure” sinon.
# Une figure est un Valet une Dame ou un Roi (de valeur 11, 12 ou 13)
# 4. Implémentez une méthode afficheCarte(self) qui affiche la carte proprement.
# Exemple :
# >> c = Carte(12, ”Coeur”)
# >> c.afficheCarte()
# Dame de Coeur
# >> c = Carte(3, ”Pique”)
# >> c.afficheCarte()
# 3 de Pique
# 5. Implémentez une méthode plusGrande(self,carte) qui prend en paramètre une
# carte et qui renvoie la carte de plus haute valeur.
# """

class Carte:
	def __init__(self, valeur, couleur):
		self.valeur = valeur
		self.couleur = couleur
	def estFigure(self):
		if self.valeur == 11 or self.valeur == 12 or self.valeur == 13:
			return True
		else:
			return False
	def afficheCarte(self):
		if self.valeur == 11:
			print("Valet de " + self.couleur)
		elif self.valeur == 12:
			print("Dame de " + self.couleur)
		elif self.valeur == 13:
			print("Roi de " + self.couleur)
		else:
			print(self.valeur, "de", self.couleur)
	def plusGrande(self, carte):
		if self.valeur > carte.valeur:
			return self
		else:
			return carte
	

### Exo5: Jeu de cartes


"""
Dans cet exercice vous allez implémenter un jeu de cartes.
1. Définissez la classe JeuDeCartes
2. Implémentez une méthode creerPaquet(self) qui va créer un paquet de cartes.
Commencez par définir un tableau vide “paquet” qui contiendra les cartes. Pour
chaque couleur, et pour chaque valeur, la méthode va créer une nouvelle carte et
l’ajouter à “paquet”.
La méthode renverra à la fin “paquet”
3. Implémentez le constructeur de la classe. Il n’y aura qu’un seul attribut “paquet”
qui ne sera pas donné en paramètre mais initialisé dans la constructeur grâce à la
méthode creerPaquet(self).
4. Implémentez une méthode melange(self) qui va mélanger aléatoirement le
paquet. Aidez vous de la méthode shuffle() de la bibliothèque random.
5. Implémentez une méthode afficheJeu(self) qui affiche proprement chaque carte
du jeu.
6. Testez vos méthodes en créant un nouveau paquet de carte, en le mélangeant et
en l’affichant."""

class JeuDeCartes:
	def __init__(self):
		self.paquet = []
	def creerPaquet(self):
		for couleur in ["Coeur", "Carreau", "Pique", "Trèfle"]:
			for valeur in range(1, 14):
				self.paquet.append(Carte(valeur, couleur))
		return self.paquet
	def melange(self):
		random.shuffle(self.paquet)
	def afficheJeu(self):
		for carte in self.paquet:
			carte.afficheCarte()


paquet = JeuDeCartes()
paquet.creerPaquet()
paquet.melange()
paquet.afficheJeu()

### Exo5: Dominos

class domino:
    def __init__(self, d, g):
        self.d = d
        self.g = g
    def pts(self):
        return self.d + self.g
    def blanc(self):
        return not bool(self.g*self.g)
    def double(self):
        



def JeudeDominos:
    def distribuer():
	
        





















































